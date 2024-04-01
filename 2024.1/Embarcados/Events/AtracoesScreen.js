import { Card, Divider } from "@rneui/base";
import * as React from "react";
import {
  View,
  Text,
  Image,
  Button,
  StyleSheet,
  BackHandler,
  TouchableOpacity,
  ScrollView,
  FlatList,
} from "react-native";

import {
  useFonts,
  LibreBaskerville_400Regular,
  LibreBaskerville_700Bold,
} from "@expo-google-fonts/libre-baskerville";

import {
  SourceSansPro_400Regular_Italic,
  SourceSansPro_700Bold,
  SourceSansPro_400Regular,
} from "@expo-google-fonts/source-sans-pro";

import AtracoesDetailsScreen from "./AtracoesDetailsScreen";
import FavoritesScreen from "./FavoritesScreen";
import { SafeAreaView } from "react-native-safe-area-context";

const atracoesData = require("./atracoes.json");

export default function AtracoesScreen({ navigation }) {
  function formatLocal(local) {
    const endereco = local.split(",")[0];
    return endereco;
  }

  function formatTime(time) {
    const date = new Date(time);
    const hours = date.getHours();
    const minutes = date.getMinutes();

    if (minutes < 10) {
      return `${hours}:0${minutes}`;
    }

    return `${hours}:${minutes}`;
  }

  let [fontsLoaded] = useFonts({
    LibreBaskerville_400Regular,
    SourceSansPro_400Regular_Italic,
    SourceSansPro_700Bold,
    LibreBaskerville_700Bold,
    SourceSansPro_400Regular,
  });

  return (
    <>
      <SafeAreaView style={styles.container}>
        <View style={styles.titleContainer}>
          <Text style={[styles.title]}>Atrações</Text>
          {/* //! PERGUNTAR COMO FAZER O TEXTO SCROLLAR JUNTO PRA CIMA
          
          //* sempre que eu scrollo ele fica fixo no topo, como se fosse um header */}
          {/* {console.log(atracoesData)} */}
          <View style={styles.subtitleContainer}>
            <Text style={styles.subtitle}>
              Confira as principais atrações do evento que vai agitar a Ilha da
              Magia!
            </Text>
          </View>
          <Divider style={{ backgroundColor: "black", width: "90%" }} />
        </View>
        <View>
          <FlatList
            showsVerticalScrollIndicator={false}
            data={atracoesData}
            renderItem={({ item }) => (
              <Card
                containerStyle={{
                  borderRadius: 10,
                  shadowColor: "#000",
                  shadowOffset: { width: 0, height: 2 },
                  shadowOpacity: 0.25,
                  shadowRadius: 3.84,
                  elevation: 2,
                }}
              >
                <TouchableOpacity
                  onPress={() =>
                    navigation.navigate("AtracoesDetailsScreen", {
                      data: item,
                    })
                  }
                >
                  <Card.Image
                    style={{ width: "100%", height: 200, borderRadius: 4 }}
                    source={{
                      uri: `${item.imagens}`,
                    }}
                  />
                  <Card.Title style={styles.nome_atracao}>
                    {item.nome_atracao}
                  </Card.Title>

                  <Text style={styles.infoAtracao}>
                    {formatLocal(item.endereco)} •{"  "}
                    {formatTime(item.horario_inicio)}h{" "}
                  </Text>
                </TouchableOpacity>
              </Card>
            )}
          />
        </View>
      </SafeAreaView>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    paddingBottom: 150,
  },
  titleContainer: {
    padding: 10,
    alignItems: "center",
    backgroundColor: "#fff",
    width: "100%",
  },
  title: {
    fontSize: 24,
    padding: 10,
    fontWeight: "bold",
    textAlign: "left",
  },
  button: {
    padding: 15,
  },
  subtitleContainer: {
    padding: 10,
    alignItems: "center",
    backgroundColor: "#fff",
    width: "90%",
  },
  subtitle: {
    fontSize: 16,
    textAlign: "justify",
  },
  nome_atracao: {
    fontSize: 20,
    marginVertical: 10,
    fontFamily: "LibreBaskerville_400Regular",
  },
  infoAtracao: {
    fontSize: 16,
    color: "#00000088",
  },
});
