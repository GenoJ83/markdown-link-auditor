def batch_urls(urls, size=20):
    for i in range(0, len(urls), size): yield urls[i:i+size]
