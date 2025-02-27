from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class TreeBase(BaseModel):
    """ツリーの基底スキーマ"""

    id: UUID = Field(..., description="ツリーID")
    title: str = Field(..., min_length=1, max_length=200, description="ツリー名")


class DreamBase(BaseModel):
    """夢の基底スキーマ"""

    id: Optional[UUID] = Field(None, description="夢ID")
    title: str = Field(..., min_length=1, max_length=200, description="タイトル")
    position: int = Field(..., description="位置")
    created_at: Optional[datetime] = Field(None, description="作成日時")
    ended_at: Optional[datetime] = Field(None, description="終了日時")


class TreeSchemaWithUserID(TreeBase):
    """ユーザーIDを含むツリーのスキーマ"""

    user_id: UUID = Field(..., description="ユーザーID")


class GetAllUsersTreesResponseSchema(BaseModel):
    """全ユーザーのツリー情報を取得するためのレスポンススキーマ"""

    trees: list[TreeSchemaWithUserID] = Field(..., description="ツリーのリスト")


class GetTreesResponseSchema(BaseModel):
    """ツリー情報を取得するためのレスポンススキーマ"""

    trees: list[TreeBase] = Field(..., description="ツリーのリスト")


class PostTreeRequestSchema(BaseModel):
    """ツリーを作成するためのリクエストスキーマ"""

    title: str = Field(..., min_length=1, max_length=200, description="ツリー名")
    dreams: list[DreamBase] = Field(..., description="夢のリスト")


class PostTreeResponseSchema(BaseModel):
    """ツリーを作成した後のレスポンススキーマ"""

    id: UUID = Field(..., description="ツリーID")


class GetTreeResponseSchema(BaseModel):
    """ツリー情報を取得するためのレスポンススキーマ"""

    id: UUID = Field(..., description="ツリーID")
    title: str = Field(..., min_length=1, max_length=200, description="ツリー名")
    dreams: list[DreamBase] = Field(..., description="夢のリスト")


class PatchTreeRequestSchema(BaseModel):
    """ツリーを更新するためのリクエストスキーマ"""

    name: str = Field(..., min_length=1, max_length=200, description="ツリー名")
    ended_at: datetime = Field(..., description="終了日時")
