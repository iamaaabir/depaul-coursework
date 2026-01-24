# Problem 1

def find_key_of_c(filename):

    fh = open(filename, 'r')
    c_melody = []

    for line in fh:

        line = line.strip()

        if line == '':
            continue

        chars = line.split()

        if chars[0] == 'C' and chars[-1] == 'C':
            c_melody.append(line)

    fh.close()
    return c_melody


# c_melodies = find_key_of_c('melodies.txt')
# print(c_melodies)

# c_melodies = find_key_of_c('melodies2.txt')
# print(c_melodies)

# c_melodies = find_key_of_c('empty.txt')
# print(c_melodies)

# Problem 2

def remove_low_notes(filename):

    fh = open(filename, 'r')
    high_notes = []

    line = fh.read()
    notes = line.split(',')

    for note in notes:

        note = note.strip()
        note = int(note)
        if note > 60 and note <= 120:
            high_notes.append(note)

    fh.close()
    return high_notes

# high_pitched_notes = remove_low_notes('midi.txt')
# print(high_pitched_notes)

# Problem 3

def separate_highs_lows(filename):

    fh = open(filename, 'r')
    fh2 = open('lows.txt', 'w')
    fh3 = open('highs.txt', 'w')

    line = fh.read()
    notes = line.split()

    for note in notes:
        note = note.strip()
        note = int(note)

        if note <= 60:
            print(note, file = fh2)
        else:
            print(note, file = fh3)

    fh.close()
    fh2.close()
    fh3.close()

# separate_highs_lows('composition.txt')

# Problem 4

def tempo_match(filename, tempo):

    fh = open(filename, 'r')
    songs = []
    lines = fh.readlines()

    if len(lines) == 0:
        fh.close()
        return ['empty']

    for line in lines:

        line = line.strip()
        word = line.split(',')

        song_name = word[0]
        song_tempo = int(word[1])

        if song_tempo == tempo:
            songs.append(song_name)

    if len(songs) == 0:
        fh.close()
        return ['no songs match']

    fh.close()
    return songs


# songs = tempo_match('samples_list.txt', 120)
# print(songs)
# songs = tempo_match('samples_list.txt', 95)
# print(songs)


