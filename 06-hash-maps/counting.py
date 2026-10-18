from collections import Counter, defaultdict


def first_unique_char(text):
    """Index of the first character that appears once, or -1."""
    counts = Counter(text)
    for i, ch in enumerate(text):
        if counts[ch] == 1:
            return i
    return -1


def top_k_frequent(items, k):
    """The k most common items, most common first, ties by value."""
    counts = Counter(items)
    ranked = sorted(counts, key=lambda item: (-counts[item], item))
    return ranked[:k]


def index_by(records, key):
    """Group dicts by one of their fields: index_by(users, "city")."""
    groups = defaultdict(list)
    for record in records:
        groups[record[key]].append(record)
    return dict(groups)


def subarray_sum_count(numbers, target):
    """How many contiguous runs add up to target. Prefix sums in a dict."""
    seen = {0: 1}
    running = count = 0
    for n in numbers:
        running += n
        count += seen.get(running - target, 0)
        seen[running] = seen.get(running, 0) + 1
    return count
