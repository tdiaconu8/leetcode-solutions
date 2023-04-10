class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        lookup = {'}': '{', ')':'(', ']': '['}

        for char in s:
            if char in lookup:
                if not stack or lookup[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        
        return not stack

        # T: O(n)
        # S: O(n)
