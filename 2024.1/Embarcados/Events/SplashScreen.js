import * as React from "react";
import { View, Text, Image, BackHandler, StyleSheet } from "react-native";
import {
  useFonts,
  LibreBaskerville_400Regular,
} from "@expo-google-fonts/libre-baskerville";
import {
  SourceSansPro_400Regular_Italic,
  SourceSansPro_700Bold,
} from "@expo-google-fonts/source-sans-pro";
import AsyncStorage from "@react-native-async-storage/async-storage";

import { Button } from "@rneui/themed";

function SplashScreen({ navigation }) {
  let [fontsLoaded] = useFonts({
    LibreBaskerville_400Regular,
    SourceSansPro_400Regular_Italic,
    SourceSansPro_700Bold,
  });

  if (!fontsLoaded) {
    return <Text>Carregando fontes...</Text>;
  }

  const handlePress = () => {
    // clearAsyncStorage(); botao de teste pra limpar o async storage
    navigation.replace("BottomNavBar");
  };

  const clearAsyncStorage = async () => {
    try {
      await AsyncStorage.clear();
      console.log("AsyncStorage limpo com sucesso.");
    } catch (error) {
      console.error("Erro ao limpar AsyncStorage:", error);
    }
  };

  return (
    <>
      <View style={styles.container}>
        <Image
          source={require("./splash.jpg")}
          style={styles.image}
          resizeMode="contain"
        />
        <Text
          style={[styles.text, { fontFamily: "LibreBaskerville_400Regular" }]}
        >
          Maratona <Text style={styles.fiction}>Ficticionalmente</Text> Cultural
        </Text>
      </View>
      <View style={styles.buttonDiv}>
        <Button
          buttonStyle={styles.button}
          titleStyle={styles.buttonText}
          title="Continuar"
          onPress={handlePress}
        />
      </View>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  image: {
    width: 200,
    height: 200,
  },
  text: {
    paddingTop: 20,
    fontSize: 30,
    marginVertical: 10,
    textAlign: "center",
  },
  fiction: {
    fontStyle: "italic",
    color: "#00000044",
  },
  buttonDiv: {
    position: "absolute",
    bottom: 150,
    width: "100%",
    alignItems: "center",
  },
  button: {
    width: 200,
    borderRadius: 10,
    border: "none",
    color: "red",
    backgroundColor: "black",
  },
  buttonText: {
    color: "white",
  },
});

export default SplashScreen;
