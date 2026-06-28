import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the first block of eco-list items
start = content.find('<div class="eco-list">')
end = content.find('<!-- DUPLICATED FOR INFINITE SCROLL -->')
if end == -1:
    end = content.find('</section>', start)

html_list = content[start:end]

projects = []
items = re.findall(r'<div class="eco-list-item">(.*?)</div>\s*</div>\s*(?=<!--|<div class="eco-list-item"|</section>)', html_list, re.DOTALL)
for item in items:
    # logo
    logo_match = re.search(r'<div class="eco-logo-box".*?>(.*?)</div>\s*<div class="eco-content">', item, re.DOTALL)
    logo = logo_match.group(1).strip() if logo_match else ""
    
    # title
    title_match = re.search(r'<h3>(.*?)</h3>', item)
    title = title_match.group(1).strip() if title_match else ""
    
    # desc
    desc_match = re.search(r'<p>(.*?)</p>', item)
    desc = desc_match.group(1).strip() if desc_match else ""
    
    # link
    link_match = re.search(r'<a href="(.*?)".*?>(.*?)</a>', item)
    link_url = link_match.group(1).strip() if link_match else ""
    link_text = link_match.group(2).strip() if link_match else ""
    
    if title:
        projects.append({
            'title': title,
            'desc': desc,
            'link_url': link_url,
            'link_text': link_text,
            'logo': logo
        })

print(json.dumps(projects, indent=2))
