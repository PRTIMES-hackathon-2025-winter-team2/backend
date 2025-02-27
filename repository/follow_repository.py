from typing import Optional
from sqlalchemy.orm import scoped_session
from domain.user import User
from domain.follow import Follow


class FollowRepository:
    def __init__(self, session: scoped_session):
        self.session = session

    def find_by_ids(self, from_user_id: str, to_user_id: str) -> Optional[Follow]:
        return (
            self.session.query(Follow)
            .filter_by(from_user_id=from_user_id, to_user_id=to_user_id)
            .first()
        )

    def get_followers_by_user_id(self, user_id: str) -> list[User]:
        return (
            self.session.query(User)
            .join(Follow, Follow.from_user_id == User.id)
            .filter(Follow.to_user_id == user_id)
            .all()
        )

    def get_following_by_user_id(self, user_id: str) -> list[User]:
        return (
            self.session.query(User)
            .join(Follow, Follow.to_user_id == User.id)
            .filter(Follow.from_user_id == user_id)
            .all()
        )

    def create(self, from_user_id: str, to_user_id: str) -> Follow:
        follow = Follow(from_user_id=from_user_id, to_user_id=to_user_id)
        self.session.add(follow)
        self.session.commit()
        return follow

    def delete(self, follow: Follow) -> None:
        self.session.delete(follow)
        self.session.commit()
