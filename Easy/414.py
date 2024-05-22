from typing import List


# My Solution
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums = sorted(nums)
        return nums[-3]


# My Solution
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")

        for num in nums:
            if num > first:
                second, third = first, second
                first = num
            elif num > second and num < first:
                third = second
                second = num
            elif num > third and num < second:
                third = num

        return third if third != float("-inf") else first
