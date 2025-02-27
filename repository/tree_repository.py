from datetime import datetime
from typing import Optional

from sqlalchemy.orm import scoped_session

from domain.tree import Tree


class TreeRepository:
    def __init__(self, session: scoped_session):
        self.session = session

    def get_trees_by_user_id(self, user_id: str) -> Optional[list[Tree]]:
        return self.session.query(Tree).filter(Tree.user_id == user_id).all()

    def get_tree_by_id(self, tree_id: str) -> Optional[Tree]:
        return self.session.query(Tree).filter(Tree.id == tree_id).first()

    def get_all_users_trees(self) -> Optional[list[Tree]]:
        return (
            self.session.query(Tree)
            .distinct(Tree.user_id)
            .order_by(Tree.user_id, Tree.created_at.desc())
            .all()
        )

    def update_tree(self, tree: Tree) -> Tree:
        self.session.commit()
        return tree

    def delete_tree(self, tree: Tree) -> None:
        self.session.delete(tree)
        self.session.commit()

    def create(self, tree: Tree) -> Tree:
        tree.created_at = datetime.now()
        self.session.add(tree)
        self.session.commit()
        return tree
