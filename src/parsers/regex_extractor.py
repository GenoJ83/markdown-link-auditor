import re
LINK_REGEX = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
def extract_links(markdown_text: str, filename: str = ''):
    results = []
    for line_idx, line in enumerate(markdown_text.splitlines(), 1):
        for m in LINK_REGEX.finditer(line):
            url = m.group(2)
            results.append({'file': filename, 'line': line_idx, 'text': m.group(1), 'url': url})
    return results
