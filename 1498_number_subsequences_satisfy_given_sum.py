class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort() # subsequences are the same for the unsorted and sorted array
        n = len(nums)
        res, MOD = 0,  10**9+7

        for i in range(n):
            l, r = 0, n-1
            while l <= r:
                m = (l+r)//2
                if nums[m] <= target-nums[i]:
                    l = m+1
                else:
                    r = m-1
            if l-1>= i: # l will be the most left value greater than target-nums[i]
                res += 2**(l-1-i)
        
        return res%MOD

        # T: O(nlogn)
        # S: O(1)
