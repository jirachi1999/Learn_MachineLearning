import json


class FileReader(object):
    def __init__(self, file_path, encoder='utf-16'):
        self.file_path = file_path
        self.encoder = encoder

    def read(self):
        with open(self.file_path, 'rb') as f:
            s = f.read()
        return s

    def content(self):
        s = self.read()
        return s.decode(self.encoder)

    # def read_json(self):
    #     with open(self.filePath) as f:
    #         s = json.load(f)
    #     return s
    #
    # def read_stopwords(self):
    #     with open(self.filePath, 'r') as f:
    #         stopwords = set([w.strip().replace(' ', '_') for w in f.readlines()])
    #     return stopwords
    #
    # def load_dictionary(self):
    #     return corpora.Dictionary.load_from_text(self.filePath)
