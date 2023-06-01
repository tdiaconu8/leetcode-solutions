from collections import defaultdict

def isValid(s: str) -> bool:
    
    br = defaultdict(list)
    br['('] = ')'
    br['['] = ']'
    br['{'] = '}'
    
    rm = []
    
    for char in s:
        if char in br.keys():
            rm.append(br[char])
        else:
            if not rm:
                return False
            c = rm.pop()
            if c != char:
                return False
    
    if rm:
        return False
    return True

# Time : O(n)
# Space : O(n)