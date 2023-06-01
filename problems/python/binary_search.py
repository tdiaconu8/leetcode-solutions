from typing import List


def search(self, nums: List[int], target: int) -> int:
    
    left = 0
    right = len(nums)-1
    
    while left <= right:
        pivot = (left+right)//2
        if nums[pivot] == target:
            return pivot
        if nums[pivot] < target:
            left = pivot+1
        elif nums[pivot] > target:
            right = pivot-1
    
    return -1

# Time : O(logn)
# Space : O(1)