'''You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.'''

'''
100, 50 -> 0

[100, 200], 50 --> 1
'''


from collections import deque
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        res, cur = 0, 0
        tokens.sort()
        queue = deque(tokens)
        
        while queue:
            
            if cur == 0 and power < queue[0]:
                return res
            
            elif power >= queue[0]:
                power -= queue.popleft()
                cur += 1
                res = max(cur, res)
            
            else:
                power += queue.pop()
                cur -= 1
        
        return res