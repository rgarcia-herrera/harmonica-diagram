from harmonica import layouts
from harmonica import scales
import harmonica


def jaccard_index(first, *others):
    """ Computes jaccard index """
    return float(len(first.intersection(*others))) \
        / float(len(first.union(*others)))


for grade in scales.arabic_harmonicas:
    print 'D4', grade, jaccard_index(set(layouts.harmonic_minors['D4']),
                                     set(scales.arabic_harmonicas[grade]))
    h = harmonica.Harp('D4')
    h.mark_in_scale(scales.arabic_harmonicas[grade])
    h.draw('arabic_%s_Dhm_harp.svg' % grade)
