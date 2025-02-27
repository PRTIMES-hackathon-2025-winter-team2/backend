from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserUpdateSchema(BaseModel):
    """ユーザー更新のリクエストスキーマ"""

    name: Optional[str] = Field(
        None, min_length=1, max_length=200, description="ユーザー名"
    )
    email: Optional[EmailStr] = Field(None, description="メールアドレス")
