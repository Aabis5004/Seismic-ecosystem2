import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_old = ".eco-list { max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 40px; padding: 0 24px; }"
css_new = """
        .eco-carousel-wrapper {
            width: 100vw;
            overflow: hidden;
            position: relative;
            padding: 20px 0 80px;
        }
        
        /* Fade edges for slick look */
        .eco-carousel-wrapper::before,
        .eco-carousel-wrapper::after {
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            width: 15vw;
            z-index: 10;
            pointer-events: none;
        }
        .eco-carousel-wrapper::before {
            left: 0;
            background: linear-gradient(to right, #f8fafc, transparent);
        }
        .eco-carousel-wrapper::after {
            right: 0;
            background: linear-gradient(to left, #f8fafc, transparent);
        }

        .eco-list {
            display: flex;
            gap: 40px;
            width: max-content;
            animation: ecoMarquee 50s linear infinite;
            padding: 20px 40px;
        }

        .eco-list:hover {
            animation-play-state: paused;
        }

        @keyframes ecoMarquee {
            0% { transform: translateX(0); }
            100% { transform: translateX(calc(-50% - 20px)); }
        }
"""
content = content.replace(css_old, css_new)

# Make the cards fixed width
card_css = ".eco-list-item {"
card_css_new = ".eco-list-item {\n            width: 500px;\n            flex-shrink: 0;"
content = content.replace(card_css, card_css_new)

# 2. Duplicate the projects to make the infinite scroll seamless
list_start = content.find('<div class="eco-list">')
list_end = content.find('</section>', list_start)
list_content = content[list_start:list_end]

# Find the inner items
items_match = re.search(r'<div class="eco-list">(.*?)</div>\s*</section>', list_content, re.DOTALL)
if items_match:
    inner_html = items_match.group(1)
    # Duplicate inner HTML
    new_inner = inner_html + "\n            <!-- DUPLICATED FOR INFINITE SCROLL -->\n" + inner_html
    new_list_content = '<div class="eco-carousel-wrapper">\n        <div class="eco-list">' + new_inner + '</div>\n        </div>\n    '
    content = content[:list_start] + new_list_content + content[list_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html with horizontal animated carousel!")
