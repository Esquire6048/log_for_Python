from typing import List


# Sample Solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i: int, j: int):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1

        n = len(nums)
        k %= n
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


# My Solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        new_nums = [0] * length
        k = k % length

        for i in range(length):
            new_nums[i] = nums[(i + length - k) % length]
        for i in range(length):
            nums[i] = new_nums[i]
