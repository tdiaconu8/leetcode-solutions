from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    
    n = len(nums)
    counter, freq = {}, [[] for _ in range(n+1)]
    
    for val in nums:
        counter[val] = counter.get(val, 0) + 1
    
    for elem in counter.keys():
        freq[counter[elem]].append(elem)
    
    ans = []
    
    
    for i in range(n, -1, -1):
        if k == 0:
            break
        else:
            if freq[i]:
                for elem in freq[i]:
                    ans.append(elem)
                    k -= 1
    return ans

'''
T: O(n)
S: O(n)
'''