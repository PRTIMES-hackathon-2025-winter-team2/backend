from flask import blueprints, jsonify
from repository.dream_repository import DreamRepository
from service.dream_service import DreamService
from settings import get_db_session

user_tree_dream_blueprint = blueprints.Blueprint(
    "user_tree_dream",
    __name__,
    url_prefix="/users/<string:user_id>/trees/<string:tree_id>/dreams",
)
tree_service = DreamService(DreamRepository(get_db_session()))


@user_tree_dream_blueprint.route("/<string:dream_id>", methods=["PATCH"])
def update_ended_at(user_id: str, tree_id: str, dream_id: str):
    try:
        tree_service.update_ended_at(dream_id)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message": "success"}), 200
