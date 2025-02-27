from flask import blueprints, jsonify
from flask_pydantic import validate
from repository.tree_repository import TreeRepository
from repository.dream_repository import DreamRepository
from service.tree_service import TreeService
from settings import get_db_session
from service.schema.tree_schema import PostTreeRequestSchema, PatchTreeRequestSchema
from settings import app
from flask_jwt_extended import jwt_required, get_jwt_identity

user_tree_blueprint = blueprints.Blueprint('user_tree', __name__, url_prefix='/users/<string:user_id>/trees')
tree_blueprint = blueprints.Blueprint('tree', __name__, url_prefix='/trees')
tree_service = TreeService(TreeRepository(get_db_session()), DreamRepository(get_db_session()))

@tree_blueprint.route('/', methods=['GET'])
def get_all_trees():
    response = tree_service.get_all_users_trees()
    return jsonify(response.model_dump())

@user_tree_blueprint.route('/', methods=['GET'])
def get_all_user_trees(user_id):
    response = tree_service.get_trees_by_user_id(user_id)
    return jsonify(response.model_dump())

@user_tree_blueprint.route('/', methods=['POST'])
@jwt_required()
@validate()
def post_user_trees(user_id, body: PostTreeRequestSchema):
    app.logger.info(f"user_id: {get_jwt_identity()}")
    saved_tree = tree_service.create_tree(user_id, body)
    return jsonify(saved_tree.model_dump()), 201  # 201 Created

@user_tree_blueprint.route('/<string:tree_id>', methods=['GET'])
@validate()
def get_user_tree(user_id, tree_id):
    tree = tree_service.get_tree_by_id(tree_id)
    return jsonify(tree.model_dump())

@user_tree_blueprint.route('/<string:tree_id>', methods=['PATCH'])
@validate()
def patch_user_tree(user_id, tree_id, body: PatchTreeRequestSchema):
    updated_tree = tree_service.update_tree(tree_id, body)
    return jsonify(updated_tree.model_dump())

@user_tree_blueprint.route('/<string:tree_id>', methods=['DELETE'])
def delete_user_tree(user_id, tree_id):
    tree_service.delete_tree(tree_id)
    return jsonify({}), 204
