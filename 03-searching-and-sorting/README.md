# Searching and sorting

Binary search in two flavours: exact match, and the first position at or above a value. Plus three sorts written by hand: insertion, merge and quick sort.

None of the sorts change the list you pass in. The tests compare each one against Python's `sorted` on random input and check that insertion and merge sort are stable.

Tests: `python3 -m pytest`.
