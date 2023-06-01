class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        res, i = 0, 0

        # Greedy approach
        while i < len(costs) and coins > 0:
            price = costs[i]
            if price <= coins:
                res += 1
                i += 1
                coins -= price
            else:
                break
        return res
        
        '''
        T: O(nlogn)
        S: O(1) --> no extra space
        '''
