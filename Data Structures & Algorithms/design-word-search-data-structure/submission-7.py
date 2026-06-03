class WordDictionary:

    def __init__(self):
        self.d = {}
        

    def addWord(self, word: str) -> None:
        d = self.d
        for c in word:
            if c not in d:
                d[c] = {}

            d = d[c]
        d["\\."] = "\\."

    def search(self, word: str) -> bool:
        d = self.d

        def sr(word, d):
            for i, c in enumerate(word):
                if c == ".":
                    for key in d:
                        if key == "\\.":
                            continue
                        if sr(word[i+1:], d[key]):
                            return True
                    return False

                if c not in d:
                    return False
                    
                d = d[c]

            if "\\." in d:
                return True
            return False
        
        return sr(word, d)