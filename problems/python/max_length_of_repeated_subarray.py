'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
'''

from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        # DYNAMIC PROGRAMMING
        # O(n*m)
        n, m = len(nums1), len(nums2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                    if dp[i][j] > res:
                        res = dp[i][j]
        return res
        
        # TWO POINTERS HASHMAP : TIME LIMIT EXCEEDED
        # O(n*m*min(n,m))
        '''
        n, m = len(nums1), len(nums2)
        lookup = {}
        for i, val in enumerate(nums2):
            lookup[val] = lookup.get(val, []) + [i]
        
        res = 0
        
        for i, num in enumerate(nums1):
            if num not in lookup:
                continue
            for val in lookup[num]:
                cur = 0
                l, r = i, val
                while l < n and r < m and nums1[l] == nums2[r]:
                    cur += 1
                    l += 1
                    r += 1
                res = max(res, cur)
        
        return res
        '''