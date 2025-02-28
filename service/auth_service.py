from datetime import datetime

from flask_jwt_extended import create_access_token, decode_token

from domain.user import User
from repository.user_repository import UserRepository
from service.schema.auth_schema import (
    TokenResponseSchema,
    UserLoginSchema,
    UserRegisterSchema,
)


class AuthService:
    def __init__(self, user_repository: UserRepository, secret_key: str):
        self.user_repository = user_repository
        self.secret_key = secret_key

    def register(self, user: UserRegisterSchema) -> TokenResponseSchema:
        user = User(
            name=user.username,
            email=user.email,
            password=user.password,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        current_user = self.user_repository.find_by_email(user.email)
        if current_user is not None:
            raise ValueError("User already exists")

        created_user = self.user_repository.create(user)
        return TokenResponseSchema(
            token=create_access_token(identity=str(created_user.id)),
            user_id=str(created_user.id),
        )

    def login(self, request: UserLoginSchema) -> TokenResponseSchema:
        user = self.user_repository.find_by_email(request.email)
        if user is None:
            raise ValueError("User not found")
        if not self.user_repository.compare_password(request.email, request.password):
            raise ValueError("Password is incorrect")
        return TokenResponseSchema(
            token=create_access_token(identity=str(user.id)),
            user_id=str(user.id),
        )

    def decode_token(token: str) -> str:
        decoded_token = decode_token(token)
        return decoded_token["sub"]

    def reset_password(self):
        # サービスのコアロジックではないので一旦、未実装
        pass
