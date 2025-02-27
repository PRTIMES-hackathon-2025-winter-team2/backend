from domain.tables import create_tables
from handler.auth_handler import auth_blueprint
from handler.dream_handler import user_tree_dream_blueprint
from handler.follow_handler import follow_blueprint
from handler.tree_handler import tree_blueprint, user_tree_blueprint
from handler.user_handler import user_blueprint
from settings import app

if __name__ == "__main__":
    create_tables()

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(user_tree_blueprint)
    app.register_blueprint(tree_blueprint)
    app.register_blueprint(follow_blueprint)
    app.register_blueprint(user_tree_dream_blueprint)

    app.run(debug=True, host="0.0.0.0", port=5000)
