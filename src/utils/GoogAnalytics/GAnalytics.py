import requests
from bs4 import BeautifulSoup as BS

class GAnalyticsHelper(object):

    def __init__(self):
        self.root = "https://trends.google.com/trends/explore?q={subject}"

    def grabPageHTML(self,_subject):
        query = self.root.format(subject = _subject)
        resp = requests.get(query)
        return resp.content

    def buildSoup(self, _html_string):
        self.soup = BS(_html_string)

    def scrapeTrendChart(self):
        searchTerm = "path"
