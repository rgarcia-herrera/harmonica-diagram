from harmonica.layouts import harmonicas
from harmonica import scales
import harmonica


def jaccard_index(first, *others):
    """ Computes jaccard index """
    return float(len(first.intersection(*others))) \
        / float(len(first.union(*others)))


harmonic_minor_harps = ['G4', 'Ab4', 'A4',
                        'Bb4', 'C4', 'Db4',
                        'D4', 'Eb4', 'E4',
                        'F4', 'Gb4']

major_diatonics = ['G4', 'Ab4', 'A4',
                   'Bb4', 'B4', 'C4', 'Db4',
                   'D4', 'Eb4', 'E4', 'F4',
                   'Gb4']

for grade_harp in major_diatonics:
    for grade_scale in scales.chromatic4:
        print grade_harp, grade_scale,\
            jaccard_index(
                set(harmonicas['major_diatonic'][grade_harp].values()),
                set(scales.blues_harmonicas[grade_scale]))

        h = harmonica.Harp(key=grade_harp, layout='major_diatonic')

        h.mark_in_scale(scales.blues_harmonicas[grade_scale])

        h.draw('diagrams/%s_blues_in_major_diatonic_%s_harp.svg'
               % (grade_scale,
                  grade_harp))
