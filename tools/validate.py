"""Validate local pages, metadata, JSON-LD, sitemap, links and fragments. Standard library only."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json, re, sys, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'https://www.whychooseme.me'
class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags=[]; self.ids=[]; self.schemas=[]; self.schema=None; self.title=''; self.in_title=False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if 'id' in a: self.ids.append(a['id'])
        if tag=='title': self.in_title=True
        if tag=='script' and a.get('type')=='application/ld+json': self.schema=''
    def handle_endtag(self, tag):
        if tag=='title': self.in_title=False
        if tag=='script' and self.schema is not None:
            self.schemas.append(json.loads(self.schema)); self.schema=None
    def handle_data(self, text):
        if self.in_title: self.title+=text
        if self.schema is not None: self.schema+=text

def canonical(path):
    rel=path.relative_to(ROOT).as_posix()
    return DOMAIN+('/' if rel=='index.html' else '/'+rel.replace('index.html','').removesuffix('.html'))
def resolve(path, ref):
    parsed=urlsplit(ref); value=unquote(parsed.path)
    dest=ROOT / value.lstrip('/') if value.startswith('/') else path.parent / value
    if not value: dest=path
    dest=dest.resolve()
    if dest.is_dir(): dest=dest/'index.html'
    elif not dest.exists() and not dest.suffix: dest=dest.with_suffix('.html')
    return dest, parsed.fragment

errors=[]; docs={}; local_links=0; titles=[]; descriptions=[]
for path in ROOT.rglob('*.html'):
    try: docs[path.resolve()]=Document(path.read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f'{path.name}: HTML/JSON-LD parse error {exc}')
for path,doc in docs.items():
    rel=path.relative_to(ROOT).as_posix()
    def require(condition, message):
        if not condition: errors.append(rel+': '+message)
    tags=doc.tags
    require(len([1 for t,a in tags if t=='h1'])==1,'expected one H1')
    require(len(doc.ids)==len(set(doc.ids)),'duplicate IDs')
    require(any(t=='html' and a.get('lang')=='en-US' for t,a in tags),'missing English lang')
    require(any(t=='meta' and a.get('name')=='viewport' for t,a in tags),'missing viewport')
    require(any(t=='main' for t,a in tags),'missing main')
    require(any(t=='link' and a.get('rel')=='canonical' and a.get('href')==canonical(path) for t,a in tags),'incorrect canonical')
    desc=[a.get('content','') for t,a in tags if t=='meta' and a.get('name')=='description']
    require(len(desc)==1 and bool(desc[0]),'missing or duplicate description')
    titles.append(doc.title); descriptions.extend(desc)
    for prop in ['og:title','og:description','og:url','og:image']:
        require(any(t=='meta' and a.get('property')==prop for t,a in tags),f'missing {prop}')
    for t,a in tags:
        if t=='meta' and a.get('property')=='og:image':
            require(a.get('content','').startswith(DOMAIN+'/'),'OG image uses another domain')
            require((ROOT/urlsplit(a.get('content','')).path.lstrip('/')).is_file(),'missing OG image asset')
    if rel.startswith('guides/') and path.name!='index.html':
        require(any(s.get('@type')=='Article' for s in doc.schemas),'missing Article schema')
        require(any(t=='nav' and a.get('aria-label')=='On this page' for t,a in tags),'missing article contents')
    for tag,a in tags:
        if tag=='img': require(all(k in a for k in ['alt','width','height']),'image lacks alt or dimensions')
        for attr in ['href','src']:
            if attr not in a: continue
            parsed=urlsplit(a[attr])
            if parsed.scheme or parsed.netloc: continue
            local_links+=1; dest,fragment=resolve(path,a[attr])
            require(dest.is_relative_to(ROOT),'link escapes root')
            require(dest.is_file(),'missing resource '+a[attr])
            if fragment and dest in docs: require(fragment in docs[dest].ids,'missing fragment '+a[attr])
    require(not any(t=='form' for t,a in tags),'unexpected form')
require_titles=len(titles)==len(set(titles))
if not require_titles: errors.append('Duplicate titles')
if len(descriptions)!=len(set(descriptions)): errors.append('Duplicate descriptions')
xml=ET.parse(ROOT/'sitemap.xml')
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
locations=[el.text for el in xml.findall('s:url/s:loc',ns)]
expected={canonical(p) for p in docs if p.name!='404.html'}
if set(locations)!=expected or len(locations)!=len(expected): errors.append('Sitemap does not match all canonical pages')
if f'Sitemap: {DOMAIN}/sitemap.xml' not in (ROOT/'robots.txt').read_text(): errors.append('Incorrect robots sitemap')
article_count=sum(1 for p in docs if p.parent.name=='guides' and p.name!='index.html')
if article_count!=10: errors.append('Expected ten articles')
patterns=[r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'gh[pousr]_[A-Za-z0-9]{30,}',r'AKIA[A-Z0-9]{16}',r'(?i)(?:api_key|password|client_secret)\s*[:=]\s*[\"\'][^\"\']{8,}']
suspects=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or '.git' in p.parts or p.suffix not in {'.html','.js','.css','.md','.txt','.json','.xml'}: continue
    text=p.read_text(encoding='utf-8')
    if '\ufffd' in text: errors.append(p.name+': replacement character')
    if any(re.search(pattern,text) for pattern in patterns): suspects.append(p.relative_to(ROOT).as_posix())
if suspects: errors.append('Potential sensitive files (values redacted): '+', '.join(suspects))
report={'passed':not errors,'html_pages':len(docs),'articles':article_count,'local_references_checked':local_links,'sitemap_urls':len(locations),'unique_titles':require_titles,'potential_secret_files':suspects,'errors':errors}
print(json.dumps(report,indent=2))
sys.exit(0 if not errors else 1)
