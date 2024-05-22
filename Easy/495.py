from typing import List
from itertools import pairwise


# My Solution
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        end_time = cnt = 0

        for time in timeSeries:
            if time >= end_time:
                cnt += duration
            else:
                cnt = cnt - (end_time - time)
                cnt += duration
            end_time = time + duration

        return cnt
