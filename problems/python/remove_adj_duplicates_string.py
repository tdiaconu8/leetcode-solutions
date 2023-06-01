class Solution:
    def removeDuplicates(self, s: str) -> str:

        N = len(s)
        stack = []

        for i in range(N):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return ''.join(char for char in stack)