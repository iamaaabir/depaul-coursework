def safe_open():
    '''safely opens a file'''

    while True:
        filename = input('Please enter a file name: ')
        try:
            fh = open(filename, 'r')
            return fh
        except:
            print(filename + '  could not be opened.')

inf = safe_open()
print(inf.readline())
