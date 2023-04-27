class Solution:
    def bulbSwitch(self, n: int) -> int:

        '''
        Initial state: all bulbs are ON
        A Bulb will be ON, if we toggle it 2*p times. In other words, if it has an odd numbers of divisors.
        The solution is to find the numbers that have an odd number of divisors.
        A number x will have itself as divisor which makes 1. Now this number can have other pair of divisors a*b=x. These pairs will generate even numver of divisor. To make it even, it must have one divisor a such that a*a = x. In other words, x is a PERFECT SQUARE.
        The solution is actually to count the number of perfect squares from 1 to n.
        '''

        #CODE
        '''
        res = 0
        for i in range(1, n+1):
            if i*i > n:
                break
            else:
                res += 1
        
        return res
        '''

        # Actually, we make a sum from 1 to int(sqrt(n)), which means that there are int(sqrt(n))-1+1 = int(sqrt(n)) elements.

        return int(sqrt(n))
      
      # T: O(1), S: 0(1)
