def longest_unique_substring(text):
    """Length of the longest run with no repeated character."""
    last_seen = {}
    start = best = 0
    for i, ch in enumerate(text):
        if last_seen.get(ch, -1) >= start:
            # repeat inside the window, move the window past it
            start = last_seen[ch] + 1
        last_seen[ch] = i
        best = max(best, i - start + 1)
    return best


def reverse_words(sentence):
    return " ".join(reversed(sentence.split()))


def compress(text):
    """Run-length encode: aaabcc becomes a3bc2."""
    if not text:
        return ""
    out = []
    run = 1
    for prev, ch in zip(text, text[1:]):
        if ch == prev:
            run += 1
        else:
            out.append(prev + (str(run) if run > 1 else ""))
            run = 1
    out.append(text[-1] + (str(run) if run > 1 else ""))
    return "".join(out)
