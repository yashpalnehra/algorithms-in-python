from collections import deque


def height(node):
    """Number of nodes on the longest root-to-leaf path. 0 for an empty tree."""
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def level_order(root):
    """Keys level by level, left to right, as a list of lists."""
    if root is None:
        return []
    levels = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    return levels


def is_balanced(root):
    """Heights of the two sides differ by at most one, everywhere."""
    return _balanced_height(root) != -1


def _balanced_height(node):
    # returns the height, or -1 as soon as one subtree is off balance
    if node is None:
        return 0
    left = _balanced_height(node.left)
    if left == -1:
        return -1
    right = _balanced_height(node.right)
    if right == -1 or abs(left - right) > 1:
        return -1
    return 1 + max(left, right)


def lowest_common_ancestor(root, a, b):
    """In a BST, the split point between two keys is their lowest common ancestor."""
    node = root
    while node:
        if a < node.key and b < node.key:
            node = node.left
        elif a > node.key and b > node.key:
            node = node.right
        else:
            return node.key
    return None
