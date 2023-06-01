class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        n = len(nums)
        curSum, minSum = 0, float('inf')

        # KADANE ALGO
        for num in nums:
            curSum = min(num, curSum + num)
            minSum = min(minSum, curSum)
        
        curSum, maxSum = 0, -float('inf')
        for num in nums:
            curSum = max(num, curSum + num)
            maxSum = max(curSum, maxSum)
        
        if minSum == sum(nums):
            return maxSum
        return max(sum(nums) - minSum, maxSum)
