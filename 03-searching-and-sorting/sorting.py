def insertion_sort(items):
    result = list(items)
    for i in range(1, len(result)):
        value = result[i]
        j = i - 1
        while j >= 0 and result[j] > value:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = value
    return result


def merge_sort(items):
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    return _merge(merge_sort(items[:mid]), merge_sort(items[mid:]))


def _merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        # <= keeps the sort stable
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(items):
    if len(items) <= 1:
        return list(items)
    pivot = items[len(items) // 2]
    smaller = [x for x in items if x < pivot]
    equal = [x for x in items if x == pivot]
    larger = [x for x in items if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(larger)
