def two_sum(numbers, target):
    """Return indexes of two numbers adding up to target, or None."""
    seen = {}
    for i, n in enumerate(numbers):
        if target - n in seen:
            return seen[target - n], i
        seen[n] = i
    return None
