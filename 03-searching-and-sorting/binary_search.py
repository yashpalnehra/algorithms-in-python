def binary_search(sorted_items, target):
    """Index of target in a sorted list, or -1."""
    lo, hi = 0, len(sorted_items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_items[mid] == target:
            return mid
        if sorted_items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def first_at_least(sorted_items, target):
    """Index of the first item >= target. len(items) if there is none."""
    lo, hi = 0, len(sorted_items)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_items[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
