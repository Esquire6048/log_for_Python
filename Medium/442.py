from typing import List


# Sample Solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [v for i, v in enumerate(nums) if v != i + 1]


# My Solution
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = []

        for i in range(n):
            num = abs(nums[i]) - 1
            if nums[num] > 0:
                nums[num] = -nums[num]
            else:
                s.append(num + 1)
        return s
