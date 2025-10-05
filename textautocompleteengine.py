import heapq
from trie import Trie

class TextAutocompleteEngine:
    def __init__(self, words, freq_dist=None):
        self.trie = Trie()
        if freq_dist is None:
            self.freq = {}
        else:
            self.freq = freq_dist
        for word in words:
            self.trie.insert(word.lower())

    def get_suggestions(self, prefix: str, max_suggestions: int = 5) -> list[str]:
        words = self.trie.autocomplete(prefix.lower())
        top_frequency = []
        for word in words:
            freq = self.freq.get(word, 0)
            heapq.heappush(top_frequency, (-freq, word))
        suggestions = [heapq.heappop(top_frequency)[1] for _ in range(min(max_suggestions, len(top_frequency)))]
        return suggestions