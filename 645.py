from typing import List
from collections import Counter


class Solution:
    # Sample Solution
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        n = len(nums)
        ans = [0] * 2
        for x in range(1, n + 1):
            if cnt[x] == 2:
                ans[0] = x
            if cnt[x] == 0:
                ans[1] = x
        return ans

    # My Solution
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        visited = [False] * (n + 1)
        x = y = 0
        for i in range(0, n):
            if visited[nums[i]]:
                x = nums[i]
            else:
                visited[nums[i]] = True
        for i in range(1, n + 1):
            if not visited[i]:
                y = i
                break
        return [x, y]
