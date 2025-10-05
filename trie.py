from trienode import TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.end_word = word

    def wordSearch(self, node: TrieNode, words: list) -> list[str]:
        if node.is_end:
            words.append(node.end_word)
        for child in node.children.values():
            self.wordSearch(child, words)
        return words

    def prefixSearch(self, prefix: str) -> TrieNode | None:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def autocomplete(self, prefix: str) -> list[str]:
        node = self.prefixSearch(prefix)
        if not node:
            return []
        return self.wordSearch(node, [])