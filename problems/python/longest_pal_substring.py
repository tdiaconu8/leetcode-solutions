def longestPalindrome(s: str) -> str:
    
    n = len(s)
    res, curLen = '', 0
    
    for i in range(n):
        
        l, r = i,i
        while l >= 0 and r < n and s[l] == s[r]:
            if curLen < r-l+1:
                res = s[l:r+1]
                curLen = r-l+1
            r += 1
            l -= 1
        
        l, r = i,i+1
        while l >= 0 and r < n and s[l] == s[r]:
            if curLen < r-l+1:
                res = s[l:r+1]
                curLen = r-l+1
            r += 1
            l -= 1
    
    return res

'''
Time : O(n**2)
Space : O(1)
'''