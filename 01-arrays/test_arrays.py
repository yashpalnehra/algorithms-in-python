import pytest

from max_subarray import max_subarray
from rotate import remove_duplicates, rotate_right
from two_sum import two_sum


def test_two_sum_found():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)


def test_two_sum_not_found():
    assert two_sum([1, 2, 3], 100) is None
    assert two_sum([], 0) is None


def test_two_sum_does_not_use_same_index_twice():
    assert two_sum([5], 10) is None
    assert two_sum([5, 5], 10) == (0, 1)


def test_max_subarray():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([-3, -1, -2]) == -1
    assert max_subarray([5, 4, -1, 7, 8]) == 23


def test_max_subarray_empty():
    with pytest.raises(ValueError):
        max_subarray([])


def test_rotate_right():
    assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_right([1, 2, 3], 3) == [1, 2, 3]
    assert rotate_right([1, 2, 3], 4) == [3, 1, 2]
    assert rotate_right([], 3) == []


def test_remove_duplicates():
    assert remove_duplicates([1, 1, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]
    assert remove_duplicates([]) == []
    assert remove_duplicates([7, 7, 7]) == [7]
