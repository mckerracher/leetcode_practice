from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    result = [1] * len(nums)
    multiplier = 1
    for i in range(len(nums)):
        result[i] = multiplier
        multiplier *= nums[i]
    multiplier = 1
    for i in reversed(range(len(nums))):
        result[i] *= multiplier
        multiplier *= nums[i]
    return result
