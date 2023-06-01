class Solution:
    def arraySign(self, nums: List[int]) -> int:

        neg = 0 # nb of negative numbers

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg += 1
        
        return 1 if neg%2==0 else -1

        # T: O(n)
        # S: O(1)
