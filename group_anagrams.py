from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for word in strs:
        count_array = [0] * 26
        for letter in word:
            count_array[ord(letter) - ord("a")] += 1
        result[tuple(count_array)].append(word)
    return result.values()
