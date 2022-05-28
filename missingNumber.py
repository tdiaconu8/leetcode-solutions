from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == 1 else 1
        
        interval = [-1] * (n+1)
        
        for i, num in enumerate(nums):
            interval[num] = 1
        
        for i, val in enumerate(interval):
            if val == -1:
                return i
        
        # T : O(n)
        # S : O(n)