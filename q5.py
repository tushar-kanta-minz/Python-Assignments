from collections import Counter

def is_anagram_efficient(str1, str2):
    return Counter(str1) == Counter(str2)


print(is_anagram_efficient("heart", "earth"))  # Output: True
print(is_anagram_efficient("hello", "world"))  # Output: False
