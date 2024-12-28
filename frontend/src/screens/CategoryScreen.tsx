import React, { useState, useEffect } from "react";
import { View, ScrollView, StyleSheet } from "react-native";
import Navbar from "../components/Navbar";
import CategoryTags from "../components/CategoryTags";
import NewsArticle from "../components/NewsArticle";
import { fetchNewsByCategory } from "../services/api";

const CategoryScreen = () => {
  const [articles, setArticles] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState("Technology");

  useEffect(() => {
    fetchNewsByCategory(selectedCategory).then(setArticles);
  }, [selectedCategory]);

  return (
    <View style={styles.container}>
      <Navbar />
      <CategoryTags onSelectCategory={setSelectedCategory} />
      <ScrollView>
        {articles.map((article, index) => (
          <NewsArticle key={index} article={article} />
        ))}
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});

export default CategoryScreen;
