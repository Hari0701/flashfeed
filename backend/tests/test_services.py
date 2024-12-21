from app.services import fetch_news, fetch_top_news

def test_fetch_news():
    results = fetch_news('Python')
    assert isinstance(results, list)
    assert len(results) > 0
    assert 'title' in results[0]
    assert 'link' in results[0]
    assert 'published' in results[0]

def test_fetch_top_news():
    results = fetch_top_news()
    assert isinstance(results, list)
    assert len(results) > 0
    assert 'title' in results[0]
    assert 'link' in results[0]
    assert 'published' in results[0]
