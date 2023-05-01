class Solution:
    def average(self, salary: List[int]) -> float:

        sm, mn, mx = sum(salary), min(salary), max(salary)

        return (sm-mn-mx)/(len(salary)-2)

        # T: O(3.n)
        # S: O(1)
