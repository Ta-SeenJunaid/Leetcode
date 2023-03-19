from typing import Optional


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        return self.dfs_helper(0, self.root, word)

    def dfs_helper(self, index: int, root: Optional[TrieNode], word:str):
        if index == len(word):
            return root.end_of_word
        if word[index] == ".":
            for child in root.children.values():
                if self.dfs_helper(index+1, child, word):
                    return True
        if word[index] in root.children:
            return self.dfs_helper(index+1, root.children[word[index]], word)
        return False

