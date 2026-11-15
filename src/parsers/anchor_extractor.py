import re
HEADING_REGEX = re.compile(r'^#+\s+(.*)$')
def extract_anchors(markdown_text: str):
    anchors = set()
    for line in markdown_text.splitlines():
        m = HEADING_REGEX.match(line)
        if m:
            slug = m.group(1).lower().replace(' ', '-').replace('/', '')
            anchors.add(slug)
    return anchors
