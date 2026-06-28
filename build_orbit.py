import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract projects
list_start = content.find('<div class="eco-carousel-wrapper">')
if list_start == -1:
    list_start = content.find('<div class="eco-list">')

list_end = content.find('</section>', list_start)
html_list = content[list_start:list_end]

projects = []
# Ensure we only extract from the original list (not the duplicated one if we can help it)
# We can just use a set to avoid duplicates
seen_titles = set()

items = re.findall(r'<div class="eco-list-item">(.*?)</div>\s*</div>\s*(?=<!--|<div class="eco-list-item"|</section>|</div>\s*</div>)', html_list, re.DOTALL)
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
    
    if title and title not in seen_titles:
        seen_titles.add(title)
        projects.append({
            'title': title,
            'desc': desc,
            'link_url': link_url,
            'link_text': link_text,
            'logo': logo
        })

# Edge case: If regex failed for some reason, we'll need to manually parse or fallback, but it should work.

orbit_html = f"""
    <!-- Section 2: Ecosystem Orbit -->
    <section class="ecosystem-section" id="ecosystem" style="padding: 120px 0; background: #f8fafc; overflow: hidden; position: relative;">
        <div class="section-header" style="position: relative; z-index: 10;">
            <h2>Ecosystem Partners</h2>
            <p>Building the foundation for private, scalable financial services.</p>
        </div>
        
        <style>
            .orbit-wrapper {{ position: relative; width: 700px; height: 700px; margin: 60px auto; border-radius: 50%; z-index: 5; }}
            
            .orbit-ring {{
                position: absolute; top: 50%; left: 50%; width: 100%; height: 100%;
                transform: translate(-50%, -50%);
                border: 1.5px dashed rgba(82, 53, 66, 0.15);
                border-radius: 50%;
                animation: orbitSpin 60s linear infinite;
            }}
            .orbit-ring:hover {{ animation-play-state: paused; }}
            
            .orbit-node {{
                position: absolute;
                width: 80px; height: 80px;
                margin: -40px 0 0 -40px;
                background: #ffffff;
                border-radius: 50%;
                box-shadow: 0 10px 25px rgba(82, 53, 66, 0.08);
                display: flex; align-items: center; justify-content: center;
                cursor: pointer;
                transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s, background 0.4s;
                animation: orbitSpinReverse 60s linear infinite;
                padding: 16px;
            }}
            
            .orbit-ring:hover .orbit-node {{ animation-play-state: paused; }}
            
            .orbit-node:hover, .orbit-node.active {{
                transform: scale(1.25) !important;
                box-shadow: 0 20px 40px rgba(82, 53, 66, 0.15);
                background: #fff;
                z-index: 10;
                border: 2px solid var(--plum);
            }}
            
            .orbit-node img, .orbit-node svg {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
            
            @keyframes orbitSpin {{ 100% {{ transform: translate(-50%, -50%) rotate(360deg); }} }}
            @keyframes orbitSpinReverse {{ 100% {{ transform: rotate(-360deg); }} }}
            
            .orbit-center {{
                position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                width: 360px; height: 360px;
                background: rgba(255, 255, 255, 0.85);
                backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
                border-radius: 50%;
                box-shadow: 0 30px 60px rgba(82, 53, 66, 0.12), inset 0 0 0 1px rgba(255,255,255,0.8);
                display: flex; flex-direction: column; align-items: center; justify-content: center;
                text-align: center; padding: 40px;
                transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
                z-index: 10;
            }}
            
            .orbit-center.morphing {{
                transform: translate(-50%, -50%) scale(0.92);
                opacity: 0.3;
                filter: blur(6px);
            }}
            
            .orbit-center-logo {{ height: 50px; margin-bottom: 24px; display: flex; align-items: center; justify-content: center; }}
            .orbit-center-logo img, .orbit-center-logo svg {{ max-height: 100%; max-width: 140px; }}
            
            .orbit-center h3 {{ font-family: 'Syne', sans-serif; font-size: 26px; color: var(--plum); margin-bottom: 12px; letter-spacing: -0.5px; }}
            .orbit-center p {{ font-size: 15px; color: var(--text-secondary); line-height: 1.6; margin-bottom: 24px; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }}
            .orbit-center a {{ background: var(--plum); color: #fff; padding: 12px 28px; border-radius: 100px; text-decoration: none; font-weight: 600; font-size: 14px; transition: transform 0.3s, box-shadow 0.3s; }}
            .orbit-center a:hover {{ transform: translateY(-2px); box-shadow: 0 10px 20px rgba(82,53,66,0.15); }}
            
            @media (max-width: 768px) {{
                .orbit-wrapper {{ width: 340px; height: 340px; margin: 40px auto; }}
                .orbit-center {{ width: 240px; height: 240px; padding: 20px; }}
                .orbit-center h3 {{ font-size: 20px; margin-bottom: 8px; }}
                .orbit-center p {{ font-size: 13px; margin-bottom: 16px; -webkit-line-clamp: 2; }}
                .orbit-center-logo {{ height: 35px; margin-bottom: 16px; }}
                .orbit-center a {{ padding: 8px 20px; font-size: 12px; }}
                .orbit-node {{ width: 56px; height: 56px; margin: -28px 0 0 -28px; padding: 10px; }}
            }}
        </style>
        
        <div class="orbit-wrapper">
            <div class="orbit-ring" id="orbitRing"></div>
            <div class="orbit-center" id="orbitCenter"></div>
        </div>
        
        <script>
            const projects = {json.dumps(projects)};
            const ring = document.getElementById('orbitRing');
            const center = document.getElementById('orbitCenter');
            const total = projects.length;
            
            // Generate nodes
            projects.forEach((proj, index) => {{
                const angle = (index / total) * Math.PI * 2;
                const leftPct = 50 + (Math.cos(angle) * 50);
                const topPct = 50 + (Math.sin(angle) * 50);
                
                const node = document.createElement('div');
                node.className = 'orbit-node';
                node.style.left = leftPct + '%';
                node.style.top = topPct + '%';
                node.innerHTML = proj.logo;
                
                node.addEventListener('mouseenter', () => {{
                    document.querySelectorAll('.orbit-node').forEach(n => n.classList.remove('active'));
                    node.classList.add('active');
                    updateCenter(proj);
                }});
                
                ring.appendChild(node);
            }});
            
            let currentActive = null;
            
            function updateCenter(proj) {{
                if (currentActive === proj.title) return;
                currentActive = proj.title;
                
                center.classList.add('morphing');
                setTimeout(() => {{
                    center.innerHTML = `
                        <div class="orbit-center-logo">${{proj.logo}}</div>
                        <h3>${{proj.title}}</h3>
                        <p>${{proj.desc}}</p>
                        <a href="${{proj.link_url}}" target="_blank">${{proj.link_text}}</a>
                    `;
                    center.classList.remove('morphing');
                }}, 250);
            }}
            
            // Initialize first project
            if(projects.length > 0) {{
                ring.firstChild.classList.add('active');
                updateCenter(projects[0]);
            }}
        </script>
"""

# Now replace the old section
# Make sure to handle <section class="ecosystem-section" id="ecosystem">
sec_start = content.find('<section class="ecosystem-section" id="ecosystem">')
sec_end = content.find('</section>', sec_start) + len('</section>')

new_content = content[:sec_start] + orbit_html + content[sec_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Orbit UI built and deployed!")
