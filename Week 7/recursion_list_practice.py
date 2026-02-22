# Problem 1 (Working with 1D lists):

def print_list(lst):
    if len(lst) == 1:
        print(lst[0])
    else:
        print(lst[0])
        print_list(lst[1:])

print_list([1, 2, 3])

# ------> 2D LISTS AND RECURSIONS <------ #

# Problem 2:

def print_list(lst):
    
    if len(lst) > 0:
        
        if type(lst[0]) != list:
            print(lst[0])
        else:
            print_list(lst[0])
            
        print_list(lst[1:])
            
print_list([[[1, [2], [3], [[[4]]]], [5], [[6, 7], 8]], 9])

# Problem 3:

def count_ints(lst):
    
    total = 0 
    if len(lst) == 0:
        return 0
    elif type(lst[0]) == int:
        total += 1
    else:
        count_ints(lst[0])
    
    count_ints(lst[1:])
    
    return total
    
print(count_ints([1, 2, 3.5, 'test', 9.1, 10]))
print(count_ints([3.5, [[[[1]]], 2], 'five', [[[3, [4, 6]]]]]))

# Problem 4:

def find_max(lst):
    
    highest = 0 
    
    if len(lst) > 0:
        
        if type(lst[0]) != list:
            if lst[0] > highest:
                highest = lst[0]
        else:
            highest = find_max(lst[0])
            
        rest_highest = find_max(lst[1:])
        
        if rest_highest > highest:
            highest = rest_highest
    
    return highest
        
    
print(find_max([1, 2, 3.5, 100, 9.1, 10]))
print(find_max([3.5, [[[[10]]], 2], 5, [[[3, [4, 6]]]]]))















