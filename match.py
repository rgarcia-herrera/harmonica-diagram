from harmonica.layouts import harmonicas
from harmonica import scales
import harmonica


def jaccard_index(first, *others):
    """ Computes jaccard index """
    return float(len(first.intersection(*others))) \
        / float(len(first.union(*others)))


for grade in scales.arabic_harmonicas:
    print 'C4', grade, jaccard_index(set(harmonicas['major_diatonic']['C4']),
                                     set(scales.arabic_harmonicas[grade]))

    h = harmonica.Harp(key='C4', layout='major_diatonic')

    h.mark_in_scale(scales.arabic_harmonicas[grade])

    h.draw('arabic_%s_major_diatonic_harp.svg' % grade)
