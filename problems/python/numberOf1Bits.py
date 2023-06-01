class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ans = 0
        while n:
            print(n)
            n = n & (n-1)
            print(n)
            ans += 1
       
        return ans