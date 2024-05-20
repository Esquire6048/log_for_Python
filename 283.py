class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sample Solution
        i = -1
        for j, x in enumerate(nums):
            if x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        # My Solution
        i = j = 0
        length = len(nums)
        while i < length:
            if nums[i] != 0:
                i += 1
                j += 1
            else:
                while j < length and nums[j] == 0:
                    j += 1
                if j < length:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
        