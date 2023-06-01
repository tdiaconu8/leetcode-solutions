from typing import List


def numberOfArithmeticSlices(nums: List[int]) -> int:

    if len(nums) <= 2:
        return 0
    
    else:
        res = 0
        d = nums[1] - nums[0]
        l = 2
        for i in range(2,len(nums)):
            if nums[i] - nums[i-1] == d:
                l += 1
            else:
                if l >= 3:
                    res += sum([i for i in range(l-1)])
                d = nums[i] - nums[i-1]
                l = 2
        if l >= 3:
            res += sum([i for i in range(l-1)])
        return res

# Time Complexity : O(n)
# Space Complexity : O(1)

nums = [2,4,6,8,12]
print(numberOfArithmeticSlices(nums))


# 123 1234 12345 123456 234 2345 23456 345 3456 456
# 123 1234 12345 123456 1234567 234 2345 23456 234567 345 3456 34567 456 4567 567