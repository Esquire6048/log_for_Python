from typing import List


# Sample Solution
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(i, nums[i] - 1)
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1


# My Solution
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        isone = False

        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
            if nums[i] == 1:
                isone = True
        if not isone:
            return 1

        for i in range(n):
            if nums[i] != 0:
                num = abs(nums[i]) - 1
                if nums[num] > 0:
                    nums[num] = -nums[num]
                elif nums[num] == 0:
                    nums[num] = -1

        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        return n + 1
