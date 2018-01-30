"""
exposes the array "notes"

notes.index('C4') -> 60
notes[60] -> 'C4'

"""

note_symbol = ['C', 'Db',
               'D', 'Eb',
               'E', 'F',
               'Gb', 'G',
               'Ab', 'A',
               'Bb', 'B', 'C']

notes = []
nota = 0
for o in range(-2, 9):
    for n in range(0, 12):
        notes.append("%s%s" % (note_symbol[n], o))
        nota += 1


def transpose(note, interval):
    return notes[notes.index(note) + interval]


def distance(n1, n2):
    return notes.index(n2) - notes.index(n1)
