from jinja2 import Environment, PackageLoader
import tunings
import layouts

env = Environment(
    loader=PackageLoader('harmonica')
)


class Harp:

    def __init__(self, key="C4", layout="major_diatonic"):
        self.key = key

        transport_interval_size = tunings.distance('C4', self.key)

        self.notes = {n: tunings.all_notes[tunings.all_notes.index(n)
                                           + transport_interval_size]
                      for n in layouts.harmonicas[layout][key]}

        self.template = env.get_template('%s_C.svg' % layout)

    def draw(self, path):
        with open(path, 'w') as out:
            out.write(self.template.render(self.notes))

    def mark_in_scale(self, scale):
        for note in self.notes:
            if self.notes[note] in scale:
                self.notes[note] = "(%s)" % self.notes[note]
