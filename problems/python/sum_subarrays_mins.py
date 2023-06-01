from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n, mod = len(arr), 10**9+7
        res = 0
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                idx = stack.pop()
                l = -1 if not stack else stack[-1]
                r = i
                res += arr[idx] * (r-idx) * (idx-l)
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            l = -1 if not stack else stack[-1]
            r = n
            res += arr[idx] * (r-idx) * (idx-l)
        
        return res%mod


        # TLE : O(n²)
        '''
        n, mod = len(arr), 10**9+7
        res = sum(arr)
        for i in range(1, n):
            curMin = arr[i]
            for j in range(i-1, -1, -1):
                curMin = min(curMin, arr[j])
                res += curMin
        
        return res%mod
        '''