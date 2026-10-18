def coin_change(coins, amount):
    """Fewest coins that make amount, or -1 if it cannot be made."""
    best = [0] + [float("inf")] * amount
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total and best[total - coin] + 1 < best[total]:
                best[total] = best[total - coin] + 1
    return best[amount] if best[amount] != float("inf") else -1


def knapsack(items, capacity):
    """Best total value of (weight, value) items within capacity, each used once."""
    best = [0] * (capacity + 1)
    for weight, value in items:
        # go downwards so each item is only counted once per row
        for cap in range(capacity, weight - 1, -1):
            best[cap] = max(best[cap], best[cap - weight] + value)
    return best[capacity]


def longest_increasing_subsequence(numbers):
    if not numbers:
        return 0
    # best[i] is the longest increasing run ending at i
    best = [1] * len(numbers)
    for i in range(1, len(numbers)):
        for j in range(i):
            if numbers[j] < numbers[i]:
                best[i] = max(best[i], best[j] + 1)
    return max(best)
