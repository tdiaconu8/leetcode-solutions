class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def backtrack(i, curr):
            if len(curr) == n:
                res.append(curr[:])
                return
            for j in range(n):
                num = nums[j]
                if num not in curr:
                    curr.append(num)
                    backtrack(j, curr)
                    curr.pop()
        
        backtrack(0, [])
        return res