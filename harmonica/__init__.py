from jinja2 import Environment, PackageLoader
import tunings
import layouts

env = Environment(
    loader=PackageLoader('harmonica')
)


class Harp:

    def __init__(self, key="C4"):
        self.key = key

        transport_interval_size = tunings.distance('C4', self.key)

        self.notes = {n: tunings.notes[tunings.notes.index(n)
                                       + transport_interval_size]
                      for n in layouts.harmonic_minor_C}

        self.template = env.get_template('harmonic_minor_C.svg')

    def draw(self, path):
        with open(path, 'w') as out:
            out.write(self.template.render(self.notes))

    def mark_in_scale(self, scale):
        for note in self.notes:
            if self.notes[note] in scale:
                self.notes[note] = "(%s)" % self.notes[note]