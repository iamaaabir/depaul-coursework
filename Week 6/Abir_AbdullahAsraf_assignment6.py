# Problem 1

def create_catalog():
    '''Creates and returns a dictionary of authors and their books.'''

    book_dict = {}

    while True:
        first_name = input('Enter author\'s first name: ')
        last_name = input('Enter author\'s last name: ')
        book_title = input('Enter book title: ')

        if first_name == '' or last_name == '' or book_title == '':
            break

        key = (first_name, last_name)

        book_dict.setdefault(key, [])
        book_dict[key].append(book_title)

    return book_dict

# Problem 2

def checkout(available_books, to_checkout):
    '''Checks out the book if available and returns the status and updated set.'''
    if to_checkout in available_books:
        # Personal note: using the difference method to remove checkout items. Could've alternatively used available_books.remove(to_checkout)
        updated_books = available_books - {to_checkout}
        return (True, updated_books)
    else:
        return (False, available_books)

# Problem 3

def set_due_date(book, tracking_system):
    '''Assigns a due date to a book and returns updated tracking.'''

    due_date = (2024, 11, 1)
    tracking_system[book] = due_date
    return tracking_system

# Problem 4

def find_popular_authors(catalog):
    '''Returns a set containing name of popular authors having 2 or more books.'''

    popular_author_names = set()

    for k,v in catalog.items():
        if len(v) > 1:
            author_first_name = k[0]
            author_last_name = k[1]
            author_full_name = k[0] + ' ' + k[1]
            popular_author_names.add(author_full_name)

    return popular_author_names


def create_catalog():
    '''Creates and returns a dictionary of authors and their books.'''

    book_dict = {}

    while True:
        first_name = input('Enter author\'s first name: ')
        last_name = input('Enter author\'s last name: ')
        book_title = input('Enter book title: ')

        if first_name == '' or last_name == '' or book_title == '':
            break

        key = (first_name, last_name)

        book_dict.setdefault(key, [])
        book_dict[key].append(book_title)

    return book_dict
