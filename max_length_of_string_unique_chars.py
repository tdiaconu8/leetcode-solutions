'''
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of 
arr that has unique characters.
Return the maximum possible length of s.
A subsequence is an array that can be derived from another array by deleting some or no elements without 
changing the order of the remaining elements.
'''

from collections import Counter
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def hasUniqueChars(s):
            return max(Counter(s).values()) <= 1

        def helper(i):
            if i == len(arr):
                return ['']
            tmp = helper(i+1)
            ret = tmp
            for w in tmp:
                test = w + arr[i]
                if hasUniqueChars(test):
                    ret.append(test)
            return ret
        
        words = helper(0)
        res = 0
        for word in words:
            res = max(res, len(word))
        return res