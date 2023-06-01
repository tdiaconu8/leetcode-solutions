from collections import defaultdict

class TrieNode:
    def __init__(self, letter = ''):
        self.letter = letter
        self.isWord = False
        self.chars = defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur.chars:
                cur.chars[char] = TrieNode(char)
            cur = cur.chars[char]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if char not in cur.chars:
                return False
            cur = cur.chars[char]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for char in prefix:
            if char not in cur.chars:
                return False
            cur = cur.chars[char]
        return cur.isWord or len(cur.chars) > 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
