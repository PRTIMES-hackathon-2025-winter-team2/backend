from pydantic import BaseModel, Field, EmailStr

class UserRegisterSchema(BaseModel):
    """ユーザー登録のリクエストスキーマ"""
    name: str = Field(..., min_length=1, max_length=200, description="ユーザー名")
    email: EmailStr = Field(..., description="メールアドレス")
    password: str = Field(..., min_length=8, max_length=100, description="パスワード")


class UserLoginSchema(BaseModel):
    """ログインのリクエストスキーマ"""
    email: EmailStr = Field(..., description="メールアドレス")
    password: str = Field(..., description="パスワード")


class TokenResponseSchema(BaseModel):
    """ログインレスポンススキーマ"""
    token: str = Field(..., description="JWTトークン")
    user_id: str = Field(..., description="ユーザーID")
