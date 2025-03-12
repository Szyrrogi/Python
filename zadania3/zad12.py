def czy_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(czy_anagram("abc", "cba"))