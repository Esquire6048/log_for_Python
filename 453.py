class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # k: number of moves
        # sum + (n-1) * k = n * target
        # target = min + k
        # k = sum - n * min
        return sum(nums) - min(nums) * len(nums)
