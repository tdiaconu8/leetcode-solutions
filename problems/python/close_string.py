class Solution:
    def closeStrings(self, a: str, b: str) -> bool:

        if len(a) != len(b):
            return False

        counterA, counterB = {}, {}
        for i in range(len(a)):
            counterA[a[i]] = counterA.get(a[i], 0) + 1
            counterB[b[i]] = counterB.get(b[i], 0) + 1
        
        freqA, freqB = {}, {}
        setA, setB = set(), set()
        for k, v in counterA.items():
            freqA[v] = freqA.get(v, 0) + 1
            setA.add(k)
        for k, v in counterB.items():
            freqB[v] = freqB.get(v, 0) + 1
            setB.add(k)
        
        return setA == setB and (counterA == counterB or freqA == freqB)

'''
T: O(n)
S: O(n)
'''