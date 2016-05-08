from app.settings import DEBUG, SERVER_HOST, SERVER_PORT
from app import app

if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=DEBUG)
