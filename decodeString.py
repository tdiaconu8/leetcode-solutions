class Solution:
    def decodeString(self, s: str) -> str:
        
        ans = ''
        cur = 0
        stack = []
        
        for char in s:
            if char.isnumeric():
               cur = cur*10 + int(char)
            else:
                if cur > 0:
                    stack.append(cur)
                    cur = 0
                if char == ']':
                    tmp = ''
                    while stack[-1] != '[':
                        tmp = stack.pop() + tmp
                    stack.pop()
                    tmp = stack.pop() * tmp
                    stack.append(tmp)
                else:
                    stack.append(char)
        
        return ''.join(elem for elem in stack)