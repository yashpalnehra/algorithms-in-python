from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def climb_stairs(n):
    """Ways to climb n steps taking 1 or 2 at a time."""
    one_back, two_back = 1, 1
    for _ in range(n - 1):
        one_back, two_back = one_back + two_back, one_back
    return one_back


def longest_common_subsequence(a, b):
    # table[i][j] is the answer for a[:i] and b[:j]
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[-1][-1]


def edit_distance(a, b):
    """Fewest single-character inserts, deletes or replacements to turn a into b."""
    prev = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        cur = [i]
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur.append(prev[j - 1])
            else:
                cur.append(1 + min(prev[j - 1], prev[j], cur[j - 1]))
        prev = cur
    return prev[-1]
