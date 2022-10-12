'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, 
formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
'''
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()

        for i in range(n-1, 1, -1):
            a,b,c = nums[i], nums[i-1], nums[i-2]
            if a < b+c:
                return a+b+c
        return 0