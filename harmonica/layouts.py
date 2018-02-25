"""
Harmonica layouts tuned to harmonic minor scales
"""
import tunings as tn

major_diatonic_C = [
    'C4',
    'Db4',
    'D4',

    'E4',
    'G4',
    'Gb4',
    'F4',

    'G4',
    'B4',
    'Bb4',
    'A4',
    'Ab4',

    'C5',
    'D5',
    'Db5',

    'E5',
    'F5',

    'G5',
    'A5',
    'Ab5',

    'C6',
    'B5',

    'Eb6',
    'E6',
    'D6',

    'Gb6',
    'G6',
    'F6',

    'Bb6',
    'B6',
    'C7',
    'A6']

harmonic_minor_C = [
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
        'B4',
        'C5',
        'Db5',
        'D5',
        'Eb5',
        'E5',
        'F5',
        'G5',
        'Ab5',
        'B5',
        'C6',
        'D6',
        'Eb6',
        'F6',
        'G6',
        'Ab6',
        'C7']


harmonicas = {
    'major_diatonic': {major_diatonic_C[t]: [tn.transpose(note, t)
                                             for note in major_diatonic_C]
                       for t in range(12)},
    'harmonic_minor': {harmonic_minor_C[t]: [tn.transpose(note, t)
                                             for note in harmonic_minor_C]
                       for t in range(12)}
    }
