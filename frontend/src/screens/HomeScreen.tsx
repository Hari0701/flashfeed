import React, { useState, useEffect } from "react";
import { View, ScrollView, StyleSheet } from "react-native";
import Navbar from "../components/Navbar";
import NewsArticle from "../components/NewsArticle";
import { fetchTopNews } from "../services/api";

const HomeScreen = () => {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    fetchTopNews().then(setArticles);
  }, []);

  return (
    <View style={styles.container}>
      <Navbar />
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

export default HomeScreen;
