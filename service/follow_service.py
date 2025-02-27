from repository.follow_repository import FollowRepository


class FollowService:
    def __init__(self, follow_repository: FollowRepository):
        self.follow_repository = follow_repository

    def follow_user(self, from_user_id: str, to_user_id: str):
        existing_follow = self.follow_repository.find_by_ids(from_user_id, to_user_id)
        if existing_follow:
            return {"error": "Already following"}, 400

        follow = self.follow_repository.create(from_user_id, to_user_id)
        return {
            "from_user_id": follow.from_user_id,
            "to_user_id": follow.to_user_id,
        }, 201

    def unfollow_user(self, from_user_id: str, to_user_id: str):
        follow = self.follow_repository.find_by_ids(from_user_id, to_user_id)
        if not follow:
            return {"error": "Follow relationship not found"}, 404

        self.follow_repository.delete(follow)
        return {"from_user_id": from_user_id, "to_user_id": to_user_id}, 200

    def get_followers(self, user_id: str):
        followers = self.follow_repository.get_followers_by_user_id(user_id)
        followers_data = [
            {"id": follower.id, "name": follower.name} for follower in followers
        ]
        return followers_data, 200

    def get_following(self, user_id: str):
        following = self.follow_repository.get_following_by_user_id(user_id)
        following_data = [
            {"id": follower.id, "name": follower.name} for follower in following
        ]
        return following_data, 200
