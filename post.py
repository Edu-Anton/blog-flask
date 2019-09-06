class Post(object):
    def __init__(self, id, title, description, url):
        self._id = id
        self.title = title
        self.description = description
        self.url = url