import tunings as tn

chromatic4 = [
    'C4',
    'Db4',
    'D4',
    'Eb4',
    'E4',
    'F4',
    'Gb4',
    'G4',
    'Ab4',
    'A4',
    'Bb4',
    'B4']


arabic_harmonica = [
    'C4',
    'Db4',
    'E4',
    'F4',
    'G4',
    'Ab4',
    'B4',
    'C5',
    'Db5',
    'E5',
    'F5',
    'G5',
    'Ab5',
    'B5',
    'C6',
    'Db6',
    'E6',
    'F6',
    'G6',
    'Ab6',
    'B6',
    'C7'
]

arabic_harmonicas = {chromatic4[t]: [tn.transpose(note, t)
                                     for note in arabic_harmonica]
                     for t in range(12)}
