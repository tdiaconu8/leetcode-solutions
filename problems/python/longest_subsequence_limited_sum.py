from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        n, m = len(nums), len(queries)
        res = []

        nums.sort()

        for i, val in enumerate(queries):
            curSum = 0
            j = 0
            while curSum < val and j < n:
                if curSum + nums[j] > val:
                    break
                else:
                    curSum += nums[j]
                    j += 1
            res.append(j)
        
        return res

        '''
        T: O(n*m)
        S: O(1)
        '''