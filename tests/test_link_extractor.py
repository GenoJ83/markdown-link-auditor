from src.parsers.regex_extractor import extract_links
def test_extract():
    doc = 'Check [Google](https://google.com) and [Docs](./docs.md)'
    links = extract_links(doc)
    assert len(links) == 2
    assert links[0]['url'] == 'https://google.com'
