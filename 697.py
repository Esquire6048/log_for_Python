from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:


        #Sample Solution
        # user a dictionary to record the appearance of a number
        
        loc = defaultdict(list)
        for i, num in enumerate(nums):
            loc[num].append(i)
        
        max_freq = max([len(l) for num, l in loc.items()])

        if max_freq == 1:
            return 1
        res = len(nums)
        for num, l in loc.items():
            if len(l) == max_freq:
                res = min(res, l[-1] - l[0] + 1)

        return res


        #My Solution
        n = len(nums)
        cnt = [0] * 50000
        e = [0] * 50000
        s = [float("inf")] * 50000
        ans = float("inf")
        max_cnt = 0

        for i in range(n):
            cnt[nums[i]] += 1
            if i > e[nums[i]]:
                e[nums[i]] = i
            if i < s[nums[i]]:
                s[nums[i]] = i
            if cnt[nums[i]] > max_cnt:
                max_cnt = cnt[nums[i]]

        for i in range(n):
            if cnt[nums[i]] == max_cnt:
                if ans > e[nums[i]] - s[nums[i]] + 1:
                    ans = e[nums[i]] - s[nums[i]] + 1
        return ans
