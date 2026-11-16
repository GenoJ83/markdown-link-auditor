const { extractLinks, slugifyHeading } = require('../../js/auditor');

describe('Markdown Auditor', () => {
  it('extracts links from markdown text', () => {
    const text = 'Read [Docs](https://docs.com) and [Blog](./blog.md)';
    const links = extractLinks(text);
    expect(links.length).toBe(2);
    expect(links[0].url).toBe('https://docs.com');
  });
  it('slugifies heading strings', () => {
    expect(slugifyHeading('## Getting Started Guide!')).toBe('getting-started-guide');
  });
});
