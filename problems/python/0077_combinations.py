class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(i, nums):
            if len(nums) == k:
                res.append(nums[:])
            else:
                for j in range(i+1, n+1):
                    nums.append(j)
                    backtrack(j, nums)
                    nums.pop()
        
        backtrack(0, [])
        return res