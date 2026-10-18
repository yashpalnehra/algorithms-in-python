class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, keys=()):
        self.root = None
        for key in keys:
            self.insert(key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        node = self.root
        while True:
            if key == node.key:
                return
            side = "left" if key < node.key else "right"
            child = getattr(node, side)
            if child is None:
                setattr(node, side, Node(key))
                return
            node = child

    def __contains__(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def inorder(self):
        """Keys in sorted order."""
        yield from self._inorder(self.root)

    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            yield node.key
            yield from self._inorder(node.right)

    def min(self):
        node = self._leftmost(self.root)
        return node.key

    def _leftmost(self, node):
        if node is None:
            raise ValueError("empty tree")
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            # two children: swap in the next larger key, then remove it below
            successor = self._leftmost(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node
