class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        m = len(flowerbed)

        for i in range(m):
            if n == 0:
                return True
            if flowerbed[i] == 0 and ((i == 0 and i == m-1) or (i == 0 and flowerbed[i+1]==0) or (i==m-1 and flowerbed[i-1]==0) or (flowerbed[i-1] == 0 and flowerbed[i+1]== 0)):
                flowerbed[i] = 1
                n -= 1
        
        return n == 0

        #T: O(n)
        # S: O(1)
