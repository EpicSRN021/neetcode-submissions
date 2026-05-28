class Node():
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        def helper(curr, word, i):
            if len(word) == i+1:
                if word[i] in curr.children or word[i] == ".":
                    if word[i] == ".":
                        for c in curr.children:
                            if curr.children[c].end == True:
                                return True
                        return False
                    if not curr.children[word[i]].end:
                        return False
                    return True
            if word[i] not in curr.children and word[i] != ".":
                return False
            if (word[i] == "."):
                for c in curr.children:
                    if helper(curr.children[c], word, i+1) == True:
                        return True
                return False
            return helper(curr.children[word[i]], word, i+1)     
        return helper(curr, word, 0)


        
