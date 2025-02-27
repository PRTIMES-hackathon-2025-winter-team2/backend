from flask import blueprints, request, jsonify
from service.auth_service import AuthService
from service.follow_service import FollowService
from repository.follow_repository import FollowRepository
from settings import get_db_session

follow_blueprint = blueprints.Blueprint("follow", __name__, url_prefix="/follow")
follow_repository = FollowRepository(get_db_session())
follow_service = FollowService(follow_repository)


def get_user_id_from_token():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None
    token = auth_header.split(" ")[1]
    user_id = AuthService.decode_token(token)
    return user_id


@follow_blueprint.route("/<string:user_id>", methods=["POST"])
def post_follow(user_id):
    from_user_id = get_user_id_from_token()
    if not from_user_id:
        return jsonify({"error": "Invalid token"}), 401

    response, status = follow_service.follow_user(from_user_id, user_id)
    return jsonify(response), status


@follow_blueprint.route("/<string:user_id>", methods=["DELETE"])
def delete_follow(user_id):
    from_user_id = get_user_id_from_token()
    if not from_user_id:
        return jsonify({"error": "Invalid token"}), 401

    response, status = follow_service.unfollow_user(from_user_id, user_id)
    return jsonify(response), status


@follow_blueprint.route("/<string:user_id>/followers", methods=["GET"])
def get_followers(user_id):
    response, status = follow_service.get_followers(user_id)
    return jsonify(response), status


@follow_blueprint.route("/<string:user_id>/following", methods=["GET"])
def get_following(user_id):
    response, status = follow_service.get_following(user_id)
    return jsonify(response), status
