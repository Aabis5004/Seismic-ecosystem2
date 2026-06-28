import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS Variables & Body
new_vars = """
        :root {
            --forest: #032F2C; 
            --emerald: #063E38; 
            --cream: #F8F7F4; 
            --purple: #6A4B63;
            --rose: #C07A8D;
            --glass: rgba(255,255,255,0.08);
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Inter', sans-serif; 
            background-color: var(--forest); /* Dynamic GSAP background */
            color: var(--cream); 
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
            background: rgba(3, 47, 44, 0.7) !important; 
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            border-bottom: 1px solid var(--glass) !important;
        }
        nav.nav-hidden { transform: translateY(-100%); }
        nav.nav-scrolled .nav-logo img { height: 28px !important; transition: height 0.4s; }
        .nav-logo, .nav-links a { color: var(--cream) !important; }
        .nav-logo { filter: brightness(0) invert(1); } /* Make dark logo white */
        .nav-cta { background: var(--rose) !important; color: #fff !important; }
"""
content = re.sub(r'/\* Navbar Scroll States \*/.*?(?=/\* Ambient Background)', new_nav, content, flags=re.DOTALL)

# 3. Ambient Shapes
new_ambient = """
        /* Ambient Background Shapes for Hero */
        .ambient-shape { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.6; pointer-events: none; z-index: 1; }
        .ambient-1 { width: 500px; height: 500px; background: var(--purple); top: -100px; left: -100px; animation: floatShape 15s ease-in-out infinite alternate; }
        .ambient-2 { width: 600px; height: 600px; background: var(--emerald); bottom: -200px; right: -100px; animation: floatShape 20s ease-in-out infinite alternate-reverse; }
        @keyframes floatShape { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(60px, 40px) scale(1.1); } }
"""
content = re.sub(r'/\* Ambient Background.*?@keyframes floatShape[^}]*}', new_ambient, content, flags=re.DOTALL)

# 4. Remove hardcoded backgrounds from sections
content = content.replace('background: var(--emerald);', 'background: transparent;')
content = content.replace('background: #000000;', 'background: transparent;')
content = content.replace('background: #ffffff;', 'background: transparent;')
content = content.replace('color: var(--text-main);', 'color: var(--cream);')
content = content.replace('color: var(--plum);', 'color: var(--cream);')
content = content.replace('color: var(--text-secondary);', 'color: rgba(248, 247, 244, 0.7);')
content = content.replace('background: #fff;', 'background: transparent;')

# Fix hero button colors
content = content.replace('color:var(--emerald)', 'color:#032F2C')
content = content.replace('background:#fff;', 'background:var(--cream);')

# Globe Panel Updates
content = content.replace('rgba(20, 10, 35, 0.7)', 'rgba(6, 62, 56, 0.4)') # Panel BG
content = content.replace('rgba(208, 160, 181, 0.25)', 'rgba(255, 255, 255, 0.1)') # Panel Border
content = content.replace('linear-gradient(90deg, #FFEEEA, #D0A0B5)', 'linear-gradient(90deg, #F8F7F4, #C07A8D)') # Text gradient
content = content.replace('linear-gradient(90deg, #451B6E, #CB2124)', 'linear-gradient(90deg, #C07A8D, #6A4B63)') # Button gradient

# Modal Updates (Make modal dark and glassmorphic)
new_modal_css = """
            /* Modal Content */
            .project-modal-content {
                background: rgba(3, 47, 44, 0.85);
                backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px);
                border: 1px solid var(--glass);
                color: var(--cream);
                width: 100%; max-width: 800px;
                border-radius: 32px;
                padding: 50px;
                position: relative;
                transform: scale(1) translateY(0);
                opacity: 1;
                transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.5s ease;
                box-shadow: 0 40px 100px rgba(0,0,0,0.8), inset 0 0 0 1px rgba(255,255,255,0.05);
                display: flex; flex-direction: column;
            }
            .modal-overlay.hidden .project-modal-content { transform: scale(0.9) translateY(30px); opacity: 0; }
            
            .modal-close {
                position: absolute; top: 30px; right: 30px;
                width: 40px; height: 40px;
                background: rgba(255,255,255,0.1); border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                cursor: pointer; transition: background 0.2s, transform 0.2s;
            }
            .modal-close:hover { background: rgba(255,255,255,0.2); transform: rotate(90deg); }
            .modal-close svg { width: 20px; height: 20px; fill: #fff; }
            
            .modal-header { display: flex; align-items: center; gap: 30px; margin-bottom: 40px; }
            .modal-logo-box { width: 100px; height: 100px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; display: flex; align-items: center; justify-content: center; padding: 20px; flex-shrink: 0; }
            .modal-logo-box img, .modal-logo-box svg { max-width: 100%; max-height: 100%; object-fit: contain; }
            .modal-title-area h2 { font-family: 'Syne', sans-serif; font-size: 40px; color: var(--cream); margin-bottom: 8px; letter-spacing: -1px; }
            .modal-status-tag { display: inline-block; padding: 6px 14px; background: rgba(192, 122, 141, 0.2); color: var(--rose); font-size: 14px; font-weight: 700; border-radius: 100px; }
            
            .modal-body p.modal-desc { font-size: 18px; color: rgba(248, 247, 244, 0.8); line-height: 1.7; margin-bottom: 40px; }
            
            .modal-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 40px; }
            .modal-metric { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 24px; }
            .modal-metric-val { font-size: 36px; font-weight: 800; color: var(--cream); font-family: 'Syne', sans-serif; margin-bottom: 8px; }
            .modal-metric-lbl { font-size: 14px; color: rgba(248, 247, 244, 0.6); font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
            
            .modal-progress-wrap { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; padding: 24px; margin-bottom: 40px; }
            .modal-progress-header { display: flex; justify-content: space-between; margin-bottom: 12px; font-weight: 600; color: var(--cream); }
            .modal-progress-bar-bg { width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 10px; overflow: hidden; }
            .modal-progress-bar-fill { height: 100%; background: linear-gradient(90deg, var(--rose), var(--purple)); border-radius: 10px; transition: width 1s cubic-bezier(0.16, 1, 0.3, 1); }
            
            .modal-action a { display: block; width: 100%; text-align: center; background: linear-gradient(90deg, var(--rose), var(--purple)); color: #fff; padding: 18px; border-radius: 16px; font-size: 18px; font-weight: 700; text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; }
            .modal-action a:hover { transform: translateY(-3px); box-shadow: 0 10px 25px rgba(192, 122, 141, 0.4); }
"""
content = re.sub(r'/\* Modal Content \*/.*?\.modal-action a:hover[^}]*}', new_modal_css, content, flags=re.DOTALL)

# Add GSAP Background Color animation
gsap_bg_logic = """
            // 4. Smooth Body Background Color Transitions
            // Animate body background based on section scroll
            gsap.to("body", {
                backgroundColor: "#063E38", // Dark Emerald
                ease: "none",
                scrollTrigger: {
                    trigger: ".nv-marquee-section",
                    start: "top center",
                    end: "bottom top",
                    scrub: true
                }
            });
            
            gsap.to("body", {
                backgroundColor: "#6A4B63", // Muted Purple
                ease: "none",
                scrollTrigger: {
                    trigger: "#ecosystem",
                    start: "top center",
                    end: "bottom center",
                    scrub: true
                }
            });
            
            gsap.to("body", {
                backgroundColor: "#032F2C", // Deep Forest Green
                ease: "none",
                scrollTrigger: {
                    trigger: "footer",
                    start: "top bottom",
                    end: "bottom bottom",
                    scrub: true
                }
            });
"""
content = content.replace('// Footer Staggered Reveal', gsap_bg_logic + '\n            // Footer Staggered Reveal')

# Make footer logo white (since body is dark)
content = content.replace('color: var(--cream); opacity: 0.6;', 'color: var(--rose); opacity: 0.9;')
content = content.replace('color: var(--cream); text-decoration: none;', 'color: var(--cream); text-decoration: none;')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Color unification complete! 60fps scrolling flow applied.")
