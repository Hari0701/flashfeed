from pygooglenews import GoogleNews
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

gn = GoogleNews()

def fetch_news(query):
    """Fetch news articles based on a search query and summarize them."""
    results = gn.search(query)
    articles = []
    for entry in results['entries']:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
        }
        content = fetch_article_content(entry.link)
        if content:
            article['summary'] = summarize_content(content)
        articles.append(article)
    return articles

def fetch_top_news():
    """Fetch top news articles and summarize them."""
    results = gn.top_news()
    articles = []
    for entry in results['entries']:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
        }
        content = fetch_article_content(entry.link)
        if content:
            article['summary'] = summarize_content(content)
        articles.append(article)
    return articles

def fetch_article_content(url):
    """
    Fetch the main content of an article from a URL.
    Returns plain text content of the article.
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract content inside <p> tags
            paragraphs = soup.find_all('p')
            content = ' '.join([para.get_text() for para in paragraphs])
            return content.strip()
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
    return None

def summarize_content(content):
    """
    Summarize the content using NLTK's sentence tokenizer.
    Returns the first 5 sentences as a simple summary.
    """
    try:
        sentences = sent_tokenize(content)
        summary = ' '.join(sentences[:5])  # Adjust number of sentences for the summary
        return summary
    except Exception as e:
        print(f"Error summarizing content: {e}")
    return "Summary not available."
