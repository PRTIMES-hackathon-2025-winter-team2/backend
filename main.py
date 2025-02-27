from settings import app
from domain.tables import create_tables
from handler.auth_handler import auth
from handler.user_handler import user
from handler.follow_handler import follow


if __name__ == '__main__':
    create_tables()

    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(follow)

    app.run(debug=True, host="0.0.0.0", port=5000)
