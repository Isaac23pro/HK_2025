// BottomNavigation.js - VERSIÓN RESPONSIVE
import {
  View,
  TouchableOpacity,
  Text,
  StyleSheet,
  Dimensions,
} from "react-native";

const { width: screenWidth } = Dimensions.get("window");

export default function BottomNavigation({ onNavigate, activeTab }) {
  const navItems = [
    { id: "home", icon: "🏠", label: "Inicio" },
    { id: "calendar", icon: "📅", label: "Calendario" },
    { id: "add", icon: "➕", label: "Agregar" },
    { id: "library", icon: "📚", label: "Biblioteca" },
    { id: "profile", icon: "👤", label: "Perfil" },
  ];

  // Tamaños responsive basados en el ancho de pantalla
  const isSmallScreen = screenWidth < 375; // iPhone SE y similares
  const isMediumScreen = screenWidth >= 375 && screenWidth < 414;

  return (
    <View style={styles.container}>
      <View
        style={[
          styles.navBar,
          isSmallScreen && styles.navBarSmall,
          isMediumScreen && styles.navBarMedium,
        ]}
      >
        {navItems.map((item) => (
          <TouchableOpacity
            key={item.id}
            style={[
              styles.navItem,
              isSmallScreen && styles.navItemSmall,
              isMediumScreen && styles.navItemMedium,
              activeTab === item.id && styles.activeNavItem,
            ]}
            onPress={() => onNavigate(item.id)}
            activeOpacity={0.7}
          >
            <Text
              style={[
                styles.navIcon,
                isSmallScreen && styles.navIconSmall,
                isMediumScreen && styles.navIconMedium,
                activeTab === item.id && styles.activeNavIcon,
              ]}
            >
              {item.icon}
            </Text>
            {!isSmallScreen && ( // Oculta labels en pantallas muy pequeñas
              <Text
                style={[
                  styles.navLabel,
                  isSmallScreen && styles.navLabelSmall,
                  isMediumScreen && styles.navLabelMedium,
                ]}
              >
                {item.label}
              </Text>
            )}
          </TouchableOpacity>
        ))}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "transparent",
    paddingHorizontal: screenWidth < 375 ? 10 : 20, // Responsive padding
    paddingVertical: 8,
  },
  navBar: {
    flexDirection: "row",
    backgroundColor: "white",
    borderRadius: 25,
    paddingVertical: 12,
    paddingHorizontal: 8,
    justifyContent: "space-around",
    alignItems: "center",
    elevation: 8,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.15,
    shadowRadius: 8,
    minHeight: 60,
  },
  navBarSmall: {
    borderRadius: 20,
    paddingVertical: 8,
    paddingHorizontal: 4,
    minHeight: 50,
  },
  navBarMedium: {
    borderRadius: 22,
    paddingVertical: 10,
    paddingHorizontal: 6,
    minHeight: 55,
  },
  navItem: {
    padding: 8,
    borderRadius: 20,
    alignItems: "center",
    flex: 1,
  },
  navItemSmall: {
    padding: 4,
    borderRadius: 15,
  },
  navItemMedium: {
    padding: 6,
    borderRadius: 18,
  },
  navIcon: {
    fontSize: 20,
  },
  navIconSmall: {
    fontSize: 16,
  },
  navIconMedium: {
    fontSize: 18,
  },
  activeNavIcon: {
    fontSize: 22,
  },
  navLabel: {
    fontSize: 10,
    marginTop: 2,
    color: "#666",
    textAlign: "center",
  },
  navLabelSmall: {
    fontSize: 8,
  },
  navLabelMedium: {
    fontSize: 9,
  },
  activeNavItem: {
    backgroundColor: "#E3F2FD",
  },
});
