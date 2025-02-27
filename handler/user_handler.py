from flask import blueprints, jsonify
from flask_pydantic import validate
from repository.user_repository import UserRepository
from settings import get_db_session
from service.schema.user_schema import UserUpdateSchema
from service.user_service import UserService

user_blueprint = blueprints.Blueprint('user', __name__, url_prefix='/users')
user_repository = UserRepository(get_db_session())
user_service = UserService(user_repository)

@user_blueprint.route('/', methods=['GET'])
def get_all_users():
    response = user_service.get_all_users()
    if not response:
        return jsonify({"error": "User not found"}), 404

    users_data = [{"id": user.id, "name": user.name, "email": user.email} for user in response]
    return jsonify(users_data)

@user_blueprint.route('/<string:user_id>', methods=['GET'])
def get_users(user_id):
    response = user_service.get_user_by_id(user_id)
    if not response:
        return jsonify({"error": "User not found"}), 404

    user_data = {
        "id": response.id,
        "name": response.name
    }
    return jsonify(user_data)

@user_blueprint.route('/<string:user_id>', methods=['PATCH'])
@validate()
def patch_users(user_id, body: UserUpdateSchema):
    user = user_service.update_user(user_id, body)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"id": user.id, "name": user.name, "email": user.email})
