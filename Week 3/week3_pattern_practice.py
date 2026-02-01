def pattern_1(num):
    for r in range(num):
        for c in range(num):
            print(c, end=' ')   # For a star pattern, replace c with '*'
        print()


# Passing 5 to print 5 rows and 5 cols of numbers 0 through 4.
pattern_1(5)
print('Once again, but different')
pattern_1(10)

print()
print('Printing pattern 2 now')


def pattern_2(num):
    for i in range(num):
        for j in range(i+1):
            print(j, end=' ')   # For a star pattern, replace j with '*'
        print()


pattern_2(5)
print('Once again, but different')
pattern_2(10)
