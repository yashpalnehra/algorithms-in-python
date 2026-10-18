import pytest

from counting import first_unique_char, index_by, subarray_sum_count, top_k_frequent
from lru_cache import LRUCache


def test_lru_evicts_oldest():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    assert "a" not in cache
    assert cache.get("b") == 2
    assert cache.get("c") == 3


def test_lru_get_refreshes():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.get("a")
    cache.put("c", 3)
    assert "b" not in cache
    assert "a" in cache


def test_lru_update_keeps_size():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("a", 2)
    assert len(cache) == 1
    assert cache.get("a") == 2
    assert cache.get("missing", "dflt") == "dflt"


def test_lru_bad_capacity():
    with pytest.raises(ValueError):
        LRUCache(0)


def test_first_unique_char():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1


def test_top_k_frequent():
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent(["b", "a", "b", "a"], 1) == ["a"]
    assert top_k_frequent([], 3) == []


def test_index_by():
    users = [
        {"name": "ann", "city": "oslo"},
        {"name": "bob", "city": "rome"},
        {"name": "cy", "city": "oslo"},
    ]
    grouped = index_by(users, "city")
    assert [u["name"] for u in grouped["oslo"]] == ["ann", "cy"]
    assert [u["name"] for u in grouped["rome"]] == ["bob"]


def test_subarray_sum_count():
    assert subarray_sum_count([1, 1, 1], 2) == 2
    assert subarray_sum_count([1, 2, 3], 3) == 2
    assert subarray_sum_count([1, -1, 0], 0) == 3
    assert subarray_sum_count([], 0) == 0
