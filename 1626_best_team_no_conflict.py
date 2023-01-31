class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        n = len(scores)
        players = [(ages[i], scores[i]) for i in range(n)]
        players.sort()

        dp = [0]*n
        for i in range(n):
            age, score = players[i]
            dp[i] = score
            for j in range(i):
                if players[j][1] <= score:
                    dp[i] = max(dp[i], score+dp[j])

        return max(dp)

        '''
        T: O(n^2)
        S: O(n)
        '''
