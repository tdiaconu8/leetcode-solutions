class Solution:
    def validPartition(self, nums: List[int]) -> bool:

        # T: O(n)
        # S: O(n)
        
        n = len(nums)

        cache = {}

        def dfs(i):
            if i == n:
                return True
            if i in cache:
                return cache[i]
            res = False
            if i < n-1 and nums[i] == nums[i+1]:
                res = dfs(i+2)
            if i < n-2 and ((nums[i] == nums[i+1] == nums[i+2]) or (nums[i+1] - nums[i] == nums[i+2] - nums[i+1] == 1)):
                res = res or dfs(i+3)
            cache[i] = res
            return res
        
        return dfs(0)