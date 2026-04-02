import re

def extract(file):
    try:
        with open(file, encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Failed to read {file}: {e}")
        return
        
    print(f"\n--- {file} ---")
    imgs = re.findall(r'<img[^>]*src=[\"\']([^\'\"]+)[\"\'][^>]*>', content)
    for i in imgs:
        if 'logo' in i.lower() or 'brand' in i.lower() or 'icon' in i.lower() or '.svg' in i.lower() or 'asset' in i.lower():
            print('IMG SRC:', i)
            
    svgs = re.findall(r'<svg[^>]*>.*?</svg>', content, re.DOTALL)
    for i, s in enumerate(svgs):
        if 'logo' in s.lower() or 'Shift' in s or 'Promis' in s:
            print(f"Found SVG {i}:", s[:200], '...')
        
extract('www.shift-apply.com.html')
extract('www.promis.fi.html')
