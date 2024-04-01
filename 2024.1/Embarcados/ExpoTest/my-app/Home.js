import * as React from "react";
import {
  View,
  Text,
  Image,
  Button,
  StyleSheet,
  BackHandler,
} from "react-native";

const atracoesData = require("./atracoes.json");

export default function HomeScreen({ navigation }) {
  <ScrollView style={styles.container}>
    <View>
      <FlatList
        data={atracoesData}
        renderItem={({ item }) => (
          <TouchableOpacity>
            <View>
              <Image
                style={{ width: 200, height: 100 }}
                source={{
                  uri: `${item.imagens}`,
                }}
              />
              <Text>{item.nome_atracao}</Text>
            </View>
          </TouchableOpacity>
        )}
      />
    </View>
  </ScrollView>;
}

const styles = StyleSheet.create({
  container: {
    alignItems: "center",
    justifyContent: "center",
    padding: 60,
  },
  logo: {
    height: 160,
    width: 160,
  },
  title: {
    padding: 30,
    fontSize: 18,
  },
  button: {
    padding: 15,
  },
});
