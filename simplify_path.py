def simplifyPath(path: str) -> str:

    path = path.replace('//', '/')
    elems = path.split('/')
    folders = []
    periods = []
    
    for e in elems:
        if e == '..':
            if folders:
                folders.pop()
        elif e != '' and e != '.':
            folders.append(e)
    res = '/' + '/'.join(char for char in folders)
    while res[-1] == '/' and len(res) > 1:
        res = res[:-1]
    return res

# Time : O(n)
# Space : O(n)