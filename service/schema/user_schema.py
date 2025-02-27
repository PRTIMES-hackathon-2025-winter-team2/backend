from pydantic import BaseModel, Field, EmailStr

class UserUpdateSchema(BaseModel):
    """ユーザー更新のリクエストスキーマ"""
    name: str = Field(None, min_length=1, max_length=200, description="ユーザー名")
    email: EmailStr = Field(None, description="メールアドレス")