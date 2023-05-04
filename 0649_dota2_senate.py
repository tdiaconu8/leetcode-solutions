class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r, d = [], []

        for i, c in enumerate(senate):
            if c == "R":
                r.append(i)
            else:
                d.append(i)
        
        while r and d:
            rTurn, dTurn = r.pop(0), d.pop(0)
            if rTurn < dTurn:
                r.append(rTurn + len(senate))
            else:
                d.append(dTurn + len(senate))
        
        return "Radiant" if not d else "Dire"

        # T: O(n)
        # S: O(n)
        
        
