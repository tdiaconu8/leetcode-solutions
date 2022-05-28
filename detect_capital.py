def detectCapitalUse(word: str) -> bool:
    
    # all letters are not capitals (e.g. leetcode)
    if word == word.lower():
        return True
    
    # Only the first letter is capital
    elif word[0].lower() + word[1:] == word.lower():
        return True
    
    else:
        if word[0].islower():
            return False
        elif word[0].isupper():
            for i in range(1, len(word)):
                if word[i].islower():
                    return False
            return True

# word = "USA"
word = "FlaG"
print(detectCapitalUse(word))