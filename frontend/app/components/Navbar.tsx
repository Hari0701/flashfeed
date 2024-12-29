import React from "react";
import { View, Text, StyleSheet } from "react-native";

const Navbar = () => {
  return (
    <View style={styles.navbar}>
      <Text style={styles.title}>FlashFeed</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  navbar: {
    height: 60,
    backgroundColor: "#6200EE",
    justifyContent: "center",
    alignItems: "center",
  },
  title: {
    color: "#FFFFFF",
    fontSize: 20,
    fontWeight: "bold",
  },
});

export default Navbar;