from anagrams import group_anagrams, is_anagram
from palindromes import is_palindrome, longest_palindrome
from substrings import compress, longest_unique_substring, reverse_words


def test_is_anagram():
    assert is_anagram("listen", "silent")
    assert is_anagram("Dormitory", "dirty room")
    assert not is_anagram("hello", "world")
    assert not is_anagram("aab", "abb")


def test_group_anagrams():
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert groups == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert group_anagrams([]) == []


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("")
    assert not is_palindrome("race a car")


def test_longest_palindrome():
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("") == ""
    assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"


def test_longest_unique_substring():
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
    assert longest_unique_substring("") == 0
    assert longest_unique_substring("abba") == 2


def test_reverse_words():
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("  hello   world  ") == "world hello"


def test_compress():
    assert compress("aaabcc") == "a3bc2"
    assert compress("abc") == "abc"
    assert compress("zzzzzzzzzzzz") == "z12"
    assert compress("") == ""
