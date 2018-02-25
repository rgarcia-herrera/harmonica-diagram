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

blues_harmonica = [
    'C4', 'Eb4', 'F4', 'Gb4', 'G4', 'Bb4',
    'C5', 'Eb5', 'F5', 'Gb5', 'G5', 'Bb5',
    'C6', 'Eb6', 'F6', 'Gb6', 'G6', 'Bb6',
    'C7'
]

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

blues_harmonicas = {chromatic4[t]: [tn.transpose(note, t)
                                     for note in blues_harmonica]
                     for t in range(12)}
