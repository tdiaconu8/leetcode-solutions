class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        num.reverse() # reverse list for optimizing time complexity

        n = len(num)
        i, carry = 0, 0

        while k > 0 or carry > 0:
            if i < n:
                num[i] += k%10 + carry
            elif i >= n:
                num.append(k%10 + carry)
            num[i], carry = num[i]%10, num[i]//10
            k = k//10
            i+= 1
        
        
        num.reverse()
        return num

        # T: O(max(n,k))
        # S: O(1) -> no extra space used
