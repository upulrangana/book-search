class SearchResult(object):
    def __init__(self, index, score, body):
        self.index = index
        self.score = score
        self.body = body
