import React, { useState } from "react";
import {
  SafeAreaView,
  View,
  Text,
  TouchableOpacity,
  FlatList,
  StyleSheet,
} from "react-native";
import BottomNavigation from "../Componets/ButtomNavigation";

const daysOfWeek = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do"];
const months = [
  "Enero",
  "Febrero",
  "Marzo",
  "Abril",
  "Mayo",
  "Junio",
  "Julio",
  "Agosto",
  "Septiembre",
  "Octubre",
  "Noviembre",
  "Diciembre",
];

const eventsData = [
  {
    id: "1",
    title: "Santa Teresa",
    location: "",
    color: "#E91E63",
    icon: "🎭",
  },
  {
    id: "2",
    title: "Feria gastronómica: Sabores de...",
    location: "Diriamba",
    color: "#2196F3",
    icon: "🍽️",
  },
  {
    id: "3",
    title: "Presentación cultural del Ballet Fo...",
    location: "San Marcos",
    color: "#4CAF50",
    icon: "💃",
  },
];

export default function CalendarScreen({ route, navigation }) {
  const departmentName = route.params?.department?.name || "Calendario";
  const [currentMonth, setCurrentMonth] = useState(new Date().getMonth());
  const [selectedDate, setSelectedDate] = useState(new Date().getDate());

  const specialDates = { 10: "#4CAF50", 20: "#2196F3", 28: "#E91E63" };

  const generateCalendarDays = () => {
    const date = new Date(new Date().getFullYear(), currentMonth, 1);
    const daysInMonth = new Date(
      date.getFullYear(),
      date.getMonth() + 1,
      0
    ).getDate();
    const firstDayOfMonth = (date.getDay() + 6) % 7; // Lunes = 0

    const days = Array.from({ length: firstDayOfMonth }, (_, i) => ({
      key: `empty-${i}`,
    }));

    for (let day = 1; day <= daysInMonth; day++) {
      days.push({ key: `day-${day}`, day, specialColor: specialDates[day] });
    }
    return days;
  };

  const calendarDays = generateCalendarDays();

  const handleNavigation = (screen) => {
    if (screen === "home") navigation.navigate("Home");
  };

  const renderDay = ({ item }) => {
    if (item.empty) return <View style={styles.dayCell} />;

    const isSelected = item.day === selectedDate;
    const cellStyle = [
      styles.dayCell,
      item.specialColor && {
        backgroundColor: item.specialColor,
        borderRadius: 8,
      },
      isSelected && { backgroundColor: "#2196F3", borderRadius: 8 },
    ];
    const textStyle = [
      styles.dayText,
      (item.specialColor || isSelected) && styles.specialDayText,
    ];

    return (
      <TouchableOpacity
        style={cellStyle}
        onPress={() => setSelectedDate(item.day)}
      >
        <Text style={textStyle}>{item.day}</Text>
      </TouchableOpacity>
    );
  };

  const renderEvent = ({ item }) => (
    <TouchableOpacity
      style={[styles.eventCard, { backgroundColor: item.color }]}
      activeOpacity={0.8}
    >
      <Text style={styles.eventIcon}>{item.icon}</Text>
      <View style={styles.eventTextContainer}>
        <Text style={styles.eventTitle}>{item.title}</Text>
        {item.location && (
          <Text style={styles.eventLocation}>{item.location}</Text>
        )}
      </View>
    </TouchableOpacity>
  );

  return (
    <SafeAreaView style={styles.container}>
      <FlatList
        data={eventsData}
        renderItem={renderEvent}
        keyExtractor={(item) => item.id}
        ListHeaderComponent={() => (
          <View style={{ paddingHorizontal: 20 }}>
            <Text style={styles.title}>{departmentName}</Text>
            <View style={styles.calendarContainer}>
              <View style={styles.monthHeader}>
                <Text style={styles.monthText}>{months[currentMonth]}</Text>
              </View>
              <View style={styles.weekDaysContainer}>
                {daysOfWeek.map((day) => (
                  <Text key={day} style={styles.weekDay}>
                    {day}
                  </Text>
                ))}
              </View>
              <FlatList
                data={calendarDays}
                renderItem={renderDay}
                keyExtractor={(item) => item.key}
                numColumns={7}
              />
            </View>
            <Text style={styles.selectedDateText}>
              Eventos para el {selectedDate} de{" "}
              {months[currentMonth].toLowerCase()}
            </Text>
          </View>
        )}
        contentContainerStyle={{ paddingBottom: 100 }}
      />
      <BottomNavigation onNavigate={handleNavigation} activeTab="calendar" />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F5F5F5",
  },
  title: {
    fontSize: 32,
    fontWeight: "bold",
    color: "#333",
    marginBottom: 30,
    paddingTop: 20,
  },
  calendarContainer: {
    backgroundColor: "white",
    borderRadius: 20,

    padding: 20,
    marginBottom: 20,
    elevation: 2,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
  },
  monthHeader: { alignItems: "center", marginBottom: 20 },
  monthText: {
    fontSize: 16,
    fontWeight: "600",
    color: "#2196F3",
    backgroundColor: "#E3F2FD",
    paddingHorizontal: 16,
    paddingVertical: 6,
    borderRadius: 12,
  },
  weekDaysContainer: {
    flexDirection: "row",
    justifyContent: "space-around",
    marginBottom: 10,
  },
  weekDay: {
    fontSize: 12,
    fontWeight: "600",
    color: "#666",
    width: 30,

    textAlign: "center",
  },
  dayCell: {
    width: "14.28%",
    aspectRatio: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  dayText: { fontSize: 16, color: "#333", fontWeight: "500" },
  specialDayText: { color: "white", fontWeight: "bold" },
  selectedDateText: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#333",
    marginBottom: 20,
    paddingHorizontal: 20,
  },
  eventCard: {
    flexDirection: "row",
    alignItems: "center",
    padding: 16,

    borderRadius: 16,
    marginBottom: 12,
    marginHorizontal: 20,
  },
  eventIcon: { fontSize: 24, marginRight: 12 },
  eventTextContainer: { flex: 1 },
  eventTitle: {
    fontSize: 16,
    fontWeight: "bold",
    color: "white",
    marginBottom: 2,
  },
  eventLocation: {
    position: "absolute",
    fontSize: 14,
    color: "rgba(255, 255, 255, 0.8)",
  },
});
