import pytest

from bst import BinarySearchTree
from traversals import height, is_balanced, level_order, lowest_common_ancestor


@pytest.fixture
def tree():
    #        8
    #      /   \
    #     3     10
    #    / \      \
    #   1   6      14
    return BinarySearchTree([8, 3, 10, 1, 6, 14])


def test_insert_and_contains(tree):
    assert 6 in tree
    assert 14 in tree
    assert 7 not in tree
    tree.insert(7)
    assert 7 in tree


def test_duplicate_insert_is_ignored(tree):
    tree.insert(3)
    assert list(tree.inorder()) == [1, 3, 6, 8, 10, 14]


def test_inorder_is_sorted():
    import random

    keys = random.Random(1).sample(range(1000), 200)
    assert list(BinarySearchTree(keys).inorder()) == sorted(keys)


def test_min(tree):
    assert tree.min() == 1
    with pytest.raises(ValueError):
        BinarySearchTree().min()


def test_delete_leaf_one_child_two_children(tree):
    tree.delete(1)
    assert list(tree.inorder()) == [3, 6, 8, 10, 14]
    tree.delete(10)
    assert list(tree.inorder()) == [3, 6, 8, 14]
    tree.delete(8)
    assert list(tree.inorder()) == [3, 6, 14]
    assert tree.root.key == 14
    tree.delete(99)
    assert list(tree.inorder()) == [3, 6, 14]


def test_height_and_levels(tree):
    assert height(tree.root) == 3
    assert height(None) == 0
    assert level_order(tree.root) == [[8], [3, 10], [1, 6, 14]]
    assert level_order(None) == []


def test_is_balanced(tree):
    assert is_balanced(tree.root)
    skewed = BinarySearchTree([1, 2, 3])
    assert not is_balanced(skewed.root)
    assert is_balanced(None)


def test_lowest_common_ancestor(tree):
    assert lowest_common_ancestor(tree.root, 1, 6) == 3
    assert lowest_common_ancestor(tree.root, 1, 14) == 8
    assert lowest_common_ancestor(tree.root, 10, 14) == 10
