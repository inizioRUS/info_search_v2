class Document:
    def __init__(self, title, text, id, stem):
        self.title = title
        self.text = text
        self.id = id
        self.stem_form = stem

    def format(self):
        return [self.title, self.text[:min(100, len(self.text) - 1)] + ' ...']