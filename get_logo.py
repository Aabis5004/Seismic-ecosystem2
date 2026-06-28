import urllib.request, re
req = urllib.request.Request('https://sedona.fi/', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
for match in re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html):
    print(match)
