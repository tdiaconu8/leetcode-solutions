class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if low % 2 == 0:
            low += 1
        
        return (high-low)//2 + 1
      
      # T: O(1)
      # S: O(1)
