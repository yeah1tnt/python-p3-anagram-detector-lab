class Anagram:
    def __init__(self, word):
        self.wordSorted = sorted(i for i in word)

    def match(self, anagram):
        list = []
        for i in anagram:
            if sorted(j for j in i) == self.wordSorted:
                list.append(i)
        return list