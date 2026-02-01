# Problem 1

def balances(lst):
    """Returns total donations and expenditures from a list."""

    new_list = []
    sum_positive = 0.0
    sum_negative = 0.0

    if len(lst) == 0:
        return [0.0, 0.0]

    for element in lst:
        if element > 0:
            sum_positive += element
        if element < 0:
            sum_negative += element

    new_list.append(sum_positive)
    new_list.append(sum_negative)

    return new_list

# Problem 2

def isalphabetical(lst):
    """Returns true if the list of string is in alphabetical order."""

    if len(lst) <= 1:
        return True

    for i in range(1, len(lst)):
        if lst[i - 1].lower() > lst[i].lower():
            return False

    return True

# Problem 3

def get_indices(sensor, stimulus):
    """Returns a list of indices where the stimulus (target) matches with the sensor"""

    lst = []

    if sensor == '' or stimulus == '':
        return []

    for i in range(len(sensor)):
        if sensor[i] in stimulus:
            lst.append(i)

    return lst

# Problem 4

def find_sub_strs(lst):
    """Returns a list of strings that are substrings of the previous element"""

    result = []

    if len(lst) == 0:
        return []

    for i in range(1, len(lst)):
        if lst[i] in lst[i - 1]:
            result.append(lst[i])

    return result

# Problem 5

def multi_sum(multilist):
    """Returns the sum of integers and floats in a list and avoids strings"""

    if len(multilist) == 0:
        return 0

    total = 0
    for i in range(len(multilist)):
        for j in range(len(multilist[i])):
            if isinstance(multilist[i][j], (int, float)):
                total += multilist[i][j]

    return total










