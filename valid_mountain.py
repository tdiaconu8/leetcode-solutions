from typing import List

def validMountainArray(arr: List[int]) -> bool:
    
    n = len(arr)
    
    if n <= 2:
        return False
    
    else:
        ind = 0
        while ind < n-1 and arr[ind] < arr[ind+1]:
            ind +=1
        if ind == 0 or ind == n-1:
            return False
        else:
            while ind < n-1 and arr[ind] > arr[ind+1]:
                    ind+=1
            return ind == n-1

# arr = [2,1]
# arr = [0,3,2,1]
# arr = [3,5,5]
arr = [0,1,2,3,4,8,9,10,11,12]

print(validMountainArray(arr))