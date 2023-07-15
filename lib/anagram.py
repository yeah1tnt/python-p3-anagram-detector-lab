class Anagram:
    def __init__(self, word):
        self.wordSorted = sorted(i for i in word)

    def match(self, anagram):
        list = []
        for i in anagram:
            anagramSorted = sorted(j for j in i)
            if anagramSorted == self.wordSorted:
                list.append(i)
        return list