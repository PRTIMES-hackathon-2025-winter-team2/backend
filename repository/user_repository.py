from typing import Optional
from sqlalchemy.orm import scoped_session
from domain.user import User
import bcrypt
from settings import app

class UserRepository:
    def __init__(self, session: scoped_session):
        self.session = session

    def find_by_email(self, email: str) -> Optional[User]:
        return self.session.query(User).filter(User.email == email).first()

    def find_by_id(self, id: str) -> Optional[User]:
        return self.session.query(User).filter(User.id == id).first()

    def find_all(self) -> list[User]:
        return self.session.query(User).all()

    def compare_password(self, email: str, password: str) -> bool:
        user = self.find_by_email(email)
        if user is None:
            app.logger.error('User not found')
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))

    def create(self, user: User) -> User:
        # データベースに文字列として保存
        user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        self.session.add(user)
        self.session.commit()
        return user
