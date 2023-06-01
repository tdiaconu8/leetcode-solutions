class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 0:
            return ''
        
        if n == 1:
            return '1'
        
        else:
            res = ''
            prev = self.countAndSay(n-1)
            k, val = 1, prev[0]
            for i in range(1, len(prev)):
                if prev[i] == val:
                    k += 1
                else:
                    res += str(k) + val
                    k = 1
                    val = prev[i]
            res += str(k) + val
            return res