from pygooglenews import GoogleNews
from newspaper import Article
from googlenewsdecoder import new_decoderv1  # Ensure this library is installed

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
        content = fetch_article_content(entry.link)
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
        content = fetch_article_content(entry.link)
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
        article = Article(decoded_url_info["decoded_url"])
        article.download()
        article.parse()

        # Return the article's content (text)
        return article.text

    except Exception as e:
        print(f"Error occurred while fetching article content: {e}")
        return None
