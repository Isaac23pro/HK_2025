import "react-native-gesture-handler";
import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";

import LoginScreen from "./Screens/LoginScreen";
import RegisterScreen from "./Screens/RegisterScreen";
import DepartmentSelectionScreen from "./Screens/DepartamentScreen";
import CalendarScreen from "./Screens/CalendarScreen";
import { ScrollView } from "react-native-gesture-handler";
import { View } from "react-native-web";
import HomeScreen from "./Screens/HomeScreen";
import LibraryScreen from "./Screens/LibraryScreen";

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Login"
        screenOptions={{
          contentStyle: {
            flex: 1,
          },
        }}
      >
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="Register"
          component={RegisterScreen}
          options={{ title: "Registro" }}
        />
        <Stack.Screen
          name="Library"
          component={LibraryScreen}
          options={{ title: "Biblioteca" }}
        />
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: "Home" }}
        ></Stack.Screen>

        <Stack.Screen
          name="DepartamentSelection"
          component={DepartmentSelectionScreen}
          options={{ title: "Seleccionar Departamento" }}
        />

        <Stack.Screen
          name="Calendar"
          component={CalendarScreen}
          options={({ route }) => ({
            title: route.params?.department?.name || "Calendario",
          })}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
