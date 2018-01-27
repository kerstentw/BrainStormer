import requests
import config
import json

import sys
sys.path.append("..") #import utils
from StringHelpers import Counter

#https://newsapi.org/v2/everything?q=bitcoin&apiKey=ec1567dd377044ebb0897251e4001566

class NewsApiHandler(object):
    def __init__(self):
        self.host = "https://newsapi.org/v2/"
        self.apiKey = config.api_key        
        self.header = {"x-api-key":self.apiKey}
        self.Counter = Counter.Counter()

    def getEverything(self,_subject):
        option = "everything?q={_sub}"
        query = self.host + option.format(_sub = _subject)
        
        resp = requests.get(query,headers = self.header)
        newsDict = json.loads(resp.content)
        newsDict["len"] = len(newsDict["articles"])
        return newsDict


    def getSubjectBreakdown(self,_subject,_sanitize = True):
        infoDict = dict()
        newsDict = self.getEverything(_subject)
        infoDict["number_of_stories"] = newsDict["len"]
        maximumString = " ".join([ article["title"] + " " + article["description"] for article in newsDict["articles"]])
        infoDict["word_count"] = self.Counter.countMembers(maximumString, sanitize = _sanitize)
        
        return infoDict


    def changeKey(self, _new_key):
        self.apiKey = _new_key
        return True
