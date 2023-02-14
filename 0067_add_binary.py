class Solution:
    def addBinary(self, a: str, b: str) -> str:

        n, m = len(a), len(b)
        i = 0
        carry = 0
        res = ''

        while i < n or i < m:
            if i >= n:
                q = int(b[m-1-i])
            if i >= m:
                q = int(a[n-1-i])
            if i < n and i < m:
                q = int(a[n-1-i]) + int(b[m-1-i])
            q += carry
            if q <= 1:
                res = str(q) + res
                carry = 0
            else:
                if q == 2:
                    res = '0' + res
                if q == 3:
                    res = '1' + res
                carry = 1
            i += 1
        
        if carry:
            res = '1' + res
        
        return res

        # T: O(max(n,m))
        # S: O(max(n,m))
