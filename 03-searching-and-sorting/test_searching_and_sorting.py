import random

import pytest

from binary_search import binary_search, first_at_least
from sorting import insertion_sort, merge_sort, quick_sort

SORTS = [insertion_sort, merge_sort, quick_sort]


def test_binary_search_hits_and_misses():
    items = [1, 3, 5, 7, 9, 11]
    for i, value in enumerate(items):
        assert binary_search(items, value) == i
    assert binary_search(items, 4) == -1
    assert binary_search([], 1) == -1


def test_first_at_least():
    items = [1, 2, 2, 2, 5]
    assert first_at_least(items, 2) == 1
    assert first_at_least(items, 3) == 4
    assert first_at_least(items, 0) == 0
    assert first_at_least(items, 6) == 5


@pytest.mark.parametrize("sort", SORTS)
def test_small_cases(sort):
    assert sort([]) == []
    assert sort([1]) == [1]
    assert sort([3, 1, 2]) == [1, 2, 3]
    assert sort([2, 2, 1, 1]) == [1, 1, 2, 2]
    assert sort(["pear", "apple", "fig"]) == ["apple", "fig", "pear"]


@pytest.mark.parametrize("sort", SORTS)
def test_matches_builtin_on_random_input(sort):
    rng = random.Random(42)
    for _ in range(50):
        items = [rng.randint(-100, 100) for _ in range(rng.randint(0, 60))]
        assert sort(items) == sorted(items)


@pytest.mark.parametrize("sort", SORTS)
def test_does_not_change_input(sort):
    items = [3, 1, 2]
    sort(items)
    assert items == [3, 1, 2]


@pytest.mark.parametrize("sort", [insertion_sort, merge_sort])
def test_stable(sort):
    # equal keys keep their original order
    pairs = [(1, "a"), (0, "b"), (1, "c"), (0, "d")]
    assert sort(pairs) == [(0, "b"), (0, "d"), (1, "a"), (1, "c")]
