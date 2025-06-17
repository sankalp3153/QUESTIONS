class Codec:

    def __init__(self):
        self.url_map = {}
        self.id = 0
        self.prefix = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        short_url = self.prefix + str(self.id)
        self.url_map[short_url] = longUrl
        self.id += 1
        return short_url

    def decode(self, shortUrl: str) -> str:
        return self.url_map[shortUrl]
