from flask import blueprints, jsonify

from repository.dream_repository import DreamRepository
from service.dream_service import DreamService
from settings import get_db_session
from flask_jwt_extended import jwt_required, get_jwt_identity

user_tree_dream_blueprint = blueprints.Blueprint(
    "user_tree_dream",
    __name__,
    url_prefix="/users/<string:user_id>/trees/<string:tree_id>/dreams",
)
dream_service = DreamService(DreamRepository(get_db_session()))


@user_tree_dream_blueprint.route("/<string:dream_id>", methods=["PATCH"])
@jwt_required()
def update_ended_at(user_id: str, tree_id: str, dream_id: str):
    current_user_id = get_jwt_identity()
    dream_user_id = dream_service.get_dream_owner(dream_id)
    if str(current_user_id) != str(dream_user_id):
        return jsonify({"message": "Unauthorized"}), 401
    try:
        dream_service.update_ended_at(dream_id)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message": "success"}), 200
