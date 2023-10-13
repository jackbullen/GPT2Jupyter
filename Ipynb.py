import json

class Ipynb:
    def __init__(self, path):
        self.path = path
        with open(path, 'r') as f:
            self.content = json.loads(f.read())
        self.cells = self.content['cells']

    def add_cell(self, cell):
        self.cells.append(cell)
        self.save()

    def save(self):
        with open(self.path, 'r') as f:
            saved = json.loads(f.read())

        saved['cells'] = self.cells

        with open(self.path, 'w') as f:
            f.write(json.dumps(saved))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name