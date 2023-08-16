from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # T: O(n)
        # S: O(n)

        n = len(nums)
        q = deque()
        l, r = 0, 0
        res = []

        while r < n:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if r-l+1 == k:
                res.append(nums[q[0]])
                if q[0] == l:
                    q.popleft()
                l += 1
            r += 1
        return res



        # TLE: O(n*k)  (k(n-k))
        '''
        n = len(nums)
        res = []

        for i in range(n-k+1):
            res.append(max(nums[i: i+k])) 
        
        return res
        '''