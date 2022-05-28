def myAtoi(s: str) -> int:
        
        digits = [i for i in range(10)]
        signs = ['-', '+']
        # Get max range
        max_value = 2**31
        
        # Digits
        digits = [str(i) for i in range(10)]
        
        # Remove space chars
        n = len(s)
        
        # Value of the sign
        sign = 1
        
        # Value of of the integer
        integer = 0
        
        ind = 0
        
        while ind < n and s[ind] == ' ':
            ind += 1
        
        if ind < n and s[ind] == '-':
            sign = -1
            ind += 1
        elif ind < n and s[ind] == '+':
            sign = 1
            ind += 1
        
        while ind < n and s[ind] in digits:
            digit = int(s[ind])
            integer = integer * 10 + digit
            ind += 1
                
        
        val = sign * integer
            
        if (val > max_value - 1):
            val = max_value - 1
        
        if (val < - max_value):
            val = - max_value
        
        return integer


s = '-+12'
print(myAtoi(s))