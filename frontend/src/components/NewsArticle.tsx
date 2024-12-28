import React from "react";
import { View, Text, StyleSheet, Image } from "react-native";

interface NewsArticleProps {
  article: {
    title: string;
    description: string;
    author: string;
    publishedAt: string;
    imageUrl: string;
  };
}

const NewsArticle: React.FC<NewsArticleProps> = ({ article }) => {
  return (
    <View style={styles.container}>
      <Image source={{ uri: article.imageUrl }} style={styles.image} />
      <Text style={styles.title}>{article.title}</Text>
      <Text style={styles.description}>{article.description}</Text>
      <Text style={styles.author}>By {article.author}</Text>
      <Text style={styles.date}>{new Date(article.publishedAt).toLocaleDateString()}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    margin: 10,
    padding: 10,
    backgroundColor: "#FFF",
    borderRadius: 10,
    shadowColor: "#000",
    shadowOpacity: 0.1,
    shadowRadius: 10,
    elevation: 5,
  },
  image: {
    width: "100%",
    height: 200,
    borderRadius: 10,
  },
  title: {
    fontSize: 18,
    fontWeight: "bold",
    marginVertical: 10,
  },
  description: {
    fontSize: 14,
    color: "#666",
  },
  author: {
    fontSize: 12,
    color: "#555",
  },
  date: {
    fontSize: 12,
    color: "#999",
  },
});

export default NewsArticle;
