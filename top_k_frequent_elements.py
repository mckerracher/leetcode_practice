from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = {}
    for num in nums:
        counts[num] = 1 + counts.get(num, 0)

    frequency = [[] for i in range(len(nums) + 1)]
    for number, count in counts.items():
        frequency[count].append(number)

    result = []
    for i in reversed(range(len(frequency))):
        for num in frequency[i]:
            result.append(num)
            if len(result) == k:
                return result