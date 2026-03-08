from urllib.request import urlopen
from html.parser import HTMLParser
from urllib.parse import urljoin

#url = 'http://facweb.cdm.depaul.edu/asettle/web/test.html'
#html = urlopen(url).read().decode()

class MyHtmlParser(HTMLParser):
    '''basic html parser'''

    def handle_starttag(self, tag, attrs):
        '''prints tags'''
        print(f"Encountered starting {tag} tag, with {len(attrs)} attributes")

    def handle_endtag(self, tag):
        '''prints end tag'''
        print(f"Encountered ending {tag} tag")


class ParserPracticeBase(HTMLParser):
    '''adds url handling capability to HTMLParser'''

    def parse(self, url):
        '''open URL and feed contents to HTMLParser'''
        html = urlopen(url).read().decode()
        self.feed(html)


class AttributesParser(ParserPracticeBase):
    '''parses attributes into key-value pairs'''

    def handle_starttag(self, tag, attrs):
        '''print attributes for <a> tags'''
        if tag == 'a':
            print(attrs)

class LinksParser(ParserPracticeBase):
    '''prints links to screen'''

    def handle_starttag(self, tag, attrs):
        '''prints href values to screen'''
        if tag == 'a':
            #for tup in attrs:
             #   if tup[0] == 'href':
              #      print(tup[1])
            for name, link in attrs:
                if name == 'href':
                    print(link)
                    
class PrettyParser(ParserPracticeBase):
    '''pretty prints html'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.indent = 0

    def handle_starttag(self, tag, attrs):
        '''prints start tag at correct indent level'''
        if tag not in ('img', 'br', 'hr'):
            print(self.indent * ' ' + tag)
            self.indent += 4
    
    def handle_endtag(self, tag):
        '''prints end tag at correct indent level'''
        self.indent -= 4
        print(self.indent * ' ' + tag)

class DataCollector(ParserPracticeBase):
    '''create string of inner data'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.data = ''

    def handle_data(self, data):
        '''collects data into string'''
        self.data += data

    def get_data(self):
        '''return data collected from html'''
        return self.data

class HeaderParser(ParserPracticeBase):
    '''create list of header data'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.headerflag = False
        self.headerlist = []

    def handle_starttag(self, tag, attrs):
        '''set the header flag'''
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headerflag = True

    def handle_endtag(self, tag):
        '''unset the header flag'''
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headerflag = False

    def handle_data(self, data):
        '''add only header data to the list'''
        if self.headerflag == True:
            self.headerlist.append(data)

    def get_list(self):
        '''returns the header data list'''
        return self.headerlist

class ListParser(ParserPracticeBase):
    '''create a list of list items'''
    
    def __init__(self):
        '''constructor'''
        super().__init__()
        self.flag = False
        self.li_list = []

    def handle_starttag(self, tag, attrs):
        '''set flag when li tag is encountered'''
        if tag == 'li':
            self.flag = True

    def handle_endtag(self, tag):
        '''unsets flag when li end tag encountered'''
        if tag == 'li':
            self.flag = False

    def handle_data(self, data):
        '''add data for li tags to list'''
        if self.flag == True:
            self.li_list.append(data)

    def set_list(self, lst):
        '''sets self.list'''
        self.li_list = lst

    def get_list(self):
        '''returns self.list'''
        return self.li_list

class Collector(HTMLParser):
    '''collect HTTP links'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.linklist = []
        self.url = ''

    def parse(self, url):
        '''run the parser'''
        self.url = url
        html = urlopen(url).read().decode()
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        '''adds absolute URLs to linklist'''
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    absolute = urljoin(self.url, value)
                    if absolute[:4] == 'http':
                        self.linklist.append(absolute)

    def get_links(self):
        '''returns links'''
        return self.linklist


class Crawler:

    def __init__(self):
        self.visitedlist = []
        
    def crawl(self, url):
        '''recursive web crawler that calls analyze() on each web page'''
        if url not in self.visitedlist:
            self.visitedlist.append(url)
        links = self.analyze(url)
        for link in links:
            if link not in self.visitedlist:
                try:
                    self.visitedlist.append(link)
                    self.crawl(link)
                except:
                    pass

    def analyze(self, url):
        '''returns the list of URLs found in the page url'''
        print("Visiting", url)
        collector = Collector()
        collector.parse(url)
        urls = collector.get_links()
        return urls



    


            
