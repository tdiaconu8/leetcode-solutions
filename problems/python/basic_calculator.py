def calculate(s: str) -> int:
    
    s = s.replace(' ','')
    
    ans, cur_Nb, stack, sign = 0, 0, [], 1
    
    for char in s:
        if char.isdigit():
            cur_Nb = cur_Nb*10 + int(char)
        else:
            if char == '+':
                ans += sign * cur_Nb
                cur_Nb = 0
                sign = 1
            elif char == '-':
                ans += sign * cur_Nb
                sign = -1
                cur_Nb = 0
            elif char == '(':
                stack.append(ans)
                stack.append(sign)
                ans, sign = 0, 1
            elif char == ')':
                ans += cur_Nb*sign
                a, b = stack.pop(), stack.pop()
                ans *= a
                ans += b
                cur_Nb = 0
    return ans + sign*cur_Nb

'''
Time: O(n)
Space: O(n)

Astuce : mettre dans la pile tout le résultat avant la parenthèse, ainsi que le signe devant la parenthèse

'''