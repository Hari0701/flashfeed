import React from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

const categories = ["Technology", "Sports", "Health", "Business", "Entertainment"];

interface CategoryTagsProps {
  onSelectCategory: (category: string) => void;
}

const CategoryTags: React.FC<CategoryTagsProps> = ({ onSelectCategory }) => {
  return (
    <View style={styles.container}>
      {categories.map((category) => (
        <TouchableOpacity key={category} style={styles.tag} onPress={() => onSelectCategory(category)}>
          <Text style={styles.tagText}>{category}</Text>
        </TouchableOpacity>
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "center",
    marginVertical: 10,
  },
  tag: {
    backgroundColor: "#E0E0E0",
    borderRadius: 20,
    paddingVertical: 5,
    paddingHorizontal: 15,
    margin: 5,
  },
  tagText: {
    color: "#000",
  },
});

export default CategoryTags;
