import json
import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Try to extract from our previous python script output logic
projects = []
# Use a regex that matches the current structure or fallback to known projects
# Since we know the projects, we can hardcode them to be safe and ensure all 11 are there.
hardcoded_projects = [
    {"title": "Blend", "desc": "Treasury-as-a-service for fintechs using private multi-currency accounts and robust yield instruments.", "link_url": "https://blend.money/", "link_text": "Visit Blend \u2014>", "logo": "<img src=\"https://framerusercontent.com/images/oJ7QVYoyXBbQ4HvAmIeq5U7AGpo.png\" alt=\"Blend\">"},
    {"title": "Vend", "desc": "Infrastructure for autonomous commerce. Self-financing machines powered by revenue-based credit.", "link_url": "https://vend.money/", "link_text": "Visit Vend \u2014>", "logo": "<img src=\"https://framerusercontent.com/images/SARuWkuMvBKRbeQeXHS7HCejxQw.png\" alt=\"Vend\">"},
    {"title": "Sedona", "desc": "Your neobank. Your keys.", "link_url": "https://sedona.fi/", "link_text": "Explore Sedona \u2014>", "logo": "<img src=\"https://sedona.fi/images/sedona-logo.svg\" alt=\"Sedona\">"},
    {"title": "Brookwell", "desc": "Private stablecoin cash accounts. Earn DeFi yields while securely paying rent and payroll via normal channels.", "link_url": "https://www.brookwell.com/", "link_text": "View Brookwell \u2014>", "logo": "<img src=\"https://www.brookwell.com/_next/image?url=%2Flogo.png&w=1080&q=75\" alt=\"Brookwell\">"},
    {"title": "Cred Protocol", "desc": "Private credit & working capital. Underwriting and lending for real-world businesses with zero data leaks.", "link_url": "https://credprotocol.com/", "link_text": "Explore Cred \u2014>", "logo": "<img src=\"https://framerusercontent.com/images/ly6CYDZguctn369Fter3suQOhA.png\" alt=\"Cred\">"},
    {"title": "Specie", "desc": "Modern banking for global businesses. Send, receive, and manage money worldwide with fast settlement across local and global rails.", "link_url": "https://www.specie.finance/", "link_text": "Explore Specie \u2014>", "logo": "<img src=\"https://framerusercontent.com/images/UgeAlOHZZ3FQwYhs7gAADiyTsio.svg\" alt=\"Specie\">"},
    {"title": "Via", "desc": "Stablecoin-first finance. Borderless access to capital, seamless payments, and premium yield.", "link_url": "https://www.via.xyz/", "link_text": "Explore Via \u2014>", "logo": "<img src=\"https://framerusercontent.com/images/kztSbCmi83eGOrsXWs2bnEqc.png\" alt=\"Via\">"},
    {"title": "Shift", "desc": "The Membership That Pays You Back. Elite financial services, lifestyle privileges, and exclusive perks driven by real yield models.", "link_url": "https://www.shift-apply.com/", "link_text": "Visit Shift \u2014>", "logo": "<img src=\"https://framerusercontent.com/images/H4Yn2rDLeq2wENXWMdowmAbKZs.png\" alt=\"Shift\">"},
    {"title": "DashX", "desc": "Cross-border payments powered by crypto. Accept USDC, track transactions, and withdraw INR globally through one unified stack.", "link_url": "https://dashx.xyz/", "link_text": "Use DashX \u2014>", "logo": "<img src=\"https://framerusercontent.com/images/le7rHwmt4MoWogPPDnWwvEQo1sA.png\" alt=\"DashX\">"}
]

globe_html = f"""
    <!-- Section 2: Ecosystem 3D Animated Globe -->
    <section class="ecosystem-section" id="ecosystem" style="padding: 120px 0; background: #000000; overflow: hidden; position: relative;">
        <div class="section-header" style="position: relative; z-index: 10; text-align: center;">
            <h2 style="color: #fff; font-size: 52px; margin-bottom: 16px;">Ecosystem Network</h2>
            <p style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px; margin: 0 auto;">Building the foundation for private, scalable financial services.</p>
        </div>
        
        <style>
            .globe-layout {{
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 60px;
                max-width: 1400px;
                margin: 0 auto;
                padding: 40px 20px;
            }}
            
            .globe-wrapper {{
                position: relative;
                width: 600px;
                height: 600px;
                perspective: 1200px;
                flex-shrink: 0;
            }}
            
            .globe-core {{
                position: absolute;
                top: 50%; left: 50%;
                transform: translate(-50%, -50%);
                width: 320px; height: 320px;
                border-radius: 50%;
                background: radial-gradient(circle at 30% 30%, #451B6E, #150824);
                box-shadow: 0 0 100px rgba(69, 27, 110, 0.9), inset -20px -20px 40px rgba(0,0,0,0.8);
                z-index: 5;
            }}
            
            .globe-grid {{
                position: absolute;
                top: 0; left: 0; width: 100%; height: 100%;
                border-radius: 50%;
                transform-style: preserve-3d;
                animation: spin-globe 25s linear infinite;
                z-index: 6;
            }}
            
            .globe-meridian {{
                position: absolute;
                top: 15%; left: 15%; width: 70%; height: 70%;
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 50%;
            }}
            .globe-meridian:nth-child(1) {{ transform: rotateY(0deg); }}
            .globe-meridian:nth-child(2) {{ transform: rotateY(45deg); }}
            .globe-meridian:nth-child(3) {{ transform: rotateY(90deg); }}
            .globe-meridian:nth-child(4) {{ transform: rotateY(135deg); }}
            
            .globe-equator {{
                position: absolute;
                top: 15%; left: 15%; width: 70%; height: 70%;
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 50%;
                transform: rotateX(90deg);
            }}

            @keyframes spin-globe {{
                0% {{ transform: rotateY(0deg) rotateX(15deg); }}
                100% {{ transform: rotateY(360deg) rotateX(15deg); }}
            }}
            
            .orbit-track {{
                position: absolute;
                top: 50%; left: 50%;
                border: 1px dashed rgba(208, 160, 181, 0.4);
                border-radius: 50%;
                transform-style: preserve-3d;
                z-index: 10;
            }}
            
            .orbit-node {{
                position: absolute;
                top: 50%; left: 50%;
                width: 64px; height: 64px;
                margin: -32px 0 0 -32px;
                background: rgba(255, 255, 255, 0.9);
                backdrop-filter: blur(10px);
                border-radius: 50%;
                box-shadow: 0 0 25px rgba(203, 33, 36, 0.6); /* Warm red glow */
                display: flex; align-items: center; justify-content: center;
                cursor: pointer;
                transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s;
                transform-style: preserve-3d;
            }}
            .orbit-node:hover, .orbit-node.active {{
                transform: scale(1.3) !important;
                box-shadow: 0 0 40px rgba(255, 238, 234, 0.8); /* Peach glow */
                z-index: 100;
            }}
            .orbit-node img, .orbit-node svg {{ max-width: 40px; max-height: 40px; object-fit: contain; border-radius: 8px; filter: brightness(0) saturate(100%); }}
            /* Make sure text logos or dark logos are visible: if they are black on white, keep them. The background is white. */
            .orbit-node img {{ filter: none; }}
            
            /* Info Panel */
            .globe-info-panel {{
                width: 400px;
                background: rgba(30, 11, 48, 0.6);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(208, 160, 181, 0.2);
                border-radius: 24px;
                padding: 40px;
                color: #fff;
                box-shadow: 0 30px 60px rgba(0,0,0,0.5);
                z-index: 20;
                transform: translateY(0);
                transition: opacity 0.4s, transform 0.4s;
            }}
            .globe-info-panel.morphing {{
                opacity: 0;
                transform: translateY(20px);
            }}
            .globe-info-panel-logo {{ height: 60px; margin-bottom: 24px; background: #fff; border-radius: 12px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; min-width: 60px; }}
            .globe-info-panel-logo img, .globe-info-panel-logo svg {{ max-height: 100%; max-width: 120px; }}
            .globe-info-panel h3 {{ font-family: 'Syne', sans-serif; font-size: 32px; margin-bottom: 16px; background: linear-gradient(90deg, #FFEEEA, #D0A0B5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .globe-info-panel p {{ font-size: 16px; line-height: 1.6; color: rgba(255,255,255,0.7); margin-bottom: 30px; }}
            .globe-info-panel a {{ background: linear-gradient(90deg, #451B6E, #CB2124); color: #fff; padding: 14px 32px; border-radius: 100px; text-decoration: none; font-weight: 700; display: inline-block; transition: transform 0.3s, box-shadow 0.3s; }}
            .globe-info-panel a:hover {{ transform: translateY(-3px); box-shadow: 0 10px 20px rgba(203, 33, 36, 0.4); }}
            
            @media (max-width: 1024px) {{
                .globe-layout {{ flex-direction: column; gap: 20px; }}
                .globe-wrapper {{ width: 350px; height: 350px; }}
                .globe-core {{ width: 180px; height: 180px; }}
                .orbit-node {{ width: 44px; height: 44px; margin: -22px 0 0 -22px; }}
                .orbit-node img, .orbit-node svg {{ max-width: 28px; max-height: 28px; }}
                .globe-info-panel {{ width: 100%; max-width: 400px; padding: 30px; }}
            }}
        </style>
        
        <div class="globe-layout">
            <div class="globe-wrapper" id="globeWrapper">
                <div class="globe-core"></div>
                <div class="globe-grid">
                    <div class="globe-meridian"></div>
                    <div class="globe-meridian"></div>
                    <div class="globe-meridian"></div>
                    <div class="globe-meridian"></div>
                    <div class="globe-equator"></div>
                </div>
                
                <!-- Track 1: Inner Orbit -->
                <div class="orbit-track" id="track1" style="width: 450px; height: 450px; margin: -225px 0 0 -225px;"></div>
                
                <!-- Track 2: Outer Orbit -->
                <div class="orbit-track" id="track2" style="width: 650px; height: 650px; margin: -325px 0 0 -325px;"></div>
            </div>
            
            <div class="globe-info-panel" id="globeInfoPanel"></div>
        </div>
        
        <script>
            const globeProjects = {json.dumps(hardcoded_projects)};
            const track1 = document.getElementById('track1');
            const track2 = document.getElementById('track2');
            const panel = document.getElementById('globeInfoPanel');
            
            const isMob = window.innerWidth <= 1024;
            const r1 = isMob ? 130 : 225;
            const r2 = isMob ? 180 : 325;
            
            track1.style.width = (r1*2) + 'px';
            track1.style.height = (r1*2) + 'px';
            track1.style.margin = (-r1) + 'px 0 0 ' + (-r1) + 'px';
            
            track2.style.width = (r2*2) + 'px';
            track2.style.height = (r2*2) + 'px';
            track2.style.margin = (-r2) + 'px 0 0 ' + (-r2) + 'px';
            
            // Split projects
            const p1 = globeProjects.slice(0, 4);
            const p2 = globeProjects.slice(4);
            
            let nodes = [];
            
            function createNodes(projectList, track, radius, speed, reverse) {{
                projectList.forEach((proj, i) => {{
                    const node = document.createElement('div');
                    node.className = 'orbit-node';
                    node.innerHTML = proj.logo;
                    
                    const angleOffset = (i / projectList.length) * Math.PI * 2;
                    
                    node.addEventListener('mouseenter', () => {{
                        nodes.forEach(n => n.classList.remove('active'));
                        node.classList.add('active');
                        updatePanel(proj);
                    }});
                    
                    // We will animate them using requestAnimationFrame for perfect 3D orbiting
                    nodes.push({{ el: node, angle: angleOffset, radius: radius, track: track, speed: speed, reverse: reverse, proj: proj }});
                    track.appendChild(node);
                }});
            }}
            
            createNodes(p1, track1, r1, 0.003, false);
            createNodes(p2, track2, r2, 0.002, true);
            
            // 3D Orbital math
            // We want tracks to be tilted.
            const tiltX = 65; // degrees
            track1.style.transform = `rotateX(${{tiltX}}deg)`;
            track2.style.transform = `rotateX(${{tiltX}}deg) rotateY(15deg)`;
            
            let time = 0;
            function animateOrbit() {{
                time += 1;
                nodes.forEach(n => {{
                    const currentAngle = n.angle + (time * n.speed * (n.reverse ? -1 : 1));
                    const x = Math.cos(currentAngle) * n.radius;
                    const y = Math.sin(currentAngle) * n.radius;
                    
                    // Apply translation on the track plane, then counter-rotate the node so it stays flat to screen
                    // The track is rotated X by tiltX. So to un-rotate the node:
                    const unRotateX = -tiltX;
                    const unRotateY = n.track === track2 ? -15 : 0;
                    
                    n.el.style.transform = `translate(${{x + n.radius}}px, ${{y + n.radius}}px) rotateX(${{unRotateX}}deg) rotateY(${{unRotateY}}deg)`;
                }});
                requestAnimationFrame(animateOrbit);
            }}
            animateOrbit();
            
            let currentTitle = null;
            function updatePanel(proj) {{
                if(currentTitle === proj.title) return;
                currentTitle = proj.title;
                
                panel.classList.add('morphing');
                setTimeout(() => {{
                    panel.innerHTML = `
                        <div class="globe-info-panel-logo">${{proj.logo}}</div>
                        <h3>${{proj.title}}</h3>
                        <p>${{proj.desc}}</p>
                        <a href="${{proj.link_url}}" target="_blank">${{proj.link_text}}</a>
                    `;
                    panel.classList.remove('morphing');
                }}, 300);
            }}
            
            if(globeProjects.length > 0) {{
                updatePanel(globeProjects[0]);
                nodes[0].el.classList.add('active');
            }}
        </script>
"""

# Replace the previous section
sec_start = content.find('<section class="ecosystem-section" id="ecosystem"')
sec_end = content.find('</section>', sec_start) + len('</section>')

new_content = content[:sec_start] + globe_html + content[sec_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("3D Globe Ecosystem UI injected!")
