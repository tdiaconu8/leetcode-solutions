class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        n = len(words)
        res = []

        # get the words to fill a new line with a with <= max width
        def getLine(i):
            line = []
            currLen = 0
            while i < n and currLen + len(words[i]) <= maxWidth:
                line.append(words[i])
                currLen += len(words[i]) + 1
                i += 1
            return line

        # create the line justified left and right
        def justifyLine(line, i):
            length = 0
            for word in line:
                length += len(word)+1
            length -= 1
            extraSpaces = maxWidth - length
            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extraSpaces
            m = len(line) - 1
            spacesPerWord, rem = divmod(extraSpaces, m)
            for j in range(rem):
                line[j] += " "
            for j in range(m):
                line[j] += " " * spacesPerWord
            return " ".join(line)
        
        i = 0
        while i < n:
            newLine = getLine(i)
            i += len(newLine)
            res.append(justifyLine(newLine, i))

        return res