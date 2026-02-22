# Using recursion to find the number of files.

import os

def count_files(pathname):
    '''recursively counts number of files in folder and subfolders'''
    
    total = 0
    
    for item in os.listdir(pathname):
        
        if item[0] == '.':
            continue
        
        name = os.path.join(pathname, item)
        
        if not os.path.isdir(name):
            # base case: it's a file
            total += 1
        
        else:
            # recursive case: it's a folder
            total += count_files(name)
    
    return total
    
# Using recursion to return the pathname of a specific file.

import os

def search(filename, pathname):
    '''recursively searches for filename in folder pathname'''
    
    for item in os.listdir(pathname):
        
        if item[0] == '.':
            continue
        
        name = os.path.join(pathname, item)
        
        # base case: item is file
        if not os.path.isdir(name):
            
            # case-insensitive comparison
            if item.lower() == filename.lower():
                return name
        
        # recursive case: item is folder
        else:
            
            result = search(filename, name)
            
            # if found inside subfolder
            if result is not None:
                return result
    
    # if not found anywhere
    return None