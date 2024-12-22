from pygooglenews import GoogleNews
from newspaper import Article
from googlenewsdecoder import new_decoderv1  # Ensure this library is installed
import requests
# Initialize the Google News object
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
        # Fetch and summarize the article content
        content = process_article(entry.link)
        if content:
            article['summary'] = content
        else:
            article['summary'] = "Content could not be retrieved or summarized."
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
        # Fetch and summarize the article content
        content = process_article(entry.link)
        if content:

            article['summary'] = content
        else:
            article['summary'] = "Content could not be retrieved or summarized."
        articles.append(article)
    return articles

def fetch_article_content(url):
    """
    Fetch and extract article content by decoding the Google News URL
    and then retrieving the actual article content using Newspaper3k.
    If an error occurs, move to the next article without stopping the process.
    """
    try:
        # Step 1: Decode the Google News URL
        interval_time = 5  # You can adjust the interval time if needed
        decoded_url_info = new_decoderv1(url, interval=interval_time)
        print(decoded_url_info)
        
        # Check if the decoding was successful
        if decoded_url_info.get("status"):
            print("Decoded URL:", decoded_url_info["decoded_url"])
        else:
            print(f"Error decoding URL: {decoded_url_info.get('message', 'Unknown error')}")
            return None

        # Step 2: Fetch and parse the article content using Newspaper3k
        decoded_url = decoded_url_info["decoded_url"]
        
        # Define custom headers (to mimic a normal browser request)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

        # Use requests to download the page
        response = requests.get(decoded_url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Use Newspaper3k to parse the content
        article = Article(decoded_url)
        article.set_html(response.text)  # Set the content manually
        article.parse()

        # Return the article's content (text)
        return article.text

    except Exception as e:
        print(f"Error occurred while fetching article content for {url}: {e}")
        return None

def process_article(url):
    """
    Process a list of URLs, fetch content for each article, 
    and skip to the next if an error occurs.
    """
    article_content = fetch_article_content(url)
        
    if article_content:
        print("Successfully fetched article content!")
            # Do something with the article content (e.g., save it, process it further)
    else:
        print("Failed to fetch article content, moving to the next URL.")