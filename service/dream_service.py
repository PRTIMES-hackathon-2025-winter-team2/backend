from repository.dream_repository import DreamRepository
from uuid import UUID


class DreamService:
    def __init__(self, dream_repository: DreamRepository):
        self.dream_repository = dream_repository

    def update_ended_at(self, dream_id: str) -> None:
        """指定されたIDのDreamのended_atを更新する"""
        self.dream_repository.update_ended_at(dream_id)
        return None

    def get_dream_owner(self, dream_id: str) -> UUID:
        """指定されたIDのDreamのオーナーを取得する"""
        return self.dream_repository.get_dream_owner(dream_id)
