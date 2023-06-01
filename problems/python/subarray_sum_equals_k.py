class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        prefixSums, curSum = {0: 1}, 0

        for num in nums:
            curSum += num
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

        return res
      
      '''
      T: O(n)
      S: O(n)
      '''
