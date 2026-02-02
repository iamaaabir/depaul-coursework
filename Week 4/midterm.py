# Problem 1:

def is_even(n):
    if n % 2 == 0:
        return True
    return False

str_n = input('Enter an integer: ')
try:
    n = int(str_n)
    print(is_even(n))
except ValueError:
    print('Please enter a valid integer.')

# Problem 2:

print()
def sum_digits(s):
    total = 0
    for i in s:
        str_i = int(i)
        total+=str_i

    return total

print(sum_digits('123'))
print(sum_digits('007'))

# Problem 3:

print()
def print_table():
    for i in range(1, 6):
        for j in range(1, 6):
            print(i * j, end = '\t')
        print()

print_table()

# Problem 4:

print()
def count_lines(filename):
    fh = open(filename, 'r')

    count = 0
    for line in fh:
        count += 1

    fh.close()
    return count

print(count_lines('writing.txt'))

# Problem 5:

print()
import random
def guess_game():
    generated_num = random.randint(1, 10)

    i = 0
    while i < 3:
        try:
            user_guess = input('Guess a number: ')
            int_user_guess = int(user_guess)
            i += 1
            if int_user_guess == generated_num:
                print('Correct!')
                break
            if int_user_guess != generated_num:
                print('Try again!')
        except ValueError:
            print('Not a valid number. Please enter integers only.')

    print(f'Game over! The correct number was: {generated_num} ')

guess_game()

