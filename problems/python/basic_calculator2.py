def calculate(s: str) -> int:
    
    s = s.replace(' ','')
    priors = {'+': 0, '-': 0, '*': 1, '/': 1}
    
    stack, op = [], []
    cur_Nb = -1
    
    # build the stack
    for char in s:
        if char.isnumeric():
            if cur_Nb == -1:
                cur_Nb = int(char)
            else:
                cur_Nb = cur_Nb * 10 + int(char)
        if char in priors.keys():
            stack.append(cur_Nb)
            cur_Nb = -1
            while len(op) > 0 and priors[op[-1]] >= priors[char]:
                stack.append(op.pop())
            op.append(char)
    if cur_Nb >= 0:
        stack.append(cur_Nb)
    while len(op) > 0:
        stack.append(op.pop())
        
    print(stack)
    
    # read the stack
    nums = []
    for elem in stack:
        if elem == '+':
            a, b = nums.pop(), nums.pop()
            nums.append(a+b)
        elif elem == '-':
            b, a = nums.pop(), nums.pop()
            nums.append(a-b)
        elif elem == '*':
            a, b = nums.pop(), nums.pop()
            nums.append(a*b)
        elif elem == '/':
            b, a = nums.pop(), nums.pop()
            nums.append(int(a/b))
        else:
            nums.append(elem)
        print(nums)
    return nums.pop()

'''
Time: O(n)
Space: O(n)
'''


'''
[1, 2, '*', 3, 4, '/', 5, 6, '*', 7, 8, '*', 9, 10, '/', '+', '-', '+', '-']

2- 0 + 30 - 56 + 0    + - + -'''