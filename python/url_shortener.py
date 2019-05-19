'''
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric
    string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url.
    If no such shortened string exists, return null.
    Hint: What if we enter the same URL twice?
'''


class UrlShortener:
    def __init__(self):
        self.urls = {}
        self.lowers = ''.join([chr(x) for x in range(97, 123)])
        self.uppers = self.lowers.upper()
        self.nums = ''.join([str(x) for x in range(10)])

    def shorten(self, url):
        pass
