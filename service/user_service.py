from repository.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.find_all()

    def get_user_by_id(self, user_id: str):
        return self.user_repository.find_by_id(user_id)

    def update_user(self, user_id: str, user_data: dict):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            return None
        if 'name' in user_data:
            user.name = user_data['name']
        if 'email' in user_data:
            user.email = user_data['email']
        self.user_repository.session.commit()
        return user