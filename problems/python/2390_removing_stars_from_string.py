class Solution:
    def removeStars(self, s: str) -> str:

        stack = []

        for char in s:
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        
        return ''.join(char for char in stack)

        # T: O(n)
        # S: O(n)
