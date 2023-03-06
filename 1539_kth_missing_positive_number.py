class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        n = len(arr)
        i, num = 0, 1

        while i < n and k > 0:
            if arr[i] == num:
                num +=1
                i += 1
            else:
                num += 1
                k -= 1
        
        return num + k - 1

        # T: O(n)
        # S: O(1)
