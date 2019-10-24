class Matural_File:

    def get_contents(self):
        with open(self.path) as f:
            return f.read().splitlines()

    def __init__(self, path):
        self.path = path
        self.file_obj = open(path)
        self.contents = self.get_contents()

    def generate_from_content(self, function):
        for i in self.contents:
            yield function(i)
