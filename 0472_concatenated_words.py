class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        wordsSet = set(words)

        # for each word, we make a dfs to check if it can be concatenated
        cache = {}
        def dfs(word):
            if word in cache:
                return cache[word]
            n = len(word)
            for i in range(n):
                prefix, suffix = word[:i+1], word[i+1:]
                if prefix in wordsSet and suffix in wordsSet:
                    cache[word] = True
                    return True
                if prefix in wordsSet and dfs(suffix):
                    cache[word] = True
                    return True
            cache[word] = False
            return False

        # we iterate through all the array
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res

        '''
        N = len(words)
        M = max(len(word) for word in words)
        T: O(N*M*M*M)
        S: O(N*M)
        '''
