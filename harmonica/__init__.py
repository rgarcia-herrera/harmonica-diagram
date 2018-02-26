from jinja2 import Environment, PackageLoader

import layouts

env = Environment(
    loader=PackageLoader('harmonica')
)


class Harp:

    def __init__(self, key="C4", layout="major_diatonic"):
        self.key = key

        self.notes = layouts.harmonicas[layout][key]

        self.template = env.get_template('%s_C.svg' % layout)

    def draw(self, path):
        with open(path, 'w') as out:
            out.write(self.template.render(self.notes,
                                           key=self.key))

    def mark_in_scale(self, scale):
        for note in self.notes:
            if self.notes[note] in scale:
                self.notes[note] = "(%s)" % self.notes[note]
