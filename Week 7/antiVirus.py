import os

rules={'Stuxnet':'iyfp9fg394g539gf',
       'SamyWorm':'9f8g8408h3498hff'}

def scan(pathname, signatures):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''
    for item in os.listdir(pathname):
        if item[0] == '.':
            continue
        name = os.path.join(pathname, item) # any OS
        if not os.path.isdir(name):
            # base case: exception means that item is a file
            f = open(name, 'r')
            s = f.read()
            for virus in signatures:
                if s.find(signatures[virus]) >= 0:
                    print(f'{name}, found virus {virus}')
            f.close()
        else:
            #recursive case
            scan(name, signatures)
