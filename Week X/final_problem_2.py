import random

def quote(filename):
    try:
        fh = open(filename)
        quotes = fh.readlines()
        fh.close()
        return random.choice(quotes)

    except:
        return 'Invalid file'

print(quote('quotes.txt'))
