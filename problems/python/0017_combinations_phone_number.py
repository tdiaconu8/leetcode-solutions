class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        n = len(digits)

        phoneMap = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y", "z"],
        }

        res = []

        def backtrack(i, curr):
            if i == n:
                if curr:
                    res.append(curr[:])
                return
            for digit in phoneMap[digits[i]]:
                curr += digit                
                backtrack(i+1, curr)
                curr = curr[:-1]
        
        backtrack(0, "")
        return res