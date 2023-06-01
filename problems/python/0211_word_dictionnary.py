from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode)

class WordDictionary:

    def __init__(self):
        self.dict = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.dict
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isWord = True

    def search(self, word: str) -> bool:
        # DFS
        def dfs(i, node):
            if i == len(word):
                return node.isWord
            if word[i] == '.':
                for child in node.children:
                    if dfs(i+1, node.children[child]):
                        return True
            else:
                if word[i] in node.children:
                    return dfs(i+1, node.children[word[i]])
                return False
        
        return dfs(0, self.dict)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
