from pygooglenews import GoogleNews 
from newspaper import Article
from googlenewsdecoder import new_decoderv1
import requests

# Initialize the Google News object
gn = GoogleNews()

def fetch_news(query):
    """Fetch news articles based on a search query and summarize them."""
    results = gn.search(query)
    return process_entries(results)

def fetch_top_news():
    """Fetch top news articles and summarize them."""
    results = gn.top_news()
    return process_entries(results)

def fetch_news_by_category(category):
    """
    Fetch news articles based on a specific category 
    (e.g., technology, business, sports) and summarize them.
    """
    results = gn.topic_headlines(category)
    return process_entries(results)

def process_entries(results):
    """Helper function to process and summarize news entries."""
    articles = []
    for entry in results['entries']:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
        }
        # Fetch and summarize the article content
        content = process_article(entry.link)
        article['summary'] = content if content else "Content could not be retrieved or summarized."
        articles.append(article)
    return articles

def fetch_article_content(url):
    """
    Fetch and extract article content by decoding the Google News URL
    and retrieving the actual article content using Newspaper3k.
    """
    try:
        # Decode the Google News URL
        decoded_url_info = new_decoderv1(url, interval=5)  # Adjust interval if needed

        if not decoded_url_info.get("status"):
            print(f"Error decoding URL: {decoded_url_info.get('message', 'Unknown error')}")
            return None

        decoded_url = decoded_url_info["decoded_url"]
        # Fetch content using custom headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(decoded_url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse content with Newspaper3k
        article = Article(decoded_url)
        article.set_html(response.text)
        article.parse()

        return article.text  # Return the full article text
    except Exception as e:
        print(f"Error occurred while fetching article content for {url}: {e}")
        return None

def process_article(url):
    """
    Fetch and process the content of an article.
    """
    article_content = fetch_article_content(url)
    if article_content:
        return article_content[:300] + "..."  # Return a trimmed summary
    return None
