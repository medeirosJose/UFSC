import * as React from "react";
import {
  Text,
  View,
  StyleSheet,
  ScrollView,
  Linking,
  TouchableOpacity,
  Alert,
  Pressable,
  Image,
} from "react-native";
import { Icon, Button } from "@rneui/themed";
import { SocialIcon } from "@rneui/themed";
import { SafeAreaView } from "react-native-safe-area-context";
import { Platform } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import YoutubePlayer from "react-native-youtube-iframe";

//* nome da atração ou artista;
//* endereço onde acontecerá a apresentação;
//* horário de início da apresentação;
//* mapa indicando o local da apresentação;
//* uma ou mais imagens ou fotos da atração ou artista;
//* um vídeo ou uma playlist do artista;
//* link para web site ou redes sociais do artista;
//* valor do ingresso, ou indicação de que a apresentação é gratuita;
//* link do site ou app para compra de ingressos, se for o caso;
//* telefone ou WhatsApp para reservas, caso se aplique.

function AtracoesDetailsScreen({ route, navigation }) {
  const { data } = route.params;

  if (!data.id) {
    data.id = Math.random().toString(36).substring(7);
  }

  const [isFavorite, setIsFavorite] = React.useState(false);

  React.useEffect(() => {
    checkIfFavorite();
  }, []);

  const checkIfFavorite = async () => {
    try {
      const favoriteData = await AsyncStorage.getItem("favoriteAtracoes");
      const parsedFavoriteData = JSON.parse(favoriteData);
      // ve se tem um elemento na lista com o mesmo id
      setIsFavorite(parsedFavoriteData && parsedFavoriteData[data.id]);
    } catch (error) {
      console.error("Erro ao verificar favorito:", error);
    }
  };

  const toggleFavorite = async () => {
    try {
      let favoriteData = await AsyncStorage.getItem("favoriteAtracoes");
      favoriteData = favoriteData ? JSON.parse(favoriteData) : {};

      if (isFavorite) {
        // ja esta na lista, remove da lista
        // Alert.alert("remove");
        delete favoriteData[data.id];
        // console.log(favoriteData);
      } else {
        // nao esta na lista, adiciona na lista
        // Alert.alert("adiciona");
        favoriteData[data.id] = data;
        // console.log(favoriteData);
      }

      // atualiza o asyncstorage com a nova lista
      await AsyncStorage.setItem(
        "favoriteAtracoes",
        JSON.stringify(favoriteData)
      );
      setIsFavorite(!isFavorite); // faz o toggle de fato
    } catch (error) {
      console.error("Erro ao manipular favorito:", error);
    }
  };

  const openTwitterApp = async (twitterUsername) => {
    const twitterAppUrl = Platform.select({
      ios: `twitter://user?screen_name=${twitterUsername}`,
      android: `twitter://user?screen_name=${twitterUsername}`,
    });

    try {
      await Linking.openURL(twitterAppUrl);
    } catch (error) {
      console.error("Erro ao abrir o aplicativo do Twitter:", error);
    }
  };

  const openInstaApp = async (socialUsername) => {
    socialAppUrl = `instagram://user?username=${socialUsername}`;

    try {
      await Linking.openURL(socialAppUrl);
    } catch (error) {
      console.error(`Erro ao abrir o aplicativo:`, error);
    }
  };

  function formatTime(time) {
    const date = new Date(time);
    const hours = date.getHours();
    const minutes = date.getMinutes();

    if (minutes < 10) {
      return `${hours}:0${minutes}`;
    }

    return `${hours}:${minutes}`;
  }

  function formatLocal(local) {
    // divide a string pelo caractere vírgula e pega o primeiro elemento do array
    const endereco = local.split(",")[0];
    return endereco;
  }

  return (
    <SafeAreaView contentContainerStyle={styles.container}>
      <ScrollView style={styles.containerScroll}>
        {/* <View> */}
        <Image
          source={{
            uri: `${data.imagens}`,
          }}
          style={styles.image}
          resizeMode="cover"
        />
        <View style={styles.heartContainer}>
          <Icon
            name="favorite"
            color={isFavorite ? "red" : "white"}
            size={32}
            onPress={toggleFavorite}
          />
        </View>

        <Text style={styles.atracaoTitle}>{data.nome_atracao}</Text>
        <View style={styles.infoContainer}>
          <Icon
            color="black"
            containerStyle={{ marginRight: 4 }}
            disabledStyle={{}}
            iconProps={{}}
            iconStyle={{ color: "#e91e63" }}
            name="place"
            size={32}
            type="material"
          />
          <Text style={styles.text}>{formatLocal(data.endereco)}</Text>
        </View>
        <View style={styles.infoContainer}>
          <Icon
            color="black"
            containerStyle={{ marginRight: 4 }}
            disabledStyle={{}}
            iconProps={{}}
            iconStyle={{ color: "#e91e63" }}
            name="schedule"
            size={32}
            type="material"
          />
          <Text style={styles.text}>{formatTime(data.horario_inicio)}h</Text>
        </View>
        {data.valor_ingresso && (
          <View style={styles.infoContainer}>
            <Icon
              color="black"
              containerStyle={{ marginRight: 4 }}
              disabledStyle={{}}
              iconProps={{}}
              iconStyle={{ color: "#e91e63" }}
              name="money"
              size={32}
              type="material"
            />
            <Text style={styles.text}>{data.valor_ingresso}</Text>
          </View>
        )}
        {/* {console.log(data)} */}
        <Text style={styles.h2}>Sobre o evento</Text>
        <Text style={styles.jsonText}>{data.sobre}</Text>

        <Text style={styles.h2}>Galeria de Fotos</Text>
        <ScrollView horizontal>
          {data.galeria.map((foto, index) => (
            <Pressable
              key={index}
              onPress={() => {
                Linking.openURL(foto);
              }}
            >
              <Image
                source={{ uri: foto }}
                style={{
                  width: 200,
                  height: 200,
                  margin: 6,
                  marginLeft: 0,
                  borderRadius: 4,
                }}
              />
            </Pressable>
          ))}
        </ScrollView>

        <Text style={styles.h2}>Vídeo</Text>
        <YoutubePlayer height={220} play={false} videoId={`${data.video}`} />
        <Text style={styles.h2}>Local do Evento</Text>

        <Text style={styles.jsonText}>{data.endereco}</Text>
        <Button
          buttonStyle={{
            width: "80%",
            borderRadius: 10,
            backgroundColor: "#e91e63",
            marginVertical: 10,
          }}
          title="Ver no mapa"
          onPress={() => {
            Linking.openURL(
              `https://www.google.com/maps/search/?api=1&query=${data.endereco}`
            );
          }}
        />

        {/* checa se o data.valor_ingresso existe, se não existir diz que entrada é franca */}
        <Text style={styles.h2}>Ingressos</Text>
        <View>
          {data.valor_ingresso ? (
            <>
              <Text>Valor do Ingresso: {data.valor_ingresso}</Text>
              <Button
                buttonStyle={styles.ticketButton}
                titleStyle={styles.ticketButtonText}
                onPress={() => {
                  Linking.openURL(data.link_ingressos);
                }}
              >
                Garantir Ingresso
                <Icon name="shopping-cart" color="white" />
              </Button>
              <Text style={styles.h2}>Formas de Pagamento</Text>
              <Image
                source={require("./payment.webp")}
                style={{ height: 50, width: 200, resizeMode: "contain" }}
              />
              <Text style={styles.smallText}>
                Parcelados em até 5x sem juros!
              </Text>
            </>
          ) : (
            <Text style={styles.jsonText}>Entrada Franca</Text>
          )}
        </View>

        {/* nem todos os eventos terão uma forma de contato */}
        <Text style={styles.h2}>Dúvidas ou Reservas?</Text>
        <TouchableOpacity
          onPress={() => Linking.openURL(`tel:${data.contato_reservas}`)}
        >
          <View style={styles.infoContainer}>
            <Icon name="phone" color="black" style={{ marginRight: 4 }} />
            <Text style={styles.jsonText}>{data.contato_reservas}</Text>
          </View>
        </TouchableOpacity>

        <Text style={styles.h2}>Acompanhe nas redes sociais!</Text>
        <View style={styles.socialContainer}>
          <SocialIcon
            type="instagram"
            style={{ backgroundColor: "black" }}
            onPress={() => openInstaApp(data["redes_sociais"].instagram)}
          />
          <SocialIcon
            type="twitter"
            style={{ backgroundColor: "black" }}
            onPress={() => openTwitterApp(data["redes_sociais"].twitter)}
          />
        </View>
        {/* </View> */}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  containerScroll: {
    paddingTop: 0,
    paddingLeft: 12,
    paddingRight: 12,
    marginTop: -10,
  },
  image: {
    width: "100%",
    height: 300,
    borderRadius: 5,
  },
  atracaoTitle: {
    fontSize: 28,
    fontWeight: "bold",
    marginVertical: 10,
  },
  socialContainer: {
    flexDirection: "row",
    justifyContent: "space-around",
    width: "50%",
    marginLeft: "auto",
    marginRight: "auto",
    marginBottom: 20,
  },
  ticketButton: {
    width: "100%",
    borderRadius: 10,
    backgroundColor: "#e91e63",
    marginVertical: 10,
  },
  ticketButtonText: {
    padding: 10,
  },
  h2: {
    fontSize: 20,
    fontWeight: "bold",
    marginVertical: 10,
    paddingTop: 16,
    color: "#e91e63",
  },
  jsonText: {
    fontSize: 16,
    // justify
  },
  infoContainer: {
    flexDirection: "row",
    alignItems: "center",
    paddingTop: 2,
    paddingBottom: 2,
  },
  smallText: {
    fontSize: 12,
    color: "gray",
    marginBottom: 10,
  },
  heartContainer: {
    position: "absolute",
    top: 10,
    right: 10,
    zIndex: 10,
  },
});

export default AtracoesDetailsScreen;
