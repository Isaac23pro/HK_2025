import React, { useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  Image,
  Alert,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
  StatusBar,
} from "react-native";
import { Ionicons } from "@expo/vector-icons";
import { LinearGradient } from "expo-linear-gradient";

// Make sure you have a logo image named 'MemoriaVivaNicaragua.png' in your assets folder
import logo from "../assets/MVLOGO.png";

export default function LoginScreen({ navigation }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const handleLogin = () => {
    // conectar con la APi para obtener los usuarios
    if (email === "William.com" && password === "123") {
      Alert.alert("Éxito", "Inicio de sesión exitoso");
    } else {
      Alert.alert("Error", "Correo o contraseña incorrectos");
    }
  };

  return (
    <KeyboardAvoidingView
      behavior={Platform.OS === "ios" ? "padding" : "height"}
      style={styles.container}
    >
      <StatusBar barStyle="light-content" />
      <LinearGradient
        colors={["#FFB041", "#FF6B6B"]}
        style={styles.topGradient}
      />
      <LinearGradient
        colors={["#FF6B6B", "#F83600"]}
        style={styles.bottomGradient}
      />

      <ScrollView contentContainerStyle={styles.scrollContainer}>
        <View style={styles.logoContainer}>
          <Image source={logo} style={styles.logo} />
        </View>

        {/* Login Form Card */}
        <View style={styles.loginCard}>
          <Text style={styles.welcomeText}>Bienvenido</Text>
          <Text style={styles.subtitle}>Inicie sesión para continuar</Text>

          {/* User Input */}
          <View style={styles.inputContainer}>
            <TextInput
              style={styles.input}
              placeholder="Usuario"
              placeholderTextColor="#888"
              value={email}
              onChangeText={setEmail}
              keyboardType="email-address"
              autoCapitalize="none"
            />
          </View>

          {/* Password Input */}
          <View style={styles.inputContainer}>
            <TextInput
              style={styles.input}
              placeholder="Contraseña"
              placeholderTextColor="#888"
              value={password}
              onChangeText={setPassword}
              secureTextEntry={!showPassword}
            />
          </View>

          <TouchableOpacity
            style={styles.loginButton}
            onPress={() => navigation.navigate("DepartamentSelection")}
          >
            <Text style={styles.loginButtonText}>Iniciar</Text>
          </TouchableOpacity>

          <View style={styles.registerContainer}>
            <Text style={styles.registerText}>¿No tienes una cuenta? </Text>
            <TouchableOpacity onPress={() => navigation.navigate("Register")}>
              <Text style={styles.registerLink}>Regístrate</Text>
            </TouchableOpacity>
          </View>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContainer: {
    flexGrow: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  topGradient: {
    top: 0,
    position: "absolute",
    left: 0,
    right: 0,
    height: "40%",
    borderBottomLeftRadius: 50,
    borderBottomRightRadius: 50,
  },
  bottomGradient: {
    bottom: 0,
    position: "absolute",
    left: 0,
    right: 0,
    height: "40%",
    borderTopLeftRadius: 50,
    borderTopRightRadius: 50,
  },
  logoContainer: {
    marginBottom: 50,
    alignSelf: "center",
    position: "absolute",
    top: 50,
  },
  logo: {
    width: 200,
    height: 150,
    resizeMode: "contain",
  },
  loginCard: {
    backgroundColor: "white",
    width: "90%",
    padding: 25,
    borderRadius: 20,
    alignItems: "center",
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 10,
    elevation: 5,
    marginTop: 150,
  },
  welcomeText: {
    fontSize: 28,
    fontWeight: "bold",
    color: "#333",
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: "#666",
    marginBottom: 20,
  },
  inputContainer: {
    backgroundColor: "#f0f0f0",
    borderRadius: 30,
    width: "100%",
    height: 50,
    paddingHorizontal: 20,
    marginBottom: 15,
    justifyContent: "center",
  },
  input: {
    fontSize: 16,
    color: "#333",
  },
  loginButton: {
    backgroundColor: "#007BFF",
    borderRadius: 30,
    height: 50,
    width: "100%",
    justifyContent: "center",
    alignItems: "center",
    marginTop: 20,
  },
  loginButtonText: {
    color: "white",
    fontSize: 18,
    fontWeight: "bold",
  },
  registerContainer: {
    flexDirection: "row",
    justifyContent: "center",
    marginTop: 20,
  },
  registerText: {
    color: "#666",
    fontSize: 15,
  },
  registerLink: {
    color: "#007BFF",
    fontWeight: "bold",
    fontSize: 15,
  },
});
