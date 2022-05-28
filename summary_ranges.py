from typing import List


def summaryRanges( nums: List[int]) -> List[str]:
    
    res = []
        
    if not nums:
        return res

    a, b = nums[0], nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] == b+1:
            b+= 1
        elif nums[i] != b+1:
            if a == b:
                res.append(str(a))
            elif a != b:
                res.append(str(a) + '->' + str(b))
            a, b = nums[i], nums[i]
    if a == b:
        res.append(str(a))
    elif a != b:
        res.append(str(a) + '->' + str(b))
    return res


nums = [0,2,3,4,6,8,9]
print(summaryRanges(nums))

# Time Complexity : O(n)
# Space Complexity : O(n)


        
        