from sqlalchemy.orm import scoped_session
from domain.dream import Dream
from datetime import datetime

class DreamRepository:
    def __init__(self, session: scoped_session):
        self.session = session

    def creates(self, dreams: list[Dream]) -> list[Dream]:
        for dream in dreams:
            dream.created_at = datetime.now()
            self.session.add(dream)
        self.session.commit()
        return dreams

    def create(self, dream: Dream) -> Dream:
        dream.created_at = datetime.now()
        self.session.add(dream)
        self.session.commit()
        return dream

    def update_ended_at(self, dream_id: str):
        dream = self.session.query(Dream).filter(Dream.id == dream_id).first()
        if not dream:
            raise Exception(f"指定されたIDのDreamが存在しません: {dream_id}")
        dream.ended_at = datetime.now()
        self.session.commit()
