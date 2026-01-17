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

# Practice 4

def num_larger(filename, val):
    fh = open(filename, 'r')
    nums = []

    for line in fh:
        str_nums = line.split()

        for str_num in str_nums:
            nums.append(float(str_num))

        nums.sort()

        for n in nums:
            if n > val:
                return n
    return val

print(num_larger('nums.txt', 0))
print(num_larger('nums.txt', 10))
print(num_larger('nums.txt', 13))
print(num_larger('nums.txt', 14.5))







