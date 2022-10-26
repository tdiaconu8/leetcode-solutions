'''
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least 
two whose elements sum up to a multiple of k, or false otherwise.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
'''

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        rem, curSum = {0: -1}, 0
        
        for i, num in enumerate(nums):
            curSum += num
            r = curSum%k
            if r not in rem:
                rem[r] = i
            elif i - rem[r] > 1:
                return True
        
        return False