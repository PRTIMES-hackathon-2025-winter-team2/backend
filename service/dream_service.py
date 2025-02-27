from repository.dream_repository import DreamRepository
from domain.dream import Dream


class DreamService:
    def __init__(self, dream_repository: DreamRepository):
        self.dream_repository = dream_repository

    def update_ended_at(self, dream_id: str) -> None:
        """指定されたIDのDreamのended_atを更新する"""
        self.dream_repository.update_ended_at(dream_id)
        return None

    def get_dream(self, dream_id: str) -> Dream:
        """指定されたIDのDreamを取得する"""
        return self.dream_repository.get_dream(dream_id)
