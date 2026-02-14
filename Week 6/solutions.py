import week5solutions as w5

def item_freq(l2d):
    '''returns dict of frequency in 2d list'''
    freq = {}
    for sublist in l2d:
        for element in sublist:
            freq.setdefault(element, 0)
            freq[element] += 1
    return freq

def duplicates(filename):
    '''returns True if filename has duplicate words'''
    freq = w5.word_freq(filename)
    for count in freq.values():
        if count != 1:
            return True
    return False

def lookup(d):
    '''takes user input and looks up phone numbers'''
    while True:
        first_name = input("Enter a first name: ")
        last_name = input("Enter a last name: ")
        if first_name == '' and last_name == '':
            break
        key = (first_name, last_name)
        number = d.get(key, "Unlisted number")
        print(number)

def unique_words(filename):
    '''returns alphabetical list of unique words in file'''
    words = w5._get_words(filename)
    words = set(words)
    words = list(words)
    words.sort()
    return words

def unique_items(l2d):
    '''returns sorted list of unique items in 2d list'''
    unique = set()
    for i in range(len(l2d)):
        for j in range(len(l2d[i])):
            unique.add(l2d[i][j])
    unique = list(unique)
    unique.sort()
    return unique

def set_duplicates(filename):
    '''returns True if filename has duplicate words'''
    words = w5._get_words(filename)
    unique = set()
    for word in words:
        if word not in unique:
            unique.add(word)
        else:
            return True
    return False

def countdown(n):
    #base case
    if n == 0:
        print("Blast off!")
    #recursive case
    else:
        print(n)
        countdown(n - 1)

def vertical(n):
    #base case
    if n < 10:
        print(n)
    #recursive case
    else:
        print(n % 10)
        vertical(n // 10)

def print_list(l):
    #base_case
    if len(l) == 1:
        print(l[0])
    #recursive case
    else:
        print(l[0])
        print_list(l[1:])

def cheer(n):
    #base case
    if n == 1:
        print("Hurray!")
    #recursive case
    else:
        print("Hip")
        cheer(n - 1)

def make_cheer(n):
    if n == 1:
        return "Hurray!"
    else:
        s = make_cheer(n - 1)
        return "Hip " + s












    
    
