class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        n = len(people)
        res = 0

        if people[-1] > limit:
            return -1
        
        l, r = 0, n-1

        while l <= r:
            if people[l] + people[r] <= limit:
                res += 1
                l +=1
                r -= 1
            elif l == r:
                res += 1
                break
            else:
                res += 1
                r -= 1

        return res

        # T: O(nlogn)
        # S: O(1)
