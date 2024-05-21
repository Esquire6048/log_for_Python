from typing import List
from itertools import pairwise


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # Sample Solution
        count = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                if count == 1:
                    return False
                if i - 2 >= 0 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
                count += 1
        return True

        # My Solution
        def is_sorted(nums: List[int]) -> bool:
            return all(a <= b for a, b in pairwise(nums))

        length = len(nums)
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                if is_sorted(nums):
                    return True
                nums[i] = nums[i + 1] = temp
                return is_sorted(nums)
        return True
