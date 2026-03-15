from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser

class ParserPracticeBase(HTMLParser):
    '''adds url handling capability to HTMLParser'''

    def parse(self, url):
        '''open URL and feed contents to HTMLParser'''
        html = urlopen(url).read().decode()
        self.feed(html)

class OrderedListParser(ParserPracticeBase):
    '''gets contents of ordered list items'''

    def __init__(self):
        super().__init__()
        self.li_data = []
        self.liflag = False
        self.olflag = False

    def get_items(self):
        return self.li_data

    def set_items(self, lst):
        self.li_data = lst

    def handle_starttag(self, tag, attrs):
        if tag == 'ol':
            self.olflag = True
        elif tag == 'li':
            self.liflag = True

    def handle_endtag(self, tag):
        if tag == 'ol':
            self.olflag = False
        elif tag == 'li':
            self.liflag = False

    def handle_data(self, data):
        if self.olflag and self.liflag:
            self.li_data.append(data)