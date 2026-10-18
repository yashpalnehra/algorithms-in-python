def is_palindrome(text):
    """True if the letters and digits read the same both ways."""
    cleaned = [ch.lower() for ch in text if ch.isalnum()]
    return cleaned == cleaned[::-1]


def longest_palindrome(text):
    """Longest palindromic substring, expanding around each centre."""
    best = ""
    for centre in range(len(text)):
        # odd length, then even length
        for lo, hi in ((centre, centre), (centre, centre + 1)):
            while lo >= 0 and hi < len(text) and text[lo] == text[hi]:
                lo -= 1
                hi += 1
            if hi - lo - 1 > len(best):
                best = text[lo + 1 : hi]
    return best
