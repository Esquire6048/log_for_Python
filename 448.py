from typing import List


# Sample Solution
# Finding an element in the set is O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in s]


# My Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = [0] * n
        miss = []

        for num in nums:
            cnt[num - 1] = 1

        for i in range(n):
            if cnt(i) == 0:
                miss.append(i + 1)
        return miss
