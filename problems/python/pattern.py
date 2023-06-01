def wordPattern(pattern: str, s: str):
    words = s.split()
    if len(pattern) != len(words):
        return False
    else:
        d = {}
        for i in range(len(pattern)):
            if pattern[i] in list(d.keys()) and d[pattern[i]] != words[i]:
                return False
            elif  pattern[i] not in list(d.keys()) and words[i] in list(d.values()):
                return False
            else:
                d[pattern[i]] = words[i]
        return True

pattern = "abba"
s = "dog dog dog dog"

print(wordPattern(pattern, s))