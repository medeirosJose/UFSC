#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>  

// Definição de pinos
// no WeMos as portas tem um D na frente
#define LEDG_PIN_VIN    D6
#define LEDR_PIN_VIN    D9
#define LEDY_PIN_VIN    D5

#define THERMISTOR_PIN_CON1 A0

// define alguns parametros pra aumentar a precisão da medição
// fonte: apostila de iniciante da eletrogate
#define SERIESRESISTOR 10000
#define THERMISTORNOMINAL 10000
#define TEMPERATURENOMINAL 25
#define BCOEFFICIENT 3950
#define Vin 3.3
#define T0 298.15
#define Rt 10000
#define R0 10000
#define T1 273.15
#define T2 373.15
#define RT1 35563
#define RT2 549
float beta = 0.0;
float Rinf = 0.0;
float TempKelvin = 0.0;
float TempCelsius = 0.0;
float Vout = 0.0;
float Rout = 0.0;

// struct de temperaturas pra receber do servidor e posteriomente desempacotar
struct Temperatures {
    float dangerTemp;
    float safeTemp;
};

// credenciais da rede wifi
const char* ssid = "Ap203"; 
const char* password = "13245768"; 

void setup() {
    Serial.begin(9600);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nConectado com sucesso!");
    //Serial.print("Endereço IP: ");
    //Serial.println(WiFi.localIP());

    pinMode(LEDG_PIN_VIN, OUTPUT);
    pinMode(LEDY_PIN_VIN, OUTPUT);
    pinMode(LEDR_PIN_VIN, OUTPUT);

    fadeOut(LEDG_PIN_VIN);
    fadeOut(LEDY_PIN_VIN);
    fadeOut(LEDR_PIN_VIN);

    pinMode(THERMISTOR_PIN_CON1, INPUT);

    beta = (log(RT1 / RT2)) / ((1 / T1) - (1 / T2));
    Rinf = R0 * exp(-beta / T0);
}

void loop() {
    Vout = analogRead(THERMISTOR_PIN_CON1) * Vin / 1024.0; 
    Rout = (Rt * Vout / (Vin - Vout)); 
  
    if (Rout > 0) {
        TempKelvin = (beta / log(Rout / Rinf));
        TempCelsius = TempKelvin - 273.15;
    } else {
        TempCelsius = -999.0; // valor de erro
    }

    // faz um "fetch" das temperaturas enviadas pelo servidor
    Temperatures currentTemps = get_https_data(); 

    if (TempCelsius > currentTemps.dangerTemp) {
        digitalWrite(LEDR_PIN_VIN, HIGH);
        digitalWrite(LEDY_PIN_VIN, LOW);
        digitalWrite(LEDG_PIN_VIN, LOW);
    } else if (TempCelsius >= currentTemps.safeTemp && TempCelsius <= currentTemps.dangerTemp) {
        digitalWrite(LEDY_PIN_VIN, HIGH);
        digitalWrite(LEDR_PIN_VIN, LOW);
        digitalWrite(LEDG_PIN_VIN, LOW);
    } else {
        digitalWrite(LEDG_PIN_VIN, HIGH);
        digitalWrite(LEDR_PIN_VIN, LOW);
        digitalWrite(LEDY_PIN_VIN, LOW);
    }

    //Serial.print("Temperatura em Celsius: ");
    //Serial.print(TempCelsius);
    //Serial.print(" Cº \n");

    // envia ao servidor a temperatura atual lida pelo thermistor
    send_http_post(TempCelsius);

    delay(2000);
}

// faz o envio da temperatura atual para o servidor
void send_http_post(float currentTemp) {
  if (WiFi.status() == WL_CONNECTED) {
      WiFiClient client;
      HTTPClient http;
      http.begin(client, "http://192.168.0.7:3000/receber_temp");
      http.addHeader("Content-Type", "application/json");
      String postData = "{\"currentTemp\":" + String(currentTemp) + "}";
      int httpCode = http.POST(postData);
      String payload = http.getString();
      //Serial.println(httpCode);
      //Serial.println(payload);
      http.end();
  } else {
    Serial.println("Erro na conexão WiFi.");
  }
}

// busca as temperaturas de perigo e seguranca vindas do servidor
Temperatures get_https_data() {
    Temperatures temps;
    temps.dangerTemp = 28.0; // valores padrão
    temps.safeTemp = 25.0;

    if (WiFi.status() == WL_CONNECTED) {
        WiFiClient client;
        HTTPClient http;
        http.begin(client, "http://192.168.0.7:3000/enviar_params");  
        http.addHeader("Content-Type", "application/json");
        int httpCode = http.GET();

        if (httpCode > 0) {
            String payload = http.getString();
            //Serial.println(payload);

            DynamicJsonDocument doc(1024);
            DeserializationError error = deserializeJson(doc, payload);

            if (!error) {
                temps.dangerTemp = doc["dangerTemp"];
                temps.safeTemp = doc["safeTemp"];
            } else {
                Serial.println("Failed to parse JSON");
            }
        } else {
            Serial.print("HTTP response code: ");
            Serial.println(httpCode);
        }
        http.end();
    } else {
        Serial.println("Not connected to WiFi");
    }
    return temps;
}
    

void fadeOut(int pin) {
  for (int i = 255; i >= 0; i -= 5) {
    analogWrite(pin, i);
    delay(15);
  }
  digitalWrite(pin, LOW);
}
