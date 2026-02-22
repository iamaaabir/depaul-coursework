import os

def digisum(num):
    '''returns the sum of the digits of num'''
    #Base case
    if num < 10:
        return num
    #recursive case
    else:
        temp = digisum(num // 10)
    return temp + (num % 10)

def ispalindrome(word):
    '''returns True if word is a palindrome'''
    #Base case
    if len(word) <= 1:
        return True
    #recursive case
    else:
        if word[0] != word[-1]:
            return False
        temp = ispalindrome(word[1:-1])
        return temp

def print_list(l):
    '''prints each element in a list'''
    if len(l) > 0:
        #base_case
        if type(l[0]) != list:
            print(l[0])
        #recursive case
        else:
            print_list(l[0])
        print_list(l[1:])

def count_ints(l):
    '''returns the number of integers in arbitrarily nested lists'''
    if len(l) == 0:
        return 0
    else:
        if type(l[0]) == int:
            temp = count_ints(l[1:])
            return 1 + temp
        elif type(l[0]) == list:
            temp = count_ints(l[0])
            temp1 = count_ints(l[1:])
            return temp + temp1
        else:
            return count_ints(l[1:])

def find_max(l):
    '''returns the max element of nested lists'''
    if len(l) == 0:
        return 0
    if len(l) == 1 and type(l[0]) != list:
        return l[0]
    if type(l[0]) == int or type(l[0]) is float:
        temp = find_max(l[1:])
        if l[0] > temp:
            return l[0]
        else:
            return temp
    else:
        temp = find_max(l[0])
        temp1 = find_max(l[1:])
        if temp > temp1:
            return temp
        else:
            return temp1

def count_files(path):
    '''count the number of files in directory or subdirectories'''
    try:
        count = 0
        for item in os.listdir(path):
            if item[0] == '.':
                continue
            name = os.path.join(path, item)
            #base case
            if not os.path.isdir(name):
                count += 1
            #recursive
            else:
                count += count_files(name)
        return count
    except:
        return 0

def search(filename, path):
    '''searches path for filename, returns path if found, None if not'''
    try:
        return_path = None
        for item in os.listdir(path):
            if item[0] == '.':
                continue
            path_to_item = os.path.join(path, item)
            if item.lower() == filename.lower():
                #base case
                return_path = path_to_item
                break
            elif not os.path.isdir(path_to_item):
                #base case
                continue
            else:
                #recursive case
                return_path = search(filename, path_to_item)
        return return_path
    except:
        return None


def fib(n):
    '''returns nth fibonacci number'''
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)



        
