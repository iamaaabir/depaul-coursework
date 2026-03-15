def sorted_unique():
    lst = []
    duplicates = []
    while True:
        try:
            str_user = input('Enter a whole number or hit enter to stop: ')

            if str_user == '':
                break

            user = int(str_user)

            if user not in duplicates:
                lst.append(user)
                duplicates.append(user)
            else:
                pass

        except:
            print(f'I am sorry but {str_user} is not a whole number.')

    lst.sort()

    return lst

print(sorted_unique())


