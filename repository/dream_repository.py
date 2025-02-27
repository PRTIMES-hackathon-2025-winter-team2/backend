from typing import Optional
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
