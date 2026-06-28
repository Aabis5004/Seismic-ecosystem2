import json

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

new_index = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seismic | The Private Layer for Web3 & Fintech</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Syne:wght@800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --emerald: #00211d; 
            --plum: #523542; 
            --rose: #D0A0B7; 
            --text-main: #0f172a;
            --text-secondary: #64748b;
            --glass-bg: rgba(255, 255, 255, 0.75);
            --glass-border: rgba(82, 53, 66, 0.1);
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Inter', sans-serif; background: #fff; color: var(--text-main); overflow-x: hidden; scroll-behavior: smooth; }}
        
        nav {{ position: fixed; top: 0; left: 0; right: 0; height: 90px; display: flex; align-items: center; z-index: 1000; background: #ffffff; border-bottom: 1px solid var(--glass-border); }}
        .nav-inner {{ display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 1400px; margin: 0 auto; padding: 0 40px; }}
        .nav-logo {{ font-family: 'Syne', sans-serif; font-size: 26px; font-weight: 800; color: var(--plum); text-decoration: none; display: flex; align-items: center; gap: 12px; }}
        .nav-logo img {{ height: 36px; }}
        .nav-links {{ display: flex; gap: 40px; }}
        .nav-links a {{ text-decoration: none; color: var(--plum); font-weight: 600; font-size: 15px; opacity: 0.75; transition: opacity 0.3s; }}
        .nav-links a:hover {{ opacity: 1; }}
        .nav-cta {{ background: var(--plum); color: #fff; padding: 12px 28px; border-radius: 100px; font-weight: 600; text-decoration: none; font-size: 15px; transition: transform 0.3s; }}
        .nav-cta:hover {{ transform: translateY(-2px); box-shadow: 0 10px 20px rgba(82, 53, 66, 0.15); }}

        .nv-hero {{ position: relative; padding: 140px 0 60px; background: var(--emerald); min-height: auto; text-align: center; color: #ffffff; overflow: hidden; }}
        .nv-hero-content {{ width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 24px; z-index: 10; }}
        .nv-hero h1 {{ font-family: 'Syne', sans-serif; font-size: clamp(2rem, 5vw, 3.8rem); font-weight: 800; line-height: 1.1; margin: 0 0 20px; letter-spacing: -2px; }}
        .nv-hero-subtitle {{ font-size: clamp(1rem, 1.8vw, 1.15rem); color: rgba(255, 255, 255, 0.7); max-width: 650px; margin: 0 auto 40px; line-height: 1.6; font-weight: 500; }}

        .nv-marquee-section {{ width: 100%; padding: 40px 0 80px; overflow: hidden; background: var(--emerald); }}
        .nv-marquee-track {{ display: flex; gap: 80px; width: max-content; animation: nvMarqueeMove 45s linear infinite; align-items: center; }}
        .nv-project-logo {{ height: 28px; opacity: 0.8; filter: brightness(0) invert(1); transition: opacity 0.3s; }}
        .nv-project-logo:hover {{ opacity: 1; }}

        @keyframes nvMarqueeMove {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(calc(-50% - 40px)); }} }}

        /* Preloader Styles */
        #premium-preloader {{
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: #FFFFFF; display: flex; align-items: center; justify-content: center;
            z-index: 999999;
            transition: opacity 0.8s ease-in-out, visibility 0.8s ease-in-out;
        }}
        .preloader-hidden {{ opacity: 0 !important; visibility: hidden !important; }}
        .loader-svg {{ width: 140px; height: 140px; animation: main-pulse 3s cubic-bezier(0.4, 0, 0.2, 1) infinite; }}
        .blob-center {{ animation: blob-pulse 3s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite; transform-origin: 50% 50%; }}
        .blob-1 {{ animation: blob-orbit-1 3s cubic-bezier(0.65, 0, 0.35, 1) infinite; transform-origin: 50px 50px; }}
        .blob-2 {{ animation: blob-orbit-2 3s cubic-bezier(0.65, 0, 0.35, 1) infinite; transform-origin: 50px 50px; }}
        .loader-circle {{ stroke-dasharray: 220; stroke-dashoffset: 220; stroke-linecap: round; transform-origin: 50% 50%; animation: draw-ring 3s cubic-bezier(0.65, 0, 0.35, 1) infinite; }}

        @keyframes main-pulse {{
            0% {{ transform: scale(0.95) rotate(0deg); filter: drop-shadow(0 10px 20px rgba(69,27,110,0.1)); }}
            50% {{ transform: scale(1) rotate(5deg); filter: drop-shadow(0 20px 40px rgba(203,33,36,0.15)); }}
            100% {{ transform: scale(0.95) rotate(0deg); filter: drop-shadow(0 10px 20px rgba(69,27,110,0.1)); }}
        }}
        @keyframes blob-pulse {{ 0% {{ transform: scale(0.5); fill: #FFEEEA; }} 50% {{ transform: scale(1.3); fill: #D0A0B5; }} 100% {{ transform: scale(0.5); fill: #FFEEEA; }} }}
        @keyframes blob-orbit-1 {{ 0% {{ transform: rotate(0deg) translateX(0) scale(1); }} 50% {{ transform: rotate(180deg) translateX(12px) scale(0.5); }} 100% {{ transform: rotate(360deg) translateX(0) scale(1); }} }}
        @keyframes blob-orbit-2 {{ 0% {{ transform: rotate(0deg) translateX(0) scale(1); }} 50% {{ transform: rotate(-180deg) translateX(-12px) scale(0.5); }} 100% {{ transform: rotate(-360deg) translateX(0) scale(1); }} }}
        @keyframes draw-ring {{ 0% {{ stroke-dashoffset: 220; transform: rotate(-90deg); }} 50% {{ stroke-dashoffset: 0; transform: rotate(90deg); }} 100% {{ stroke-dashoffset: -220; transform: rotate(270deg); }} }}

        /* Footer */
        footer {{ padding: 100px 0; background: #ffffff; border-top: 1px solid var(--glass-border); }}
        .footer-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 80px; max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
        .footer-logo {{ font-family: 'Syne', sans-serif; font-size: 32px; font-weight: 800; color: var(--plum); margin-bottom: 24px; }}
        .footer-links h4 {{ color: var(--plum); opacity: 0.6; text-transform: uppercase; font-size: 13px; letter-spacing: 2px; margin-bottom: 24px; }}
        .footer-links ul {{ list-style: none; }}
        .footer-links li {{ margin-bottom: 16px; }}
        .footer-links a {{ color: var(--plum); text-decoration: none; font-size: 15px; font-weight: 500; transition: color 0.3s; }}
        .footer-links a:hover {{ color: var(--rose); }}

        @media (max-width: 768px) {{
            .nav-links {{ display: none; }}
            .footer-grid {{ grid-template-columns: 1fr; gap: 60px; text-align: center; }}
        }}
    </style>
</head>
<body>
    <div id="premium-preloader">
        <svg class="loader-svg" viewBox="0 0 100 100">
            <defs>
                <filter id="goo">
                <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur" />
                <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9" result="goo" />
                <feBlend in="SourceGraphic" in2="goo" />
                </filter>
                <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#451B6E" />
                <stop offset="100%" stop-color="#CB2124" />
                </linearGradient>
            </defs>
            <g filter="url(#goo)">
                <circle class="blob-center" cx="50" cy="50" r="14" fill="#FFEEEA" />
                <circle class="blob-1" cx="28" cy="50" r="14" fill="url(#grad1)" />
                <circle class="blob-2" cx="72" cy="50" r="14" fill="#CB2124" />
            </g>
            <circle class="loader-circle" cx="50" cy="50" r="35" stroke="url(#grad1)" stroke-width="2" fill="none" />
        </svg>
    </div>

    <nav>
        <div class="nav-inner">
            <a href="#" class="nav-logo">
                <img src="https://framerusercontent.com/images/RNHqhN9OPcfhYMA27iXglrnSM.svg" alt="Seismic">
            </a>
            <div class="nav-links">
                <a href="#ecosystem">Ecosystem</a>
                <a href="https://docs.seismic.systems/" target="_blank">Docs</a>
            </div>
            <a href="#ecosystem" class="nav-cta">Start Building</a>
        </div>
    </nav>

    <section class="nv-hero">
        <div class="nv-hero-content">
            <h1>Projects Building on Seismic</h1>
            <p class="nv-hero-subtitle">Explore apps and teams shaping the future of encrypted blockchain infrastructure.</p>
            <div style="display: flex; gap: 16px; justify-content: center;">
                <a href="#ecosystem" style="background:#fff; color:var(--emerald); padding: 14px 40px; border-radius: 12px; font-weight: 700; text-decoration: none;">Get Started</a>
                <a href="https://docs.seismic.systems/" target="_blank" style="background:rgba(255,255,255,0.1); color:#fff; border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(10px); padding: 14px 40px; border-radius: 12px; font-weight: 700; text-decoration: none;">Read Docs</a>
            </div>
        </div>
    </section>

    <div class="nv-marquee-section">
        <div class="nv-marquee-track">
            <!-- First set -->
            <img src="https://framerusercontent.com/images/kztSbCmi83eGOrsXWs2bnEqc.png" alt="Via" class="nv-project-logo">
            <img src="https://framerusercontent.com/images/le7rHwmt4MoWogPPDnWwvEQo1sA.png" alt="DashX" class="nv-project-logo">
            <img src="https://framerusercontent.com/images/oJ7QVYoyXBbQ4HvAmIeq5U7AGpo.png" alt="Blend" class="nv-project-logo">
            <img src="https://sedona.fi/images/sedona-logo.svg" alt="Sedona" class="nv-project-logo">
            <img src="https://framerusercontent.com/images/jXvSeWV4wo0VFBKxnbf1nl2lw.png" alt="Brookwell" class="nv-project-logo">
            <img src="https://framerusercontent.com/images/H4Yn2rDLeq2wENXWMdowmAbKZs.png" alt="Shift" class="nv-project-logo">
            <!-- Duplicated for infinite scroll -->
            <img src="https://framerusercontent.com/images/kztSbCmi83eGOrsXWs2bnEqc.png" alt="Via" class="nv-project-logo">
            <img src="https://framerusercontent.com/images/le7rHwmt4MoWogPPDnWwvEQo1sA.png" alt="DashX" class="nv-project-logo">
            <img src="https://framerusercontent.com/images/oJ7QVYoyXBbQ4HvAmIeq5U7AGpo.png" alt="Blend" class="nv-project-logo">
            <img src="https://sedona.fi/images/sedona-logo.svg" alt="Sedona" class="nv-project-logo">
            <img src="https://framerusercontent.com/images/jXvSeWV4wo0VFBKxnbf1nl2lw.png" alt="Brookwell" class="nv-project-logo">
            <img src="https://framerusercontent.com/images/H4Yn2rDLeq2wENXWMdowmAbKZs.png" alt="Shift" class="nv-project-logo">
        </div>
    </div>

    <!-- 3D GLOBE SECTION -->
    <section class="ecosystem-section" id="ecosystem" style="padding: 120px 0; background: #000000; overflow: hidden; position: relative;">
        <div class="section-header" style="position: relative; z-index: 10; text-align: center;">
            <h2 style="color: #fff; font-size: 52px; margin-bottom: 16px; font-family: 'Syne', sans-serif;">Ecosystem Network</h2>
            <p style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px; margin: 0 auto;">Building the foundation for private, scalable financial services.</p>
        </div>
        
        <style>
            .globe-layout {{ display: flex; align-items: center; justify-content: center; gap: 60px; max-width: 1400px; margin: 0 auto; padding: 40px 20px; }}
            .globe-wrapper {{ position: relative; width: 600px; height: 600px; perspective: 1200px; flex-shrink: 0; }}
            .globe-core {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 320px; height: 320px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #451B6E, #150824); box-shadow: 0 0 100px rgba(69, 27, 110, 0.9), inset -20px -20px 40px rgba(0,0,0,0.8); z-index: 5; }}
            .globe-grid {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 50%; transform-style: preserve-3d; animation: spin-globe 25s linear infinite; z-index: 6; }}
            .globe-meridian {{ position: absolute; top: 15%; left: 15%; width: 70%; height: 70%; border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; }}
            .globe-meridian:nth-child(1) {{ transform: rotateY(0deg); }} .globe-meridian:nth-child(2) {{ transform: rotateY(45deg); }} .globe-meridian:nth-child(3) {{ transform: rotateY(90deg); }} .globe-meridian:nth-child(4) {{ transform: rotateY(135deg); }}
            .globe-equator {{ position: absolute; top: 15%; left: 15%; width: 70%; height: 70%; border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; transform: rotateX(90deg); }}
            @keyframes spin-globe {{ 0% {{ transform: rotateY(0deg) rotateX(15deg); }} 100% {{ transform: rotateY(360deg) rotateX(15deg); }} }}
            .orbit-track {{ position: absolute; top: 50%; left: 50%; border: 1px dashed rgba(208, 160, 181, 0.4); border-radius: 50%; transform-style: preserve-3d; z-index: 10; }}
            .orbit-node {{ position: absolute; top: 50%; left: 50%; width: 64px; height: 64px; margin: -32px 0 0 -32px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); border-radius: 50%; box-shadow: 0 0 25px rgba(203, 33, 36, 0.6); display: flex; align-items: center; justify-content: center; cursor: pointer; transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s; transform-style: preserve-3d; }}
            .orbit-node:hover, .orbit-node.active {{ transform: scale(1.3) !important; box-shadow: 0 0 40px rgba(255, 238, 234, 0.8); z-index: 100; }}
            .orbit-node img, .orbit-node svg {{ max-width: 40px; max-height: 40px; object-fit: contain; border-radius: 8px; filter: none; }}
            
            .globe-info-panel {{ width: 400px; background: rgba(30, 11, 48, 0.6); backdrop-filter: blur(20px); border: 1px solid rgba(208, 160, 181, 0.2); border-radius: 24px; padding: 40px; color: #fff; box-shadow: 0 30px 60px rgba(0,0,0,0.5); z-index: 20; transform: translateY(0); transition: opacity 0.4s, transform 0.4s; }}
            .globe-info-panel.morphing {{ opacity: 0; transform: translateY(20px); }}
            .globe-info-panel-logo {{ height: 60px; margin-bottom: 24px; background: #fff; border-radius: 12px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; min-width: 60px; }}
            .globe-info-panel-logo img, .globe-info-panel-logo svg {{ max-height: 100%; max-width: 120px; filter: none; }}
            .globe-info-panel h3 {{ font-family: 'Syne', sans-serif; font-size: 32px; margin-bottom: 16px; background: linear-gradient(90deg, #FFEEEA, #D0A0B5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .globe-info-panel p {{ font-size: 16px; line-height: 1.6; color: rgba(255,255,255,0.7); margin-bottom: 30px; }}
            .globe-info-panel a {{ background: linear-gradient(90deg, #451B6E, #CB2124); color: #fff; padding: 14px 32px; border-radius: 100px; text-decoration: none; font-weight: 700; display: inline-block; transition: transform 0.3s, box-shadow 0.3s; }}
            .globe-info-panel a:hover {{ transform: translateY(-3px); box-shadow: 0 10px 20px rgba(203, 33, 36, 0.4); }}
            @media (max-width: 1024px) {{ .globe-layout {{ flex-direction: column; gap: 20px; }} .globe-wrapper {{ width: 350px; height: 350px; }} .globe-core {{ width: 180px; height: 180px; }} .orbit-node {{ width: 44px; height: 44px; margin: -22px 0 0 -22px; }} .orbit-node img, .orbit-node svg {{ max-width: 28px; max-height: 28px; }} .globe-info-panel {{ width: 100%; max-width: 400px; padding: 30px; }} }}
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
                <div class="orbit-track" id="track1" style="width: 450px; height: 450px; margin: -225px 0 0 -225px;"></div>
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
            track1.style.width = (r1*2) + 'px'; track1.style.height = (r1*2) + 'px'; track1.style.margin = (-r1) + 'px 0 0 ' + (-r1) + 'px';
            track2.style.width = (r2*2) + 'px'; track2.style.height = (r2*2) + 'px'; track2.style.margin = (-r2) + 'px 0 0 ' + (-r2) + 'px';
            
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
                        nodes.forEach(n => n.el.classList.remove('active'));
                        node.classList.add('active');
                        updatePanel(proj);
                    }});
                    nodes.push({{ el: node, angle: angleOffset, radius: radius, track: track, speed: speed, reverse: reverse, proj: proj }});
                    track.appendChild(node);
                }});
            }}
            
            createNodes(p1, track1, r1, 0.003, false);
            createNodes(p2, track2, r2, 0.002, true);
            
            const tiltX = 65;
            track1.style.transform = `rotateX(${{tiltX}}deg)`;
            track2.style.transform = `rotateX(${{tiltX}}deg) rotateY(15deg)`;
            
            let time = 0;
            function animateOrbit() {{
                time += 1;
                nodes.forEach(n => {{
                    const currentAngle = n.angle + (time * n.speed * (n.reverse ? -1 : 1));
                    const x = Math.cos(currentAngle) * n.radius;
                    const y = Math.sin(currentAngle) * n.radius;
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
            
            // Fix preloader dismissal script explicitly
            window.addEventListener('load', () => {{
                setTimeout(() => {{
                    const pre = document.getElementById('premium-preloader');
                    if (pre) pre.classList.add('preloader-hidden');
                }}, 3000);
            }});
            
            // Failsafe: if 'load' event already fired before this script is evaluated:
            if(document.readyState === 'complete') {{
                setTimeout(() => {{
                    const pre = document.getElementById('premium-preloader');
                    if (pre) pre.classList.add('preloader-hidden');
                }}, 3000);
            }}
        </script>
    </section>

    <footer>
        <div class="footer-grid">
            <div>
                <div class="footer-logo">SEISMIC</div>
                <p style="color: var(--text-secondary); line-height: 1.6; font-size: 14px;">Native encryption for a secure, decentralized world.</p>
            </div>
            <div class="footer-links">
                <h4>Ecosystem</h4>
                <ul><li><a href="#ecosystem">Partners</a></li><li><a href="https://docs.seismic.systems/">Documentation</a></li></ul>
            </div>
            <div class="footer-links">
                <h4>Community</h4>
                <ul><li><a href="https://x.com/SeismicSys">@SeismicSys</a></li><li><a href="https://discord.gg/seismic">Discord</a></li></ul>
            </div>
        </div>
    </footer>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)

print("index.html fully rebuilt with clean structure!")
