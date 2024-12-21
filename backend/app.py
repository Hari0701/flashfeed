from app import create_app
from app.config import PORT, HOST, DEBUG

app = create_app()

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
