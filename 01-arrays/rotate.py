def rotate_right(items, k):
    """Move every item k places to the right, wrapping around."""
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k] if k else list(items)


def remove_duplicates(sorted_items):
    """Drop repeats from a sorted list, keeping order."""
    result = []
    for item in sorted_items:
        if not result or result[-1] != item:
            result.append(item)
    return result
