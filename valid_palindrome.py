def validPalindrome(s: str) -> bool:
    
    if s[::-1] == s:
        return True
    
    l, r, d = 0, len(s)-1, 0
    while l < r:
        if s[l] != s[r]:
            if (s[:l] + s[l+1:])[::-1] == s[:l] + s[l+1:]:
                return True
            elif (s[:r] + s[r+1:])[::-1] == s[:r] + s[r+1:]:
                return True
            else:
                return False
        else:
            l += 1
            r -= 1
    
    # Time : O(n)
    # Space : O(1)