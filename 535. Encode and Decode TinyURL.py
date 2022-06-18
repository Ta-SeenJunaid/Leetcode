# https://www.youtube.com/watch?v=VyBOaboQLGc
class Codec:
    def __init__(self):
        self.base = "http://tinyurl.com/"
        self.encode_map = {}
        self.decode_map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_map:
            short_url = self.base + str(len(self.encode_map) + 1)
            self.encode_map[longUrl] = short_url
            self.decode_map[short_url] = longUrl
        return self.encode_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[shortUrl]


codec = Codec()
print(codec.decode(codec.encode(longUrl = "https://leetcode.com/problems/design-tinyurl")))