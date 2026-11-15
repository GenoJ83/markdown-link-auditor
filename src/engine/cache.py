class UrlCache:
    _cache = {}
    @classmethod
    def get(cls, url): return cls._cache.get(url)
    @classmethod
    def set(cls, url, status): cls._cache[url] = status
