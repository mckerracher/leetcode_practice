from typing import List


def productExceptSelf_bruteforce_solution(nums: List[int]) -> List[int]:
    i, ret = 0, []
    while i < len(nums):
        product, counter = 1, 0
        while counter < len(nums):
            if counter == i:
                counter += 1
            else:
                product *= nums[counter]
                counter += 1
        ret.append(product)
        i += 1
    return ret