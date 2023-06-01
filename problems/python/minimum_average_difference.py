from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return 0

        leftSum = [0] * n
        rightSum = [0] * n

        curSum = 0
        for i in range(n):
            curSum += nums[i]
            leftSum[i] = int(curSum/(i+1))
        
        curSum = nums[-1]
        for i in range(n-2, -1, -1):
            rightSum[i] = int(curSum/(n-1-i))
            curSum += nums[i]
        
        res = [float('inf'), -1]
        for i in range(n):
            diff = abs(leftSum[i] - rightSum[i])
            if diff < res[0]:
                res[0] = diff
                res[1] = i
        
        return res[1]

        '''
        T: O(n)
        S: O(n)
        '''