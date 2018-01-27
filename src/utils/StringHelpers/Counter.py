class Counter(object):

    def sanitizeDict(self,dictionary):
        sanitizedDict = {}
        for key in dictionary:
            if dictionary[key] > 1:
                sanitizedDict[key] = dictionary[key]

        return sanitizedDict

    def countMembers(self,_str,inc = " ", zIndex = False, sanitize = False):
        word_list = _str.split(inc)
        word_count = {}

        for word in word_list:
            if word_count.get(word) == None:
                if zIndex: word_count[word] = 1
                else: word_count[word] == 0
            else:
                word_count[word] += 1

        if sanitize == True:
            word_count = self.sanitizeDict(word_count)    

        return word_count
            
