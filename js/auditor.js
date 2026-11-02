function extractLinks(markdown) {
  const regex = /\[([^\]]+)\]\(([^\)]+)\)/g;
  const links = [];
  let m;
  while ((m = regex.exec(markdown)) !== null) {
    links.push({ text: m[1], url: m[2] });
  }
  return links;
}
function slugifyHeading(heading) {
  return heading.toLowerCase().replace(/[^\w\s-]/g, '').trim().replace(/\s+/g, '-');
}
module.exports = { extractLinks, slugifyHeading };
