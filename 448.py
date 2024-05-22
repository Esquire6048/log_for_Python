from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:


        # Sample Solution
        # Finding an element in the set is O(1)
        s = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in s]


        # My Solution
        n = len(nums)
        cnt = [0] * n
        miss = []
        for num in nums:
            cnt[num - 1] = 1
        for i in range(n):
            if cnt(i) == 0:
                miss.append(i + 1)
        return miss

        