from src.parsers.anchor_extractor import extract_anchors
def test_anchors():
    doc = '# Introduction\n## Getting Started'
    a = extract_anchors(doc)
    assert 'introduction' in a
    assert 'getting-started' in a
