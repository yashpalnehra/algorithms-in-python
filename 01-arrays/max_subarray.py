def max_subarray(numbers):
    """Largest sum of any contiguous run (Kadane). Needs at least one number."""
    if not numbers:
        raise ValueError("need at least one number")
    best = current = numbers[0]
    for n in numbers[1:]:
        # either extend the run or start fresh here
        current = max(n, current + n)
        best = max(best, current)
    return best
