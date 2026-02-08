import random

def dice_sim():
    '''six-sided die simulator'''
    stats = [0,0,0,0,0,0,0]
    total_rolls = 0
    #take user input
    user_input = input("Would you like to roll a die? (y/n): ")
    while True:
    #check for flags
        if user_input == 'y':
            #roll die
            roll = random.randint(1, 6)
            print(roll)
            #capture stats
            stats[roll] += 1
            total_rolls += 1
        elif user_input == 'n':
            #print stats
            print(f'''Roll statistics:
Total rolls: {total_rolls}
Frequencies:
1: {stats[1]}
2: {stats[2]}
3: {stats[3]}
4: {stats[4]}
5: {stats[5]}
6: {stats[6]}''')
            #terminate
            break
        else:
            #error message
            print("Sorry, I didn't get that. Please entter 'y' or 'n'")
        user_input = input("Roll again? (y/n): ")

def copy_dict(d1):
    '''creates a new copy of d1'''
    d2 = {}
    for k, v in d1.items():
        d2[k] = v
    return d2

def inverse(d1):
    '''invert key-value pairs'''
    d2 = {}
    old_keys = d1.keys()
    for k in old_keys:
        d2[d1[k]] = k
    return d2

def word_freq(filename):
    '''count frequency of words in file'''
    #get words out of file
    words = _get_words(filename)
    #build a dictionary
    freq = {}
    for word in words:
        #word doesn't exist, add it
        if word not in freq:
            freq[word] = 1
        #word already exists, update it
        else:
            freq[word] += 1
    return freq

def _get_words(filename):
    '''returns a list of words in filename, punctuation removed'''
    try:
        infile = open(filename, 'r')
        contents = infile.read()
        contents = contents.lower()
        contents = _remove_targets(contents, '.,;:?!')
        words = contents.split()
        return words
    except:
        print(f'Error opening {filename}')
        return []

def _remove_targets(content, targets):
    '''removes targets from content'''
    for char in targets:
        content = content.replace(char, ' ')
    return content




