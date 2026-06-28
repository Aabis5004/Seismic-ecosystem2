import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS Variables & Body
new_vars = """
        :root {
            --bg-primary: #FFFFFF;
            --bg-secondary: #FFEEEA;
            --text-main: #451B6E;
            --text-secondary: #475569;
            --accent-red: #CB2124;
            --accent-pink: #D0A0B5;
            --glass-white: rgba(255,255,255,0.85);
            --shadow-soft: rgba(69, 27, 110, 0.08);
            --shadow-heavy: rgba(69, 27, 110, 0.15);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Inter', sans-serif; 
            background-color: var(--bg-primary);
            color: var(--text-main); 
            overflow-x: hidden; 
            scroll-behavior: smooth; 
        }
"""
content = re.sub(r':root\s*{[^}]*}\s*\*\s*{[^}]*}\s*body\s*{[^}]*}', new_vars, content)

# 2. Navbar Colors
new_nav = """
        /* Navbar Scroll States */
        nav { background: transparent !important; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important; border-bottom: 1px solid transparent !important; }
        nav.nav-scrolled { 
            height: 70px !important; 
            background: var(--glass-white) !important; 
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 10px 30px var(--shadow-soft);
            border-bottom: 1px solid rgba(69, 27, 110, 0.05) !important;
        }
        nav.nav-hidden { transform: translateY(-100%); }
        nav.nav-scrolled .nav-logo img { height: 28px !important; transition: height 0.4s; }
        .nav-logo, .nav-links a { color: var(--text-main) !important; }
        .nav-logo { filter: none; } /* Original logo colors */
        .nav-cta { background: var(--text-main) !important; color: #fff !important; }
"""
content = re.sub(r'/\* Navbar Scroll States \*/.*?(?=/\* Ambient Background)', new_nav, content, flags=re.DOTALL)

# 3. Ambient Shapes
new_ambient = """
        /* Ambient Background Shapes for Hero */
        .ambient-shape { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.8; pointer-events: none; z-index: 1; }
        .ambient-1 { width: 500px; height: 500px; background: var(--bg-secondary); top: -100px; left: -100px; animation: floatShape 15s ease-in-out infinite alternate; }
        .ambient-2 { width: 600px; height: 600px; background: var(--accent-pink); bottom: -200px; right: -100px; animation: floatShape 20s ease-in-out infinite alternate-reverse; opacity: 0.3; }
        @keyframes floatShape { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(60px, 40px) scale(1.1); } }
"""
content = re.sub(r'/\* Ambient Background.*?@keyframes floatShape[^}]*}', new_ambient, content, flags=re.DOTALL)

# 4. Global Text and Section Fixes
# Hero
content = content.replace('color: rgba(255, 255, 255, 0.7);', 'color: var(--text-secondary);')
content = content.replace('color:#032F2C', 'color:#fff')
content = content.replace('background:var(--cream);', 'background:var(--accent-red);')
content = content.replace('color:#fff; border: 1px solid rgba(255,255,255,0.2);', 'color:var(--text-main); border: 1px solid rgba(69,27,110,0.15);')

# Marquee logos shouldn't be inverted anymore because background is white
content = content.replace('filter: brightness(0) invert(1);', 'filter: grayscale(100%) opacity(0.6);')
content = content.replace('filter: grayscale(100%) opacity(0.6); transition:', 'filter: grayscale(100%) opacity(0.6); transition:')
# Ensure hover removes grayscale
content = content.replace('.nv-project-logo:hover { opacity: 1; }', '.nv-project-logo:hover { opacity: 1; filter: grayscale(0%); }')

# Ecosystem Text
content = content.replace('color: #fff; font-size: 52px;', 'color: var(--text-main); font-size: 52px;')
content = content.replace('color: rgba(255,255,255,0.7); font-size: 18px;', 'color: var(--text-secondary); font-size: 18px;')

# Globe Core
content = content.replace('background: radial-gradient(circle at 30% 30%, #451B6E, #150824); box-shadow: 0 0 100px rgba(69, 27, 110, 0.9), inset -20px -20px 40px rgba(0,0,0,0.8);',
                          'background: radial-gradient(circle at 30% 30%, #FFFFFF, #FFEEEA); box-shadow: 0 0 80px rgba(208, 160, 181, 0.4), inset -20px -20px 40px rgba(69, 27, 110, 0.05); border: 1px solid rgba(255,255,255,0.8);')
content = content.replace('border: 1px solid rgba(255,255,255,0.15);', 'border: 1px solid rgba(69, 27, 110, 0.1);')
content = content.replace('border: 1px dashed rgba(208, 160, 181, 0.4);', 'border: 1px dashed rgba(69, 27, 110, 0.15);')
content = content.replace('box-shadow: 0 0 25px rgba(203, 33, 36, 0.6);', 'box-shadow: 0 10px 25px var(--shadow-soft); border: 1px solid rgba(69,27,110,0.05);')
content = content.replace('box-shadow: 0 0 40px rgba(255, 238, 234, 0.8);', 'box-shadow: 0 20px 40px var(--shadow-heavy); border: 2px solid var(--accent-red);')

# Globe Panel
panel_css = """
            /* Enhanced Premium Side Panel */
            .globe-info-panel { 
                width: 500px; 
                min-height: 400px;
                background: #FFFFFF; 
                border: 1px solid rgba(69, 27, 110, 0.08); 
                border-radius: 32px; 
                padding: 48px; 
                color: var(--text-main); 
                box-shadow: 0 30px 60px var(--shadow-soft); 
                z-index: 20; 
                transform: translateY(0) scale(1); 
                transition: opacity 0.4s, transform 0.4s, box-shadow 0.4s; 
                cursor: pointer;
                position: relative;
                display: flex;
                flex-direction: column;
            }
            .globe-info-panel:hover {
                transform: translateY(-8px) scale(1.02);
                box-shadow: 0 40px 80px var(--shadow-heavy);
            }
            .globe-info-panel.morphing { opacity: 0; transform: translateY(20px) scale(0.95); }
            .globe-info-panel-logo { height: 70px; margin-bottom: 30px; background: #f8fafc; border: 1px solid rgba(69,27,110,0.05); border-radius: 16px; padding: 12px; display: inline-flex; align-items: center; justify-content: center; min-width: 80px; align-self: flex-start; }
            .globe-info-panel-logo img, .globe-info-panel-logo svg { max-height: 100%; max-width: 140px; filter: none; }
            .globe-info-panel h3 { font-family: 'Syne', sans-serif; font-size: 38px; margin-bottom: 16px; color: var(--text-main); }
            .globe-info-panel p { font-size: 18px; line-height: 1.6; color: var(--text-secondary); margin-bottom: 40px; flex-grow: 1; }
            .globe-info-panel .view-btn { 
                background: var(--text-main); 
                color: #fff; padding: 16px 32px; border-radius: 100px; 
                font-weight: 700; font-size: 16px; text-align: center;
                transition: transform 0.3s, box-shadow 0.3s; 
                pointer-events: none; 
            }
"""
content = re.sub(r'/\* Enhanced Premium Side Panel \*/.*?\.globe-info-panel \.view-btn[^}]*}', panel_css, content, flags=re.DOTALL)

# Modal Updates (Light & Elegant)
new_modal_css = """
            /* Modal Overlay */
            .modal-overlay {
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(255, 255, 255, 0.4);
                backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px);
                z-index: 9999999;
                display: flex; align-items: center; justify-content: center;
                opacity: 1; visibility: visible;
                transition: opacity 0.5s ease, visibility 0.5s ease;
                padding: 20px;
            }
            .modal-overlay.hidden { opacity: 0; visibility: hidden; pointer-events: none; }
            
            /* Modal Content */
            .project-modal-content {
                background: #ffffff;
                border: 1px solid rgba(69,27,110,0.08);
                color: var(--text-main);
                width: 100%; max-width: 800px;
                border-radius: 32px;
                padding: 50px;
                position: relative;
                transform: scale(1) translateY(0);
                opacity: 1;
                transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.5s ease;
                box-shadow: 0 40px 100px var(--shadow-heavy);
                display: flex; flex-direction: column;
            }
            .modal-overlay.hidden .project-modal-content { transform: scale(0.9) translateY(30px); opacity: 0; }
            
            .modal-close {
                position: absolute; top: 30px; right: 30px;
                width: 40px; height: 40px;
                background: #f8fafc; border-radius: 50%;
                border: 1px solid rgba(69,27,110,0.05);
                display: flex; align-items: center; justify-content: center;
                cursor: pointer; transition: background 0.2s, transform 0.2s;
            }
            .modal-close:hover { background: #e2e8f0; transform: rotate(90deg); }
            .modal-close svg { width: 20px; height: 20px; fill: var(--text-main); }
            
            .modal-header { display: flex; align-items: center; gap: 30px; margin-bottom: 40px; }
            .modal-logo-box { width: 100px; height: 100px; background: #f8fafc; border: 1px solid rgba(69,27,110,0.05); border-radius: 20px; display: flex; align-items: center; justify-content: center; padding: 20px; flex-shrink: 0; }
            .modal-logo-box img, .modal-logo-box svg { max-width: 100%; max-height: 100%; object-fit: contain; }
            .modal-title-area h2 { font-family: 'Syne', sans-serif; font-size: 40px; color: var(--text-main); margin-bottom: 8px; letter-spacing: -1px; }
            .modal-status-tag { display: inline-block; padding: 6px 14px; background: rgba(208, 160, 181, 0.15); color: var(--accent-red); font-size: 14px; font-weight: 700; border-radius: 100px; }
            
            .modal-body p.modal-desc { font-size: 18px; color: var(--text-secondary); line-height: 1.7; margin-bottom: 40px; }
            
            .modal-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 40px; }
            .modal-metric { background: #f8fafc; border: 1px solid rgba(69,27,110,0.05); border-radius: 20px; padding: 24px; }
            .modal-metric-val { font-size: 36px; font-weight: 800; color: var(--text-main); font-family: 'Syne', sans-serif; margin-bottom: 8px; }
            .modal-metric-lbl { font-size: 14px; color: var(--text-secondary); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
            
            .modal-progress-wrap { background: #f8fafc; border: 1px solid rgba(69,27,110,0.05); border-radius: 20px; padding: 24px; margin-bottom: 40px; }
            .modal-progress-header { display: flex; justify-content: space-between; margin-bottom: 12px; font-weight: 600; color: var(--text-main); }
            .modal-progress-bar-bg { width: 100%; height: 8px; background: rgba(69,27,110,0.1); border-radius: 10px; overflow: hidden; }
            .modal-progress-bar-fill { height: 100%; background: linear-gradient(90deg, var(--accent-red), var(--text-main)); border-radius: 10px; transition: width 1s cubic-bezier(0.16, 1, 0.3, 1); }
            
            .modal-action a { display: block; width: 100%; text-align: center; background: var(--text-main); color: #fff; padding: 18px; border-radius: 16px; font-size: 18px; font-weight: 700; text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; }
            .modal-action a:hover { transform: translateY(-3px); box-shadow: 0 10px 25px var(--shadow-heavy); }
"""
content = re.sub(r'/\* Modal Overlay \*/.*?\.modal-action a:hover[^}]*}', new_modal_css, content, flags=re.DOTALL)

# Footer
content = content.replace('color: var(--rose); opacity: 0.9;', 'color: var(--text-main); opacity: 1;')
content = content.replace('color: var(--cream); text-decoration: none;', 'color: var(--text-main); text-decoration: none; opacity: 0.8;')

# GSAP Background Animations (Light theme transition)
gsap_bg_logic = """
            // 4. Smooth Body Background Color Transitions
            gsap.to("body", {
                backgroundColor: "#FFEEEA", // Soft Peach
                ease: "none",
                scrollTrigger: {
                    trigger: ".nv-marquee-section",
                    start: "top center",
                    end: "bottom top",
                    scrub: true
                }
            });
            
            gsap.to("body", {
                backgroundColor: "#FFFFFF", // Clean White
                ease: "none",
                scrollTrigger: {
                    trigger: "footer",
                    start: "top bottom",
                    end: "bottom bottom",
                    scrub: true
                }
            });
"""
# We replace the previous GSAP bg logic
content = re.sub(r'// 4\. Smooth Body Background Color Transitions.*?// Footer Staggered Reveal', gsap_bg_logic + '\n            // Footer Staggered Reveal', content, flags=re.DOTALL)


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Light Aida theme successfully applied!")
