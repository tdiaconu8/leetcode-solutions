from math import ceil

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        n = len(nums)
        res = nums[0]
        prefixSum = nums[0]

        for i in range(1, n):
            prefixSum += nums[i]
            res = max(res, ceil(prefixSum/(i+1)))

        return res

        # T: O(n)
        # S: O(1)
