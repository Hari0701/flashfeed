import axios from "axios";

const API_URL = "http://127.0.0.1:5000";

export const fetchTopNews = async () => {
  const response = await axios.get(`${API_URL}/top-news`);
  return response.data.articles;
};

export const fetchNewsByCategory = async (category: string) => {
  const response = await axios.get(`${API_URL}/category-news`, { params: { category } });
  return response.data.articles;
};

export const fetchArticles = async () => {
  try {
    const response = await fetch("https://api.example.com/articles");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    return data.articles;
  } catch (error) {
    console.error("Error fetching articles:", error);
    throw error;
  }
};

export const fetchArticlesByCategory = async (category: string) => {
  try {
    const response = await fetch(`https://api.example.com/articles?category=${category}`);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    return data.articles;
  } catch (error) {
    console.error(`Error fetching articles for category ${category}:`, error);
    throw error;
  }
};
