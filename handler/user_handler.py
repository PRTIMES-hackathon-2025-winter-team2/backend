from flask import blueprints, request, jsonify
from flask_pydantic import validate
from service.schema.auth_schema import UserRegisterSchema, UserLoginSchema, TokenResponseSchema
from service.auth_service import AuthService
from repository.user_repository import UserRepository
from settings import get_db_session
from service.schema.user_schema import UserUpdateSchema


user = blueprints.Blueprint('user', __name__, url_prefix='/users')
user_repository = UserRepository(get_db_session())

@user.route('/<string:id>', methods=['GET'])
def get_users(id):
    response = user_repository.find_by_id(id)
    if not response:
        return jsonify({"error": "User not found"}), 404
    
    user_data = {
        "id": str(response.id),
        "name": response.name,
        "email": response.email,
        "created_at": response.created_at.isoformat(),
        "updated_at": response.updated_at.isoformat(),
    }

    return jsonify(user_data)