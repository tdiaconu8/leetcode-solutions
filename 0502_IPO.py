from heapq import *

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        heapify(projects)
        maxProfit = []

        for _ in range(min(n,k)):
            while projects and projects[0][0] <= w:
                heappush(maxProfit, -heappop(projects)[1])
            if maxProfit:
                w += -heappop(maxProfit)
        
        return w

        # T: O(max(nlogn, k*logn))
        # S: O(n)




        ######################################################
        ######################################################
        ######################################################

        # O(n*k)
        '''
        # APPROACH
        # iterate over k
        # we pick a project with capital <= w and the maximises the NET profit

        n = len(profits)
        used = [False for i in range(n)]

        def getMaxNetProfit(cap):
            res, maxProfit = -1, -1
            for i in range(n):
                if (capital[i] <= cap) and (profits[i] > maxProfit) and (not used[i]):
                    maxProfit = profits[i]
                    res = i
            if res == -1:
                return 0
            used[res] = True
            return profits[res]

        for _ in range(min(k,n)):
            w += getMaxNetProfit(w)
        
        return w
        '''
