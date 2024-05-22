from typing import List


# Sample Solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = -1

        for j, x in enumerate(nums):
            if x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]


# My Solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        length = len(nums)

        for j in range(length):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
