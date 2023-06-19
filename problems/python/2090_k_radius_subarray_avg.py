class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        # T: O(n)
        # S: O(n)

        n = len(nums)
        prefixSum = [0]

        curSum = 0
        for num in nums:
            curSum += num
            prefixSum.append(curSum)
        
        res = []

        for i in range(n):
            if i-k < 0 or i+k >= n:
                res.append(-1)
                continue
            avg = (prefixSum[i+k+1]-prefixSum[i-k])/(2*k+1)
            res.append(int(avg))
        
        return res