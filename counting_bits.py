from typing import List


def countBits(n: int) -> List[int]:

    ans = [0] * (n+1)
    offset = 1
    for i in range(1,n+1):
        if 2 * offset == i:
            offset = i
        ans[i] = 1 + ans[i - offset]
    return ans 

    # ans = []
    # for i in range(n+1):
    #     b = [i for i in bin(i) if i=='1']
    #     ans.append(len(b))
    # return ans


# Time Complexity O(n)
# Space O(n)



# 0 = 0 --> 0

# 1 = 1 --> 1

# 2  = 10 --> 1
# 3 = 11 --> 2

# 4 = 100 --> 1
# 5 = 101 --> 2
# 6 = 110 --> 2
# 7 = 111 --> 3

# 8 = 1000 --> 1
# 9 = 1001 --> 2
# 10 = 1010 --> 2
# 11 = 1011 --> 3
# 12 = 1100 --> 2
# 13 = 1101 --> 3
# 14 = 1110 --> 3
# 15 = 1111 --> 4

# 16 = 10000 --> 1

n = 5
print(countBits(n))
