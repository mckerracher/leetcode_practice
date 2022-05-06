def is_pair_anagram(s: str, t: str) -> bool:
    """
    Tests if two input strings are case insensitive anagrams.
    :param s1: First input string.
    :param s2: Second input string.
    :return: True if the strings are anagrams, false otherwise.
    """
    if len(s) != len(t):
        return False

    s1_map, s2_map = {}, {}

    for i in range(len(s)):
        s1_map[s[i]] = 1 + s1_map.get(s[i], 0)  # if key doesn't exist yet, 0 is used as default count
        s2_map[t[i]] = 1 + s2_map.get(t[i], 0)

    for key in s1_map:
        if s1_map[key] != s2_map.get(key, 0):
            return False

    return True