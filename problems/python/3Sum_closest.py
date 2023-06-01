'''
Given an integer array nums of length n and an integer target, find three integers 
in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
'''

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)
        nums.sort()
        res = float('inf')

        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if abs(curSum - target) < abs(res - target):
                    res = curSum
                if curSum < target:
                    l += 1
                elif curSum > target:
                    r -= 1
                elif curSum == target:
                    return curSum
        
        return res