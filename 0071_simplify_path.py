class Solution:
    def simplifyPath(self, path: str) -> str:

        pathList = path.split('/')
        stack = []
        
        for elem in pathList:
            if not elem or elem == '.':
                continue
            if elem == '..':
                stack and stack.pop()
            else:
                stack.append(elem)
        
        return '/' + '/'.join(elem for elem in stack)

        # T: O(n)
        # S: O(n)
