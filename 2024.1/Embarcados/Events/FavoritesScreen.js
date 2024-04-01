import React, { useState, useEffect } from "react";
import {
  View,
  Text,
  FlatList,
  Button,
  StyleSheet,
  Image,
  TouchableOpacity,
} from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { SafeAreaView } from "react-native-safe-area-context";

// precisei para garantir que o componente seja atualizado sempre que o usuario vir para essa tela
import { useFocusEffect } from "@react-navigation/native";

function FavoriteScreen({ navigation }) {
  const [favoriteItems, setFavoriteItems] = useState([]);

  const loadFavoriteItems = async () => {
    try {
      const favoriteData = await AsyncStorage.getItem("favoriteAtracoes");
      if (favoriteData) {
        const parsedFavoriteData = JSON.parse(favoriteData);
        const favoriteArray = Object.values(parsedFavoriteData);
        setFavoriteItems(favoriteArray);
      }
    } catch (error) {
      console.error(error);
    }
  };

  useFocusEffect(
    React.useCallback(() => {
      loadFavoriteItems();
    }, [])
  );

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
    const endereco = local.split(",")[0];
    return endereco;
  }

  const renderItem = ({ item }) => (
    <TouchableOpacity
      onPress={() =>
        navigation.navigate("AtracoesDetailsScreen", {
          data: item,
        })
      }
    >
      <View
        style={{
          padding: 10,
          paddingTop: 0,
          paddingBottom: 20,
          flexDirection: "row",
        }}
      >
        <Image
          source={{
            uri: `${item.imagens}`,
          }}
          style={styles.image}
          resizeMode="cover"
        />
        <View style={styles.infoContainer}>
          <Text style={styles.infoNome}>{item.nome_atracao}</Text>
          <Text style={styles.infoEndereco}>{formatLocal(item.endereco)}</Text>
          <View style={styles.infoHorario}>
            <Text style={styles.infoText}>
              {formatTime(item.horario_inicio)}
            </Text>
          </View>
        </View>
      </View>
    </TouchableOpacity>
  );

  return (
    <SafeAreaView style={{ flex: 1 }}>
      <View>
        {favoriteItems.length > 0 ? (
          <FlatList
            data={favoriteItems}
            renderItem={renderItem}
            keyExtractor={(item, index) => index.toString()}
          />
        ) : (
          <View>
            <Text style={{ textAlign: "center", fontSize: 16 }}>
              Nenhum atração favoritada até o momento... :(
            </Text>
            <Text style={{ textAlign: "center", fontSize: 16 }}>
              Não deixe de conferir nossos eventos!
            </Text>
          </View>
        )}
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  image: {
    width: "35%",
    height: 110,
    borderRadius: 4,
    marginRight: 10,
  },
  infoContainer: {
    flex: 1,
    flexDirection: "column",
  },
  infoNome: {
    fontSize: 16,
    fontWeight: "bold",
    flexWrap: "wrap",
  },
  infoEndereco: {
    fontSize: 14,
    color: "#666",
  },
  infoHorario: {
    position: "absolute",
    bottom: 0,
    left: 0,
    paddingTop: 10,
  },
  infoText: {
    fontSize: 14,
    color: "#666",
    marginRight: "auto",
  },
});
export default FavoriteScreen;
