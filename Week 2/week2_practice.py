# Practice 1

def num_lines(filename):

    fh = open(filename, 'r')

    count = 0
    for line in fh:
        count = count + 1

    return count

print(num_lines('example.txt'))

# Practice 2

def num_chars(filename):

    fh = open(filename, 'r')

    count = 0
    for line in fh:
        count = count + len(line)

    return count

print(num_chars('example.txt'))

# Practice 3

def string_count(filename, target):
    fh = open(filename, 'r')

    count = 0
    for line in fh:
        count += line.count(target)

    return count






