class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.end_word = ""