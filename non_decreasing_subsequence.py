class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        self.res = set()

        def backtrack(i, sub):

            if len(sub) > 1:
                    self.res.add(tuple(sub))

            if i == n:
                return
                
            val = nums[i]
            if not sub or val >= sub[-1]:
                backtrack(i+1, sub+[val])
            backtrack(i+1, sub)
        
        backtrack(0, [])
        return self.res
