def filter_broken(links: list):
    return [l for l in links if l.get('status') == 'BROKEN']
