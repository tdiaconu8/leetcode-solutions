from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        n, m = len(strs), len(strs[0])
        res = 0

        for j in range(m):
            for i in range(1, n):
                if ord(strs[i][j]) < ord(strs[i-1][j]):
                    res += 1
                    break
        
        return res

        '''
        T: O(n*m)
        S: O(1)
        '''
        
        '''
        n, m = len(strs), len(strs[0])
        res = 0

        for j in range(m):
            tmp = []
            for i in range(n):
                tmp.append(ord(strs[i][j]))
            print(tmp)
            if tmp != sorted(tmp):
                res += 1
        
        print(res)
        return res
        '''