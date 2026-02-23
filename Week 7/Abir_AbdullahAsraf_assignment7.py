# Problem 1

def create_countdown(seconds):
    '''Counts the number of seconds from highest down to 0.'''

    if seconds <= 0:
        return

    print(seconds)

    if seconds == 1:
        print(0)
        return

    create_countdown(seconds - 1)

# Problem 2

def hourglass(base):
    '''Prints a star pattern of hourglass of specified width.'''

    hourglass_helper(base, base)

def hourglass_helper(base, current_level):
    '''Helper function for hourglass which is used recursively'''

    print(('*' * current_level).center(base))

    if current_level <= 2:
        print(('*' * current_level).center(base))
        return

    hourglass_helper(base, current_level - 2)

    print(('*' * current_level).center(base))

# Problem 3

def progress_bar(completion_percent):
    '''Returns a progress bar of 10 spaces which gets occupied based on the completion percent'''

    hashmarks = completion_percent // 10
    inside = progress_bar_recursive(hashmarks, 0)
    return '[' + inside + ']'

def progress_bar_recursive(hashmarks, counter):
    '''Helper function for the progress bar which is used recursively.'''

    if counter == 10:
        return ''

    if counter < hashmarks:
        return '#' + progress_bar_recursive(hashmarks, counter + 1)
    else:
        return ' ' + progress_bar_recursive(hashmarks, counter + 1)

# Problem 4

import os

def num_occurrences(filename, path):
    '''Returns the number of times the specified file occurs in a directory.'''

    if not os.path.exists(path):
        return 0

    total = 0

    for item in os.listdir(path):

        if item[0] == '.':
            continue

        full_path = os.path.join(path, item)

        if not os.path.isdir(full_path):
            if item == filename:
                total += 1
        else:
            total += num_occurrences(filename, full_path)

    return total






