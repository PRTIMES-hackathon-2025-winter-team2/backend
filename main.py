from settings import app
from domain.tables import create_tables
from handler.auth_handler import auth

if __name__ == '__main__':
    create_tables()

    app.register_blueprint(auth)

    app.run(debug=True, host="0.0.0.0", port=5000)
