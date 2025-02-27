from domain.tree import Tree
from domain.dream import Dream
from repository.tree_repository import TreeRepository
from repository.dream_repository import DreamRepository
from service.schema.tree_schema import (
    GetTreesResponseSchema,
    PostTreeRequestSchema,
    PostTreeResponseSchema,
    GetTreeResponseSchema,
    PatchTreeRequestSchema,
    TreeBase,
    GetAllUsersTreesResponseSchema,
    TreeSchemaWithUserID,
)


class TreeService:
    def __init__(
        self, tree_repository: TreeRepository, dream_repository: DreamRepository
    ):
        self.dream_repository = dream_repository
        self.tree_repository = tree_repository

    def get_all_users_trees(self) -> GetAllUsersTreesResponseSchema:
        trees = self.tree_repository.get_all_users_trees()
        if not trees:
            raise ValueError("Trees not found")
        trees = [
            TreeSchemaWithUserID(id=tree.id, title=tree.title, user_id=tree.user_id)
            for tree in trees
        ]

        return GetAllUsersTreesResponseSchema(trees=trees)

    def get_trees_by_user_id(self, user_id: str) -> GetTreesResponseSchema:
        trees = self.tree_repository.get_trees_by_user_id(user_id)
        if not trees:
            raise ValueError(f"Trees not found for user_id: {user_id}")
        trees = [TreeBase(id=tree.id, title=tree.title) for tree in trees]

        return GetTreesResponseSchema(trees=trees)

    def get_tree_by_id(self, tree_id: str) -> GetTreeResponseSchema:
        tree = self.tree_repository.get_tree_by_id(tree_id)
        if not tree:
            raise ValueError(f"Tree not found for tree_id: {tree_id}")
        dreams = []
        for dream in tree.dreams:
            dreams.append(
                {
                    "id": dream.id,
                    "title": dream.title,
                    "position": dream.position,
                    "created_at": dream.created_at,
                    "ended_at": dream.ended_at,
                }
            )

        return GetTreeResponseSchema(id=tree.id, title=tree.title, dreams=dreams)

    def create_tree(
        self, user_id: str, body: PostTreeRequestSchema
    ) -> PostTreeResponseSchema:
        tree = Tree(user_id=user_id, title=body.title)
        tree = self.tree_repository.create(tree)
        dreams = [
            Dream(tree_id=tree.id, title=dream.title, position=dream.position)
            for dream in body.dreams
        ]
        self.dream_repository.creates(dreams)
        return PostTreeResponseSchema(id=tree.id)

    def update_tree(self, tree_id: str, body: PatchTreeRequestSchema) -> TreeBase:
        tree = self.tree_repository.get_tree_by_id(tree_id)
        if not tree:
            raise ValueError(f"Tree not found for tree_id: {tree_id}")
        if body.name:
            tree.title = body.name
        if body.ended_at:
            tree.ended_at = body.ended_at

        tree = self.tree_repository.update_tree(tree)
        return TreeBase(id=tree.id, title=tree.title)

    def delete_tree(self, tree_id: str) -> None:
        tree = self.tree_repository.get_tree_by_id(tree_id)
        if not tree:
            raise ValueError(f"Tree not found for tree_id: {tree_id}")
        self.tree_repository.delete_tree(tree)
        return None
