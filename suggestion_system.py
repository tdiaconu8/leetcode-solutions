from typing import List


def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    
    n = len(searchWord)
    products.sort()
    ans = []
    
    for i in range(n):
        cur = []
        for p in products:
            if len(cur) == 3:
                break
            elif p[:i+1] == searchWord[:i+1]:
                cur.append(p)
        ans.append(cur)
    
    return ans

'''
n -> products.length, m -> searchWord.length
T: O(nlogn)
S: O(m)
'''