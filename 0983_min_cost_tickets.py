class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        daysSet = set(days)

        res = float('inf')
        cache = {}

        def dfs(day):
            if day > 365:
                return 0
            if day in cache:
                return cache[day]
            if day not in daysSet:
                return dfs(day+1)
            else:
                cache[day] = min(costs[0]+dfs(day+1), costs[1]+dfs(day+7), costs[2]+dfs(day+30))
            return cache[day]

        return dfs(1)
