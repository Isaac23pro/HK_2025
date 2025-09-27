import React from "react";
import {
  SafeAreaView,
  FlatList,
  Text,
  TouchableOpacity,
  View,
  Image,
  StyleSheet,
} from "react-native";
import BottomNavigation from "../Componets/ButtomNavigation";

import MapaCarazo from "../assets/MapaCarazo.png";
import MapaChinandega from "../assets/MapaChinandega.png";
import MapaGranada from "../assets/MapaGranada.png";
import MapaLeón from "../assets/MapaLeón.png";
import MapaMatagalpa from "../assets/MapaMatagalpa.png";
import MapaRivas from "../assets/MapaRivas.png";

const departments = [
  {
    id: "1",
    name: "Carazo",
    color: "#4A90E2",
    bgColor: "#E3F2FD",
    icon: MapaCarazo,
  },
  {
    id: "2",
    name: "Granada",
    color: "#F5A623",
    bgColor: "#FFF8E1",
    icon: MapaGranada,
  },
  {
    id: "3",
    name: "León",
    color: "#E91E63",
    bgColor: "#FCE4EC",
    icon: MapaLeón,
  },
  {
    id: "4",
    name: "Rivas",
    color: "#4CAF50",
    bgColor: "#E8F5E8",
    icon: MapaRivas,
  },
  {
    id: "5",
    name: "Chinandega",
    color: "#E91E63",
    bgColor: "#FCE4EC",
    icon: MapaChinandega,
  },
  {
    id: "6",
    name: "Matagalpa",
    color: "#2196F3",
    bgColor: "#E3F2FD",
    icon: MapaMatagalpa,
  },
  {
    id: "7",
    name: "Managua",
    color: "#00ff",
    bgColor: "#eeff00",
    icon: MapaCarazo,
  },
  {
    id: "8",
    name: "chonteles",
    color: "#00ff",
    bgColor: "#eeff00",
    icon: MapaCarazo,
  },
  {
    id: "9",
    name: "ocotal",
    color: "#00ff",
    bgColor: "#eeff00",
    icon: MapaCarazo,
  },
  {
    id: "10",
    name: "san juan",
    color: "#00ff",
    bgColor: "#eeff00",
    icon: MapaCarazo,
  },
  {
    id: "11",
    name: "san juan",
    color: "#00ff",
    bgColor: "#eeff00",
    icon: MapaCarazo,
  },
  {
    id: "12",
    name: "san juan",
    color: "#00ff",
    bgColor: "#eeff00",
    icon: MapaCarazo,
  },
  {
    id: "13",
    name: "san juan",
    color: "#00ff",
    bgColor: "#eeff00",
    icon: MapaCarazo,
  },
  {
    id: "14",
    name: "san juan",
    color: "#00ff",
    bgColor: "#eeff00",
    icon: MapaCarazo,
  },
  {
    id: "15",
    name: "san juan",
    color: "#00ff",
    bgColor: "#eeff00",
    icon: MapaCarazo,
  },
];

export default function DepartmentSelectionScreen({ navigation }) {
  const handleDepartmentPress = (department) => {
    navigation.navigate("Calendar", { department });
  };

  const handleNavigation = (screen) => {
    if (screen === "home") {
      navigation.navigate("Home");

      if (screen === "library") {
        navigation.navigate("Library");
      }
    }
  };

  const renderDepartmentCard = ({ item }) => (
    <TouchableOpacity
      style={[styles.departmentCard, { backgroundColor: item.bgColor }]}
      onPress={() => handleDepartmentPress(item)}
      activeOpacity={0.8}
    >
      <View style={styles.mapContainer}>
        <Image source={item.icon} style={styles.mapIcon} resizeMode="contain" />
      </View>
      <Text style={[styles.departmentName, { color: item.color }]}>
        {item.name}
      </Text>
    </TouchableOpacity>
  );

  return (
    <SafeAreaView style={styles.container}>
      <FlatList
        style={{ flex: 1 }}
        data={departments}
        renderItem={renderDepartmentCard}
        keyExtractor={(item) => item.id}
        numColumns={2}
        contentContainerStyle={styles.departmentsGrid}
        ListHeaderComponent={() => (
          <>
            <Text style={styles.title}>Calendario</Text>
            <Text style={styles.subtitle}>Elegir{"\n"}Departamento</Text>
          </>
        )}
      />

      <View style={styles.footerContainer}>
        <BottomNavigation onNavigate={handleNavigation} activeTab="calendar" />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F5F5F5",
  },
  departmentsGrid: {
    paddingHorizontal: 15,
    paddingTop: 30,
    paddingBottom: 30,
    position: "absolute",
    margin: 7,
  },

  title: {
    fontSize: 32,
    fontWeight: "bold",
    color: "#333",
    marginBottom: 8,
    paddingHorizontal: 5,
  },
  subtitle: {
    fontSize: 18,
    color: "#666",
    marginBottom: 40,
    lineHeight: 24,
    paddingHorizontal: 5,
  },
  departmentCard: {
    flex: 1,

    aspectRatio: 1,
    borderRadius: 20,
    padding: 20,
    margin: 5,
    justifyContent: "space-between",
    alignItems: "center",
    elevation: 2,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  mapContainer: {
    width: 80,
    height: 80,
    borderRadius: 15,
    backgroundColor: "rgba(255, 255, 255, 0.3)",
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 10,
  },
  mapIcon: { width: 60, height: 60 },
  departmentName: { fontSize: 18, fontWeight: "bold", textAlign: "center" },
  footerContainer: { paddingBottom: 10 },
});
