def num_larger(filename, val):
    fh = open(filename, 'r')

    for line in fh:
        nums = line.split()
        for n in nums:
            n = float(n)
            if n > val:
                return n
    return val

print(num_larger('nums.txt', 0))
print(num_larger('nums.txt', 10))
print(num_larger('nums.txt', 13))
print(num_larger('nums.txt', 14.5))
