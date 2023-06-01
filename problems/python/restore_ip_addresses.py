class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        n = len(s)
        res = []

        def BT(i, curIP):

            if i >=n:
                if len(curIP) == 4:
                    res.append('.'.join(char for char in curIP))
                return
            else:
                lastElement = curIP[-1]
                if lastElement == '0':
                    BT(i+1, curIP+[s[i]])
                else:
                    BT(i+1, curIP+[s[i]])
                    if int(lastElement)*10+int(s[i]) <= 255:
                        newLast = curIP[-1] + s[i]
                        curIP[-1] = newLast
                        BT(i+1, curIP)
        
        BT(1, [s[0]])
        return res
