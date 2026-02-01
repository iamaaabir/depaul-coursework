def guess(n):
    ''' random number guessing game '''

    import random
    random_number = random.randint(1, n)

    while True:

        str_guess = input('Enter your guess: ')

        try:
            guess = int(str_guess)
            if guess < 1 or guess > n:
                print('That was not a valid number')
            elif guess == random_number:
                print('You got it!')
                break
            elif guess > random_number:
                print('Too high')
            else:
                print('Too low')

        except ValueError:
            print('That was not a valid number')

guess(100)