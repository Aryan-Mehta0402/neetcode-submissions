class PrefixTree:

    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        d = self.d
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d["."] = "."

    def search(self, word: str) -> bool:
        d = self.d
        for c in word:
            if c not in d:
                return False
            d = d[c]
        if "." in d:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        d = self.d
        for c in prefix:
            if c not in d:
                return False
            d = d[c]
        return True
        