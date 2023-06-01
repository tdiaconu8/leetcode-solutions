from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        counter, res = {}, 0

        # map task value to number of occurences
        for _, task in enumerate(tasks):
            counter[task] = counter.get(task, 0) + 1
        
        for key, val in counter.items():
            if val == 1:  # if the task appears only 1 time, we return -1
                return -1
            if val%3 == 0:  # if val%3 == 0, we solve the task by group of 3
                res += val//3
            else: 
                res += val//3+1
        
        return res

        '''
        T: O(n)
        S: O(n)
        '''