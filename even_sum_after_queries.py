'''
You are given an integer array nums and an array queries where queries[i] = [vali, indexi].

For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.

Return an integer array answer where answer[i] is the answer to the ith query.
'''

from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        evenSum = 0
        for num in nums:
            if num%2 == 0:
                evenSum += num
        
        res = []
        for val, i in queries:
            if nums[i] % 2 == 0:
                evenSum -= nums[i]
            nums[i] += val
            if (nums[i])%2 == 0:
                evenSum += nums[i]
            res.append(evenSum)
            
        return res