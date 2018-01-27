from string_lib.function_words import function_words
from string_lib.punctuation import punctuation

class Sanitizer(object):
    def __init__(self):
        self.function_words = function_words

    def pullFunctionWords(self, _str):
        processed_str = " ".join([word for word in _str.lower().split(" ") 
                                  if word not in self.function_words])
        return processed_str

    def pullPunctuation(self,_str):
        processed_str = " ".join([_str.replace(punc,"") for punc in punctuation])

        return processed_str
