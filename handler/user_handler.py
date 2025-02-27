from flask import blueprints, request, jsonify
from flask_pydantic import validate
from service.schema.auth_schema import UserRegisterSchema, UserLoginSchema, TokenResponseSchema
from service.auth_service import AuthService
from repository.user_repository import UserRepository
from settings import get_db_session
from service.schema.user_schema import UserUpdateSchema


user = blueprints.Blueprint('user', __name__, url_prefix='/users')
user_repository = UserRepository(get_db_session())

@user.route('/', methods=['GET'])
def get_all_users():
    response = user_repository.find_all()
    if not response:
        return jsonify({"error": "User not found"}), 404
    
    users_data = [user.to_dict() for user in response]
    return jsonify(users_data)

@user.route('/<string:id>', methods=['GET'])
def get_users(id):
    response = user_repository.find_by_id(id)
    if not response:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(response.to_dict())

@user.route('/<string:id>', methods=['PATCH'])
@validate()
def patch_users(id, body: UserUpdateSchema):
    user = user_repository.find_by_id(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if body.name:
        user.name = body.name
    if body.email:
        user.email = body.email

    user_repository.session.commit()
    return jsonify(user.to_dict())