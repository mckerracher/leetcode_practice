from typing import List


def longestConsecutive(nums: List[int]):
    max_length, numbers = 0, set(nums)
    for i in range(len(nums)):
        tmp_len = 1
        if nums[i] - 1 not in numbers:
            counter = nums[i] + 1
            while counter in numbers:
                tmp_len += 1
                counter += 1
        max_length = max(max_length, tmp_len)
    return max_length
