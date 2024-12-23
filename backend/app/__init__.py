from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow cross-origin requests (useful for connecting the frontend)

    # Register routes
    from app.routes import routes
    app.register_blueprint(routes)

    return app
