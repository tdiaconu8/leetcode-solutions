class Solution:
    def partitionString(self, s: str) -> int:

        n = len(s)
        res = 1
        partition = set()

        for i in range(n):
            curChar = s[i]
            if curChar in partition:
                res += 1
                partition = set()
            partition.add(curChar)
        
        return res

        # T: O(n)
        # S: O(n)
