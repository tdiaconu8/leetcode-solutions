class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        n = len(pushed)
        i, j = 0, 0

        while i < n and j < n:
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                stack.append(pushed[i])
                i += 1
        
        while j < n:
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False
        
        return True

        # T: O(n)
        # S: O(n)
