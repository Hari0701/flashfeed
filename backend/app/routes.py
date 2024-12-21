from flask import Blueprint, request, jsonify
from app.services import fetch_news, fetch_top_news

routes = Blueprint('routes', __name__)

@routes.route('/search', methods=['GET'])
def search_news():
    query = request.args.get('q')
    if not query:
        return jsonify({'error': 'Missing query parameter "q"'}), 400

    news = fetch_news(query)
    return jsonify(news)

@routes.route('/top-news', methods=['GET'])
def top_news():
    news = fetch_top_news()
    return jsonify(news)
