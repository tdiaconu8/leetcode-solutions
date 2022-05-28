from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    
    left = 0
    right = len(nums)-1
        
    while left < right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid+1
        if nums[mid] > target:
            right = mid-1
    if nums[left] < target:
        return left+1
    if nums[left] > target:
        return left

# nums = [1,3,5,6]
# target = 2

# nums = [1,3,5,6]
# target = 5

nums = [1,3,5,6]
target = 7

print(searchInsert(nums, target))