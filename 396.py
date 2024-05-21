from typing import List


# Sample Solution
def maxRotateFunction(self, nums: List[int]) -> int:
    f = sum(i * v for i, v in enumerate(nums))
    n, s = len(nums), sum(nums)
    ans = f
    for i in range(1, n):
        f = f + s - n * nums[n - i]
        ans = max(ans, f)
    return ans


# My Solution
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        temp_sum = 0
        for i in range(n):
            temp_sum += i * nums[i]
        max_sum = temp_sum
        nums_sum = sum(nums)
        for i in range(n):
            temp_sum = temp_sum + nums_sum - n * nums[n - 1 - i]
            max_sum = max(temp_sum, max_sum)
        return max_sum
