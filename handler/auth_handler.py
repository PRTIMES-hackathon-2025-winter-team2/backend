from flask import blueprints, request, jsonify
from flask_pydantic import validate
from service.schema.auth_schema import UserRegisterSchema, UserLoginSchema, TokenResponseSchema
from service.auth_service import AuthService
from repository.user_repository import UserRepository
from settings import get_db_session
from flask_jwt_extended import set_access_cookies

auth = blueprints.Blueprint('auth', __name__, url_prefix='/auth')
user_repository = UserRepository(get_db_session())
auth_service = AuthService(user_repository, 'secret_key')

@auth.route('/register', methods=['POST'])
@validate()
def register(body: UserRegisterSchema):
    r = auth_service.register(body)
    response = jsonify(r.model_dump())
    set_access_cookies(response, r.token)
    return response

@auth.route('/login', methods=['POST'])
@validate()
def login(body: UserLoginSchema):
    r = auth_service.login(body)
    response = jsonify(r.model_dump())
    set_access_cookies(response, r.token)
    return response

@auth.route('/reset_password', methods=['POST'])
def reset_password():
    auth_service.reset_password()
    return jsonify({'message': 'Reset password'})
