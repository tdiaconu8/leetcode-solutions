class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        res = []

        def BT(start, partition):

            if start >= n:
                res.append(partition)
                return
            for i in range(start, n):
                if isPalindrome(s[start:i+1]):
                    BT(i+1, partition+[s[start:i+1]])
            return
        
        def isPalindrome(s: str):
            l, r = 0, len(s)-1
            while l <= r:
                if s[l] != s[r]:
                    return False
                else:
                    l, r = l+1, r-1
            return True
        
        BT(0, [])
        return res
