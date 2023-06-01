from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temperatures[i], i))

        return res

        '''
        BRUTE FORCE : O(n²)
        n = len(temperatures)
        res = [0] * n

        for i in range(n-1):
            for j in range(i+1, n):
                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break
        
        return res
        '''