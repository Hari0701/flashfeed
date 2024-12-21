from pygooglenews import GoogleNews

gn = GoogleNews(country="IN")

def fetch_news(query):
    """Fetch news articles based on a search query."""
    results = gn.search(query)
    return [
        {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
        }
        for entry in results['entries']
    ]

def fetch_top_news():
    """Fetch top news articles."""
    results = gn.top_news()
    return [
        {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
        }
        for entry in results['entries']
    ]
