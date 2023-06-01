def brokenCalc(x: int, y: int) -> int:
    
    res = 0
    
    while x != y:
        if y <= x:
            res += int(x-y)
            y = x
        else:
            if y%2 == 0:
                y = y/2
                res += 1
            else:
                y += 1
                res += 1
    
    return res

# Time : O(|x-y|)
# Space : O(1)

x, y = 3, 10
print(brokenCalc(x,y))