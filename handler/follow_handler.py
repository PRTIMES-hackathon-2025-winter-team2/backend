from flask import blueprints, request, jsonify
from flask_pydantic import validate
from service.schema.auth_schema import UserRegisterSchema, UserLoginSchema, TokenResponseSchema
from service.auth_service import AuthService
from repository.user_repository import UserRepository
from repository.follow_repository import FollowRepository
from settings import get_db_session


follow = blueprints.Blueprint('follow', __name__, url_prefix='/follow')
user_repository = UserRepository(get_db_session())
follow_repository = FollowRepository(get_db_session())

def get_user_id_from_token():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None
    token = auth_header.split(" ")[1]
    user_id = AuthService.decode_token(token)
    return user_id

@follow.route('/<string:user_id>', methods=['POST'])
def post_follow(user_id):
    from_user_id = get_user_id_from_token()
    if not from_user_id:
        return jsonify({"error": "Invalid token"}), 401

    existing_follow = follow_repository.find_by_ids(from_user_id=from_user_id, to_user_id=user_id)
    if existing_follow:
        return jsonify({"error": "Already following"}), 400

    follow = follow_repository.create(from_user_id=from_user_id, to_user_id=user_id)
    return jsonify({"from_user_id": follow.from_user_id, "to_user_id": follow.to_user_id}), 201

@follow.route('/<string:user_id>', methods=['DELETE'])
def delete_follow(user_id):
    from_user_id = get_user_id_from_token()
    if not from_user_id:
        return jsonify({"error": "Invalid token"}), 401

    follow = follow_repository.find_by_ids(from_user_id=from_user_id, to_user_id=user_id)
    if not follow:
        return jsonify({"error": "Follow relationship not found"}), 404

    follow_repository.delete(follow)
    return jsonify({"from_user_id": from_user_id, "to_user_id": user_id}), 200

@follow.route('/<string:user_id>/followers', methods=['GET'])
def get_followers(user_id):
    followers = follow_repository.get_followers_by_user_id(user_id)
    followers_data = [{"id": follower.id, "name": follower.name} for follower in followers]
    return jsonify(followers_data), 200

@follow.route('/<string:user_id>/following', methods=['GET'])
def get_following(user_id):
    followers = follow_repository.get_following_by_user_id(user_id)
    followers_data = [{"id": follower.id, "name": follower.name} for follower in followers]
    return jsonify(followers_data), 200
