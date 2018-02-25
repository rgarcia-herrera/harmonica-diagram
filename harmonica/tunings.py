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

all_notes = []
for o in range(-2, 9):
    for n in range(0, 12):
        all_notes.append("%s%s" % (note_symbol[n], o))


def transpose(note, interval):
    return all_notes[all_notes.index(note) + interval]


def distance(n1, n2):
    return all_notes.index(n2) - all_notes.index(n1)
