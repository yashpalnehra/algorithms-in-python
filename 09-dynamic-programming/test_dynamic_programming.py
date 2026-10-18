from knapsack import coin_change, knapsack, longest_increasing_subsequence
from sequences import (
    climb_stairs,
    edit_distance,
    fib,
    fib_iterative,
    longest_common_subsequence,
)


def test_fib_both_ways_agree():
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert [fib(n) for n in range(10)] == expected
    assert [fib_iterative(n) for n in range(10)] == expected
    assert fib(90) == fib_iterative(90) == 2880067194370816120


def test_climb_stairs():
    assert [climb_stairs(n) for n in range(1, 7)] == [1, 2, 3, 5, 8, 13]


def test_longest_common_subsequence():
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == 4


def test_edit_distance():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("", "abc") == 3
    assert edit_distance("same", "same") == 0
    assert edit_distance("flaw", "lawn") == 2


def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([186, 419, 83, 408], 6249) == 20


def test_knapsack():
    items = [(1, 1), (3, 4), (4, 5), (5, 7)]
    assert knapsack(items, 7) == 9
    assert knapsack(items, 0) == 0
    assert knapsack([], 10) == 0
    assert knapsack([(10, 100)], 5) == 0


def test_longest_increasing_subsequence():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence([7, 7, 7]) == 1
    assert longest_increasing_subsequence([]) == 0
