from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        n = len(ideas)
        res = 0
        groups = defaultdict(set) # we group ideas by their first char

        for i in range(n):
            idea = ideas[i]
            groups[idea[0]].add(idea[1:])
        
        keys = list(groups.keys()) 
        for i in range(len(keys)-1):
            for j in range(i+1, len(keys)):
                mutuals = groups[keys[i]] & groups[keys[j]]
                res += 2*(len(groups[keys[i]])-len(mutuals))*(len(groups[keys[j]])-len(mutuals))
        
        return res

        # n -> length of ideas, m -> abg length of a word
        # T: O(325*n*m)
        # S: O(n)


        ##########################################################################
        ##########################################################################


        # TLE: O(n^2)
        '''
        n = len(ideas)
        ideasSet = set(ideas)
        res = 0

        for i in range(n-1):
            for j in range(i+1, n):
                a = ideas[i][0] + ideas[j][1:]
                b = ideas[j][0] + ideas[i][1:]
                if a not in ideasSet and b not in ideasSet:
                    res +=2
        
        return res
        '''
