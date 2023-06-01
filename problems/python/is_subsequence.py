def isSubsequence(s: str, t: str) -> bool:

    if len(s) > len(t):
        return False
    if len(s) == len(t):
        if s == t: return True 
        else: return False
    if len(s) == 0:
        return True
    else:
        p = 0
        for char in t:
            if p == len(s):
                return True
            else:
                if char == s[p]:
                    p += 1
        if p == len(s):
            return True
        return False

# Time Complexity : O(t.length)
# Space Complexity : O(1)


# s = "axc"
# t = "ahbgdc"

s = 'b'
t = 'abc'

print(isSubsequence(s,t))