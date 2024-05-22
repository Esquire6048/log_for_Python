from typing import List


# My Solution
# k: number of moves
# sum + (n-1) * k = n * target
# target = min + k
# k = sum - n * min
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
