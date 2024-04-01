import * as React from "react";
import { View, Text, TouchableOpacity, Image, ScrollView } from "react-native";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import SplashScreen from "./SplashScreen";
import AtracoesScreen from "./AtracoesScreen";
import AtracoesDetailsScreen from "./AtracoesDetailsScreen";
import FavoritesScreen from "./FavoritesScreen";
// react-native-vector-icons/Ionicons otherwise.
import Ionicons from "react-native-vector-icons/Ionicons";
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

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

function App() {
  let [fontsLoaded] = useFonts({
    LibreBaskerville_400Regular,
    SourceSansPro_400Regular_Italic,
    SourceSansPro_700Bold,
  });

  if (!fontsLoaded) {
    return <Text>Carregando fontes...</Text>;
  }

  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Splash" component={SplashScreen} />
        <Stack.Screen
          name="BottomNavBar"
          component={BottomNavBar}
          options={{ animationEnabled: false }}
        />
        <Stack.Screen
          name="AtracoesDetailsScreen"
          component={AtracoesDetailsScreen}
          // quero que essa tela tenha o header
          options={{ headerShown: true, title: "Detalhes" }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

function BottomNavBar() {
  return (
    <>
      <Tab.Navigator
        // seguindo o tutorial do react-navigation oficial
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            if (route.name === "Atrações") {
              iconName = focused ? "home" : "home-outline";
            } else if (route.name === "Favoritos") {
              iconName = focused ? "heart" : "heart-outline";
            }

            return <Ionicons name={iconName} size={size} color={color} />;
          },
          headerShown: false, // esconde o header
          tabBarActiveTintColor: "#e91e63",
          tabBarStyle: {
            backgroundColor: "white",
            padding: 4,
            paddingBottom: 8,
            height: 60,
          },
        })}
      >
        {/* essa tela é renderizada por default, em ordem de "aparecimento" no código */}
        <Tab.Screen
          name="Atrações"
          component={AtracoesScreen}
          options={{ tabBarBadge: "+6" }}
        />
        <Tab.Screen
          name="Favoritos"
          component={FavoritesScreen}
          options={{ headerShown: true }}
        />
        {/* <Tab.Screen name="Splash" component={SplashScreen} />   usado para testar mais facilmente a splashscreen 
      sem precisar reiniciar o aplicativo */}
      </Tab.Navigator>
    </>
  );
}

export default App;
