from typing import List

'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        n = len(nums)
        x, y = float('inf'), float('inf')

        for i in range(n):
            val = nums[i]
            if val < x:
                x = val
            elif x < val < y:
                y = min(val, y)
            elif val > y:
                return True
        
        return False