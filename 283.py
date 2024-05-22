from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # Sample Solution
        i = -1
        for j, x in enumerate(nums):
            if x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]


        # My Solution
        i = 0
        length = len(nums)
        
        for j in range(length):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
