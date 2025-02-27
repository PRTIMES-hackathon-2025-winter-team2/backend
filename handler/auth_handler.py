from flask import blueprints, request, jsonify
from flask_pydantic import validate
from service.schema.auth_schema import UserRegisterSchema, UserLoginSchema, TokenResponseSchema
from service.auth_service import AuthService
from repository.user_repository import UserRepository
from settings import get_db_session

auth = blueprints.Blueprint('auth', __name__, url_prefix='/auth')
user_repository = UserRepository(get_db_session())
auth_service = AuthService(user_repository, 'secret_key')

@auth.route('/register', methods=['POST'])
@validate()
def register(body: UserRegisterSchema):
    response = auth_service.register(body)
    return jsonify(response.model_dump())

@auth.route('/login', methods=['POST'])
@validate()
def login(body: UserLoginSchema):
    response = auth_service.login(body)
    return jsonify(response.model_dump())

@auth.route('/reset_password', methods=['POST'])
def reset_password():
    auth_service.reset_password()
    return jsonify({'message': 'Reset password'})
