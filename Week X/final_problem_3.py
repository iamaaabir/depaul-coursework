import random

def make_noisy(table, num_changes):
    if len(table) == 0 or num_changes <= 0:
        return

    for i in range(num_changes):
        row = random.randrange(0, len(table))
        col = random.randrange(0, len(table[row]))
        table[row][col] = random.randint(0, 255)


