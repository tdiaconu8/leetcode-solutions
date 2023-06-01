def reverseWords(s: str) -> str:
    
    words = [word for word in s.split()]
    for i in range(len(words)):
        words[i] = [char for char in words[i]]
    
    for i in range(len(words)):
        l, r = 0, len(words[i])-1
        while l < r:
            words[i][l], words[i][r] = words[i][r], words[i][l]
            l+=1
            r-=1
        words[i] = ''.join(char for char in words[i])  
    print(words)
    return ' '.join(elem for elem in words)

s = "Let's take LeetCode contest"

print(reverseWords(s))