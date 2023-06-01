def minRemoveToMakeValid(s: str) -> str:
    
    res = list(s)
    stack = []
    
    for i, v in enumerate(res):
        if v == '(':
            stack.append(i)
        elif v == ')':
            if stack:
                stack.pop()
            elif not stack:
                res[i] = ''
    for elem in stack:
        res[elem] = ''
    
    return ''.join(char for char in res)

# Time: O(n)
# Space: O(n) 