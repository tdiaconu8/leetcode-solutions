class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        ans = 0
        
        for i in range(n):
            
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            
            l = i
            r = i+1
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        
        return ans
    
    # T : O(n²)
    # S : O(1)