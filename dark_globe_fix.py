import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS Variables & Body to DARK theme
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
            background-color: var(--forest);
            color: var(--cream); 
            overflow-x: hidden; 
            scroll-behavior: smooth; 
        }
"""
content = re.sub(r':root\s*{[^}]*}\s*\*\s*{[^}]*}\s*body\s*{[^}]*}', new_vars, content)

# 2. Navbar Colors to Dark
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
        .nav-logo { filter: brightness(0) invert(1); }
        .nav-cta { background: var(--rose) !important; color: #fff !important; }
"""
content = re.sub(r'/\* Navbar Scroll States \*/.*?(?=/\* Ambient Background)', new_nav, content, flags=re.DOTALL)

# 3. Ambient Shapes to Dark
new_ambient = """
        /* Ambient Background Shapes for Hero */
        .ambient-shape { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.6; pointer-events: none; z-index: 1; }
        .ambient-1 { width: 500px; height: 500px; background: var(--purple); top: -100px; left: -100px; animation: floatShape 15s ease-in-out infinite alternate; }
        .ambient-2 { width: 600px; height: 600px; background: var(--emerald); bottom: -200px; right: -100px; animation: floatShape 20s ease-in-out infinite alternate-reverse; opacity: 0.6; }
        @keyframes floatShape { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(60px, 40px) scale(1.1); } }
"""
content = re.sub(r'/\* Ambient Background.*?@keyframes floatShape[^}]*}', new_ambient, content, flags=re.DOTALL)

# 4. Global Text and Section Fixes to Dark
content = content.replace('color: var(--text-secondary);', 'color: rgba(248, 247, 244, 0.7);')
content = content.replace('color:#fff', 'color:#032F2C')
content = content.replace('background:var(--accent-red);', 'background:var(--cream);')
content = content.replace('color:var(--text-main); border: 1px solid rgba(69,27,110,0.15);', 'color:var(--cream); border: 1px solid rgba(255,255,255,0.2);')

content = content.replace('filter: grayscale(100%) opacity(0.6); transition:', 'filter: brightness(0) invert(1); opacity: 0.6; transition:')
content = content.replace('.nv-project-logo:hover { opacity: 1; filter: grayscale(0%); }', '.nv-project-logo:hover { opacity: 1; filter: none; }')

content = content.replace('color: var(--text-main); font-size: 52px;', 'color: var(--cream); font-size: 52px;')

# 5. Globe CSS: Sizes (+40%) & Dark Colors
globe_css = """
        <style>
            .globe-layout { display: flex; align-items: center; justify-content: center; gap: 80px; max-width: 1400px; margin: 0 auto; padding: 40px 20px; }
            .globe-wrapper { position: relative; width: 850px; height: 850px; perspective: 1500px; flex-shrink: 0; }
            .globe-core { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 450px; height: 450px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #451B6E, #150824); box-shadow: 0 0 120px rgba(255,255,255,0.15), inset -30px -30px 60px rgba(0,0,0,0.8); border: 1px solid rgba(255,255,255,0.1); z-index: 5; }
            .globe-grid { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 50%; transform-style: preserve-3d; animation: spin-globe 25s linear infinite; z-index: 6; }
            .globe-meridian { position: absolute; top: 15%; left: 15%; width: 70%; height: 70%; border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 50%; }
            .globe-meridian:nth-child(1) { transform: rotateY(0deg); } .globe-meridian:nth-child(2) { transform: rotateY(45deg); } .globe-meridian:nth-child(3) { transform: rotateY(90deg); } .globe-meridian:nth-child(4) { transform: rotateY(135deg); }
            .globe-equator { position: absolute; top: 15%; left: 15%; width: 70%; height: 70%; border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 50%; transform: rotateX(90deg); }
            @keyframes spin-globe { 0% { transform: rotateY(0deg) rotateX(15deg); } 100% { transform: rotateY(360deg) rotateX(15deg); } }
            
            .orbit-track { position: absolute; top: 50%; left: 50%; border: 2px dashed rgba(255, 255, 255, 0.15); border-radius: 50%; transform-style: preserve-3d; z-index: 10; }
            
            /* Enhanced Projects Nodes - Increased Size +40% */
            .orbit-node { 
                position: absolute; top: 50%; left: 50%; 
                width: 90px; height: 90px; margin: -45px 0 0 -45px; 
                background: rgba(20, 10, 35, 0.9); backdrop-filter: blur(10px); 
                border-radius: 50%; 
                box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.15); 
                display: flex; align-items: center; justify-content: center; cursor: pointer; 
                transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s; 
                transform-style: preserve-3d; 
            }
            .orbit-node:hover, .orbit-node.active { 
                transform: scale(1.3) !important; 
                box-shadow: 0 20px 50px rgba(192, 122, 141, 0.6), inset 0 0 0 2px var(--rose); 
                z-index: 100; 
            }
            .orbit-node img, .orbit-node svg { max-width: 55px; max-height: 55px; object-fit: contain; border-radius: 12px; filter: none; }
            
            /* Enhanced Premium Side Panel (Dark Theme) */
            .globe-info-panel { 
                width: 500px; min-height: 400px;
                background: rgba(6, 62, 56, 0.4); 
                backdrop-filter: blur(24px);
                border: 1px solid rgba(255, 255, 255, 0.1); 
                border-radius: 32px; padding: 48px; 
                color: var(--cream); 
                box-shadow: 0 40px 80px rgba(0,0,0,0.6), inset 0 0 0 1px rgba(255,255,255,0.05); 
                z-index: 20; transform: translateY(0) scale(1); 
                transition: opacity 0.4s, transform 0.4s, box-shadow 0.4s; 
                cursor: pointer; position: relative; display: flex; flex-direction: column;
            }
            .globe-info-panel:hover {
                transform: translateY(-8px) scale(1.02);
                box-shadow: 0 50px 100px rgba(0,0,0,0.8), 0 0 40px rgba(69, 27, 110, 0.4), inset 0 0 0 1px rgba(255,255,255,0.1);
            }
            .globe-info-panel.morphing { opacity: 0; transform: translateY(20px) scale(0.95); }
            .globe-info-panel-logo { height: 70px; margin-bottom: 30px; background: #fff; border-radius: 16px; padding: 12px; display: inline-flex; align-items: center; justify-content: center; min-width: 80px; align-self: flex-start; }
            .globe-info-panel-logo img, .globe-info-panel-logo svg { max-height: 100%; max-width: 140px; filter: none; }
            .globe-info-panel h3 { font-family: 'Syne', sans-serif; font-size: 38px; margin-bottom: 16px; background: linear-gradient(90deg, var(--cream), var(--rose)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .globe-info-panel p { font-size: 18px; line-height: 1.6; color: rgba(248, 247, 244, 0.7); margin-bottom: 40px; flex-grow: 1; }
            .globe-info-panel .view-btn { 
                background: linear-gradient(90deg, var(--rose), var(--purple)); 
                color: #fff; padding: 16px 32px; border-radius: 100px; 
                font-weight: 700; font-size: 16px; text-align: center;
                transition: transform 0.3s, box-shadow 0.3s; 
                pointer-events: none; 
            }
"""
content = re.sub(r'<style>.*?\.globe-info-panel \.view-btn[^}]*}', globe_css, content, flags=re.DOTALL)

# Modal Updates (Dark & Glassmorphic)
new_modal_css = """
            /* Modal Overlay */
            .modal-overlay {
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(0, 0, 0, 0.6);
                backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px);
                z-index: 9999999;
                display: flex; align-items: center; justify-content: center;
                opacity: 1; visibility: visible;
                transition: opacity 0.5s ease, visibility 0.5s ease;
                padding: 20px;
            }
            .modal-overlay.hidden { opacity: 0; visibility: hidden; pointer-events: none; }
            
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
            .modal-logo-box img, .modal-logo-box svg { max-width: 100%; max-height: 100%; object-fit: contain; filter:none; }
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
content = re.sub(r'/\* Modal Overlay \*/.*?\.modal-action a:hover[^}]*}', new_modal_css, content, flags=re.DOTALL)

# Fix JS orbit math and radiuses
js_radiuses = """
            const isMob = window.innerWidth <= 1024;
            const r1 = isMob ? 200 : 315; // Increased by ~40%
            const r2 = isMob ? 280 : 455; // Increased by ~40%
            track1.style.width = (r1*2) + 'px'; track1.style.height = (r1*2) + 'px'; track1.style.margin = (-r1) + 'px 0 0 ' + (-r1) + 'px';
            track2.style.width = (r2*2) + 'px'; track2.style.height = (r2*2) + 'px'; track2.style.margin = (-r2) + 'px 0 0 ' + (-r2) + 'px';
"""
content = re.sub(r'const isMob = window\.innerWidth <= 1024;.*?track2\.style\.margin = \(-r2\) \+ \'px 0 0 \' \+ \(-r2\) \+ \'px\';', js_radiuses, content, flags=re.DOTALL)

js_orbit = """
            let time = 0;
            function animateOrbit() {
                time += 1;
                nodes.forEach(n => {
                    const currentAngle = n.angle + (time * n.speed * (n.reverse ? -1 : 1));
                    const x = Math.cos(currentAngle) * n.radius;
                    const y = Math.sin(currentAngle) * n.radius;
                    const unRotateX = -tiltX;
                    const unRotateY = n.track === track2 ? -15 : 0;
                    // FIX: Remove n.radius from translate! The node is absolutely positioned 50% 50% with negative margin, so translate(0,0) is center.
                    n.el.style.transform = `translate(${x}px, ${y}px) rotateX(${unRotateX}deg) rotateY(${unRotateY}deg)`;
                });
                requestAnimationFrame(animateOrbit);
            }
"""
content = re.sub(r'let time = 0;.*?requestAnimationFrame\(animateOrbit\);\n            }', js_orbit, content, flags=re.DOTALL)

# GSAP Background Animations (Dark theme transition)
gsap_bg_logic = """
            // 4. Smooth Body Background Color Transitions
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
content = re.sub(r'// 4\. Smooth Body Background Color Transitions.*?// Footer Staggered Reveal', gsap_bg_logic + '\n            // Footer Staggered Reveal', content, flags=re.DOTALL)

# Footer text
content = content.replace('color: var(--text-main); opacity: 1;', 'color: var(--rose); opacity: 0.9;')
content = content.replace('color: var(--text-main); text-decoration: none; opacity: 0.8;', 'color: var(--cream); text-decoration: none;')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dark theme restored and orbital physics fixed! Elements scaled up significantly.")
