from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for s in strs:
            ana = ''.join(char for char in sorted(s))
            groups[ana] = groups.get(ana, []) + [s]
        
        return list(key for _, key in groups.items())

        '''
        T: O(m*n*log(n))
        S: O(m)
        '''