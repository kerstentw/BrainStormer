import Counter

class BagOfWords(Counter):
    def buildVectors(self,_str):
        self.countMembers(_str, zIndex = True, sanitize = False)
