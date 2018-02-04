"""
Harmonica layouts tuned to harmonic minor scales
"""
import tunings as tn

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

harmonic_minors = {harmonic_minor_C[t]: [tn.transpose(note, t)
                                         for note in harmonic_minor_C]
                   for t in range(12)}
