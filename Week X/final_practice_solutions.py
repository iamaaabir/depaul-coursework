import random
from html.parser import HTMLParser
from urllib.request import urlopen

def sorted_unique():
    '''returns sorted list of unique numbers'''
    user_in = input('Enter a whole number or hit enter to stop: ')
    unique_ints = set()
    while user_in != '':
        try:
            in_int = int(user_in)
            unique_ints.add(in_int)
        except:
            print(f"I'm sorry but {user_in} is not an integer.")
        user_in = input('Enter a whole number or hit enter to stop: ')
    int_list = list(unique_ints)
    int_list.sort()
    return int_list

def quotes(filename):
    '''opens filename and returns random line'''
    infile = open(filename)
    lines = infile.readlines()
    infile.close()
    numlines = len(lines)
    if numlines == 0:
        return 'invalid file'
    randint = random.randint(0, numlines-1)
    return lines[randint]

def make_noisy(table, numchanges):
    '''adds random noise to table'''
    while numchanges > 0:
        rowindex = random.randint(0, len(table) - 1)
        row = table[rowindex]
        columnindex = random.randint(0, len(row) - 1)
        row[columnindex] = random.randint(0, 255)
        numchanges -= 1

def unique_values(d):
    '''returns unique values from dict'''
    unique_vals = set()
    for val in d.values():
        try:
            unique_vals.add(val)
        except:
            continue
    return unique_vals

class Stat:
    '''statistical information class'''

    def __init__(self, user_list=[]):
        '''constructor'''
        self.nums = user_list

    def __contains__(self, num):
        return self.nums.count(num) > 0

    def __len__(self):
        return len(self.nums)

    def __add__(self, other):
        newlist = self.sum(lst) + other.sum(lst)
        return Stat(newlist)

    def add(self, num):
        self.nums.append(num)

    def clear(self):
        self.nums.clear()

    def min(self):
        try:
            return min(self.nums)
        except:
            pass

    def max(self):
        try:
            return max(self.nums)
        except:
            pass

    def sum(self):
        accum = 0
        for num in self.nums:
            accum += num
        return accum

    def mean(self):
        if len(self) == 0:
            return 0.0
        else:
            return self.sum() / len(self)

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











