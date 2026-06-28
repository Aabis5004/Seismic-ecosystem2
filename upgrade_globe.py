import json
import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Expanded Project Data
expanded_projects = [
    {
        "title": "Blend", 
        "desc": "Treasury-as-a-service for fintechs using private multi-currency accounts and robust yield instruments.", 
        "long_desc": "Blend brings sophisticated treasury management to growing fintechs. By leveraging Seismic's private layer, Blend offers multi-currency cash sweeps, automated yield generation, and complete data privacy for corporate treasuries.",
        "link_url": "https://blend.money/", "link_text": "Visit Blend \u2014>", 
        "logo": "<img src=\"https://framerusercontent.com/images/oJ7QVYoyXBbQ4HvAmIeq5U7AGpo.png\" alt=\"Blend\">",
        "status": "Mainnet Live", "progress": 100, "metric1": "$4.2B", "metric1_label": "Processed", "metric2": "120+", "metric2_label": "Institutions"
    },
    {
        "title": "Vend", 
        "desc": "Infrastructure for autonomous commerce. Self-financing machines powered by revenue-based credit.",
        "long_desc": "Vend is revolutionizing the machine economy. Using encrypted data rails, autonomous vending machines and kiosks can instantly secure financing based on verified, completely private revenue streams.",
        "link_url": "https://vend.money/", "link_text": "Visit Vend \u2014>", 
        "logo": "<img src=\"https://framerusercontent.com/images/SARuWkuMvBKRbeQeXHS7HCejxQw.png\" alt=\"Vend\">",
        "status": "Beta", "progress": 75, "metric1": "8,500", "metric1_label": "Active Machines", "metric2": "$12M", "metric2_label": "Financed"
    },
    {
        "title": "Sedona", 
        "desc": "Your neobank. Your keys.", 
        "long_desc": "Sedona provides a consumer neobanking experience with self-custody at its core. Manage your fiat and crypto seamlessly without ever surrendering control of your assets or personal data.",
        "link_url": "https://sedona.fi/", "link_text": "Explore Sedona \u2014>", 
        "logo": "<img src=\"https://sedona.fi/images/sedona-logo.svg\" alt=\"Sedona\">",
        "status": "Mainnet Live", "progress": 100, "metric1": "45K", "metric1_label": "Users", "metric2": "$85M", "metric2_label": "TVL"
    },
    {
        "title": "Brookwell", 
        "desc": "Private stablecoin cash accounts. Earn DeFi yields while securely paying rent and payroll via normal channels.", 
        "long_desc": "Brookwell bridges the gap between decentralized yield and real-world utility. Hold your balance in high-yield stablecoins while routing payments directly to standard fiat bank accounts privately.",
        "link_url": "https://www.brookwell.com/", "link_text": "View Brookwell \u2014>", 
        "logo": "<img src=\"https://www.brookwell.com/_next/image?url=%2Flogo.png&w=1080&q=75\" alt=\"Brookwell\">",
        "status": "In Development", "progress": 40, "metric1": "Q4", "metric1_label": "Expected Launch", "metric2": "12K", "metric2_label": "Waitlist"
    },
    {
        "title": "Cred Protocol", 
        "desc": "Private credit & working capital. Underwriting and lending for real-world businesses with zero data leaks.", 
        "long_desc": "Cred Protocol introduces zero-knowledge underwriting. Businesses can prove their cash flow and financial health to access on-chain credit pools without exposing sensitive trade secrets.",
        "link_url": "https://credprotocol.com/", "link_text": "Explore Cred \u2014>", 
        "logo": "<img src=\"https://framerusercontent.com/images/ly6CYDZguctn369Fter3suQOhA.png\" alt=\"Cred\">",
        "status": "Testnet", "progress": 85, "metric1": "$250M", "metric1_label": "Committed Capital", "metric2": "1.2s", "metric2_label": "Proof Time"
    },
    {
        "title": "Specie", 
        "desc": "Modern banking for global businesses. Send, receive, and manage money worldwide with fast settlement across local and global rails.", 
        "long_desc": "Specie operates a next-generation clearing network. By leveraging Seismic's private layer, cross-border B2B payments settle instantly while complying with local data privacy regulations.",
        "link_url": "https://www.specie.finance/", "link_text": "Explore Specie \u2014>", 
        "logo": "<img src=\"https://framerusercontent.com/images/UgeAlOHZZ3FQwYhs7gAADiyTsio.svg\" alt=\"Specie\">",
        "status": "Mainnet Live", "progress": 100, "metric1": "14", "metric1_label": "Supported Corridors", "metric2": "< 3s", "metric2_label": "Settlement"
    },
    {
        "title": "Via", 
        "desc": "Stablecoin-first finance. Borderless access to capital, seamless payments, and premium yield.", 
        "long_desc": "Via enables borderless commerce by natively integrating stablecoins into everyday financial operations, offering a secure yield engine and instant vendor payouts globally.",
        "link_url": "https://www.via.xyz/", "link_text": "Explore Via \u2014>", 
        "logo": "<img src=\"https://framerusercontent.com/images/kztSbCmi83eGOrsXWs2bnEqc.png\" alt=\"Via\">",
        "status": "Mainnet Live", "progress": 100, "metric1": "20+", "metric1_label": "Partner Networks", "metric2": "5.5%", "metric2_label": "Avg Yield"
    },
    {
        "title": "Shift", 
        "desc": "The Membership That Pays You Back. Elite financial services, lifestyle privileges, and exclusive perks driven by real yield models.", 
        "long_desc": "Shift redefines premium card memberships. Instead of burning fees, your membership deposit earns private, on-chain yield that dynamically pays for luxury travel and lifestyle subscriptions.",
        "link_url": "https://www.shift-apply.com/", "link_text": "Visit Shift \u2014>", 
        "logo": "<img src=\"https://framerusercontent.com/images/H4Yn2rDLeq2wENXWMdowmAbKZs.png\" alt=\"Shift\">",
        "status": "Private Beta", "progress": 90, "metric1": "1,000", "metric1_label": "Founding Members", "metric2": "Tier 1", "metric2_label": "Perks Active"
    },
    {
        "title": "DashX", 
        "desc": "Cross-border payments powered by crypto. Accept USDC, track transactions, and withdraw INR globally through one unified stack.", 
        "long_desc": "DashX is the ultimate bridge for emerging markets. It enables merchants to accept global stablecoin payments and instantly off-ramp to local fiat currencies seamlessly.",
        "link_url": "https://dashx.xyz/", "link_text": "Use DashX \u2014>", 
        "logo": "<img src=\"https://framerusercontent.com/images/le7rHwmt4MoWogPPDnWwvEQo1sA.png\" alt=\"DashX\">",
        "status": "Mainnet Live", "progress": 100, "metric1": "$8.2M", "metric1_label": "Monthly Volume", "metric2": "0.1%", "metric2_label": "FX Fee"
    }
]

# We will completely replace the <section class="ecosystem-section" id="ecosystem"> with our new version
# This ensures a clean slate for the new CSS and JS
sec_start = content.find('<section class="ecosystem-section" id="ecosystem"')
sec_end = content.find('</section>', sec_start) + len('</section>')

new_html = f"""
    <!-- 3D GLOBE SECTION WITH MODAL -->
    <section class="ecosystem-section" id="ecosystem" style="padding: 120px 0; background: #000000; overflow: hidden; position: relative;">
        <div class="section-header" style="position: relative; z-index: 10; text-align: center;">
            <h2 style="color: #fff; font-size: 52px; margin-bottom: 16px; font-family: 'Syne', sans-serif;">Ecosystem Network</h2>
            <p style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px; margin: 0 auto;">Building the foundation for private, scalable financial services.</p>
        </div>
        
        <style>
            .globe-layout {{ display: flex; align-items: center; justify-content: center; gap: 80px; max-width: 1400px; margin: 0 auto; padding: 40px 20px; }}
            .globe-wrapper {{ position: relative; width: 600px; height: 600px; perspective: 1200px; flex-shrink: 0; }}
            .globe-core {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 320px; height: 320px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, #451B6E, #150824); box-shadow: 0 0 100px rgba(69, 27, 110, 0.9), inset -20px -20px 40px rgba(0,0,0,0.8); z-index: 5; }}
            .globe-grid {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 50%; transform-style: preserve-3d; animation: spin-globe 25s linear infinite; z-index: 6; }}
            .globe-meridian {{ position: absolute; top: 15%; left: 15%; width: 70%; height: 70%; border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; }}
            .globe-meridian:nth-child(1) {{ transform: rotateY(0deg); }} .globe-meridian:nth-child(2) {{ transform: rotateY(45deg); }} .globe-meridian:nth-child(3) {{ transform: rotateY(90deg); }} .globe-meridian:nth-child(4) {{ transform: rotateY(135deg); }}
            .globe-equator {{ position: absolute; top: 15%; left: 15%; width: 70%; height: 70%; border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; transform: rotateX(90deg); }}
            @keyframes spin-globe {{ 0% {{ transform: rotateY(0deg) rotateX(15deg); }} 100% {{ transform: rotateY(360deg) rotateX(15deg); }} }}
            
            .orbit-track {{ position: absolute; top: 50%; left: 50%; border: 1px dashed rgba(208, 160, 181, 0.4); border-radius: 50%; transform-style: preserve-3d; z-index: 10; }}
            .orbit-node {{ position: absolute; top: 50%; left: 50%; width: 64px; height: 64px; margin: -32px 0 0 -32px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(10px); border-radius: 50%; box-shadow: 0 0 25px rgba(203, 33, 36, 0.6); display: flex; align-items: center; justify-content: center; cursor: pointer; transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s; transform-style: preserve-3d; }}
            .orbit-node:hover, .orbit-node.active {{ transform: scale(1.3) !important; box-shadow: 0 0 40px rgba(255, 238, 234, 0.8); z-index: 100; border: 2px solid var(--plum); }}
            .orbit-node img, .orbit-node svg {{ max-width: 40px; max-height: 40px; object-fit: contain; border-radius: 8px; filter: none; }}
            
            /* Enhanced Premium Side Panel */
            .globe-info-panel {{ 
                width: 500px; 
                min-height: 400px;
                background: rgba(20, 10, 35, 0.7); 
                backdrop-filter: blur(24px); 
                border: 1px solid rgba(208, 160, 181, 0.25); 
                border-radius: 32px; 
                padding: 48px; 
                color: #fff; 
                box-shadow: 0 40px 80px rgba(0,0,0,0.6), inset 0 0 0 1px rgba(255,255,255,0.05); 
                z-index: 20; 
                transform: translateY(0) scale(1); 
                transition: opacity 0.4s, transform 0.4s, box-shadow 0.4s; 
                cursor: pointer;
                position: relative;
                display: flex;
                flex-direction: column;
            }}
            .globe-info-panel:hover {{
                transform: translateY(-8px) scale(1.02);
                box-shadow: 0 50px 100px rgba(0,0,0,0.8), 0 0 40px rgba(69, 27, 110, 0.4), inset 0 0 0 1px rgba(255,255,255,0.1);
            }}
            .globe-info-panel.morphing {{ opacity: 0; transform: translateY(20px) scale(0.95); }}
            .globe-info-panel-logo {{ height: 70px; margin-bottom: 30px; background: #fff; border-radius: 16px; padding: 12px; display: inline-flex; align-items: center; justify-content: center; min-width: 80px; align-self: flex-start; }}
            .globe-info-panel-logo img, .globe-info-panel-logo svg {{ max-height: 100%; max-width: 140px; filter: none; }}
            .globe-info-panel h3 {{ font-family: 'Syne', sans-serif; font-size: 38px; margin-bottom: 16px; background: linear-gradient(90deg, #FFEEEA, #D0A0B5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
            .globe-info-panel p {{ font-size: 18px; line-height: 1.6; color: rgba(255,255,255,0.7); margin-bottom: 40px; flex-grow: 1; }}
            .globe-info-panel .view-btn {{ 
                background: linear-gradient(90deg, #451B6E, #CB2124); 
                color: #fff; padding: 16px 32px; border-radius: 100px; 
                font-weight: 700; font-size: 16px; text-align: center;
                transition: transform 0.3s, box-shadow 0.3s; 
                pointer-events: none; /* Clicking the panel itself handles it */
            }}
            
            /* Modal Overlay */
            .modal-overlay {{
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background: rgba(0, 0, 0, 0.6);
                backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px);
                z-index: 9999999;
                display: flex; align-items: center; justify-content: center;
                opacity: 1; visibility: visible;
                transition: opacity 0.5s ease, visibility 0.5s ease;
                padding: 20px;
            }}
            .modal-overlay.hidden {{ opacity: 0; visibility: hidden; pointer-events: none; }}
            
            /* Modal Content */
            .project-modal-content {{
                background: #ffffff;
                width: 100%; max-width: 800px;
                border-radius: 32px;
                padding: 50px;
                position: relative;
                transform: scale(1) translateY(0);
                opacity: 1;
                transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.5s ease;
                box-shadow: 0 40px 100px rgba(0,0,0,0.5);
                display: flex; flex-direction: column;
            }}
            .modal-overlay.hidden .project-modal-content {{ transform: scale(0.9) translateY(30px); opacity: 0; }}
            
            .modal-close {{
                position: absolute; top: 30px; right: 30px;
                width: 40px; height: 40px;
                background: #f1f5f9; border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                cursor: pointer; transition: background 0.2s, transform 0.2s;
            }}
            .modal-close:hover {{ background: #e2e8f0; transform: rotate(90deg); }}
            .modal-close svg {{ width: 20px; height: 20px; fill: #0f172a; }}
            
            .modal-header {{ display: flex; align-items: center; gap: 30px; margin-bottom: 40px; }}
            .modal-logo-box {{ width: 100px; height: 100px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 20px; display: flex; align-items: center; justify-content: center; padding: 20px; flex-shrink: 0; }}
            .modal-logo-box img, .modal-logo-box svg {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
            .modal-title-area h2 {{ font-family: 'Syne', sans-serif; font-size: 40px; color: var(--plum); margin-bottom: 8px; letter-spacing: -1px; }}
            .modal-status-tag {{ display: inline-block; padding: 6px 14px; background: rgba(69,27,110,0.1); color: var(--plum); font-size: 14px; font-weight: 700; border-radius: 100px; }}
            
            .modal-body p.modal-desc {{ font-size: 18px; color: #475569; line-height: 1.7; margin-bottom: 40px; }}
            
            .modal-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-bottom: 40px; }}
            .modal-metric {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 20px; padding: 24px; }}
            .modal-metric-val {{ font-size: 36px; font-weight: 800; color: var(--plum); font-family: 'Syne', sans-serif; margin-bottom: 8px; }}
            .modal-metric-lbl {{ font-size: 14px; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }}
            
            .modal-progress-wrap {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 20px; padding: 24px; margin-bottom: 40px; }}
            .modal-progress-header {{ display: flex; justify-content: space-between; margin-bottom: 12px; font-weight: 600; color: #0f172a; }}
            .modal-progress-bar-bg {{ width: 100%; height: 8px; background: #e2e8f0; border-radius: 10px; overflow: hidden; }}
            .modal-progress-bar-fill {{ height: 100%; background: linear-gradient(90deg, #451B6E, #CB2124); border-radius: 10px; transition: width 1s cubic-bezier(0.16, 1, 0.3, 1); }}
            
            .modal-action a {{ display: block; width: 100%; text-align: center; background: var(--plum); color: #fff; padding: 18px; border-radius: 16px; font-size: 18px; font-weight: 700; text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; }}
            .modal-action a:hover {{ transform: translateY(-3px); box-shadow: 0 10px 25px rgba(69,27,110,0.25); }}

            @media (max-width: 1024px) {{ 
                .globe-layout {{ flex-direction: column; gap: 40px; }} 
                .globe-wrapper {{ width: 350px; height: 350px; }} 
                .globe-core {{ width: 180px; height: 180px; }} 
                .orbit-node {{ width: 44px; height: 44px; margin: -22px 0 0 -22px; }} 
                .orbit-node img, .orbit-node svg {{ max-width: 28px; max-height: 28px; }} 
                .globe-info-panel {{ width: 100%; max-width: 500px; padding: 30px; min-height: 300px; }} 
                .globe-info-panel h3 {{ font-size: 28px; }}
                .globe-info-panel p {{ font-size: 16px; }}
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
                <div class="orbit-track" id="track1" style="width: 450px; height: 450px; margin: -225px 0 0 -225px;"></div>
                <div class="orbit-track" id="track2" style="width: 650px; height: 650px; margin: -325px 0 0 -325px;"></div>
            </div>
            
            <div class="globe-info-panel" id="globeInfoPanel"></div>
        </div>
        
        <!-- Modal Overlay -->
        <div id="projectModal" class="modal-overlay hidden">
            <div class="project-modal-content">
                <div class="modal-close" id="modalClose">
                    <svg viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
                </div>
                <div class="modal-header">
                    <div class="modal-logo-box" id="modalLogo"></div>
                    <div class="modal-title-area">
                        <h2 id="modalTitle">Project Name</h2>
                        <div class="modal-status-tag" id="modalStatus">Status</div>
                    </div>
                </div>
                <div class="modal-body">
                    <p class="modal-desc" id="modalDesc">Detailed description here.</p>
                    <div class="modal-grid">
                        <div class="modal-metric">
                            <div class="modal-metric-val" id="modalMetric1Val">0</div>
                            <div class="modal-metric-lbl" id="modalMetric1Lbl">Metric</div>
                        </div>
                        <div class="modal-metric">
                            <div class="modal-metric-val" id="modalMetric2Val">0</div>
                            <div class="modal-metric-lbl" id="modalMetric2Lbl">Metric</div>
                        </div>
                    </div>
                    <div class="modal-progress-wrap">
                        <div class="modal-progress-header">
                            <span>Development Progress</span>
                            <span id="modalProgressText">0%</span>
                        </div>
                        <div class="modal-progress-bar-bg">
                            <div class="modal-progress-bar-fill" id="modalProgressFill" style="width: 0%;"></div>
                        </div>
                    </div>
                    <div class="modal-action">
                        <a href="#" id="modalLink" target="_blank">Visit Project</a>
                    </div>
                </div>
            </div>
        </div>
        
        <script>
            const globeProjects = {json.dumps(expanded_projects)};
            const track1 = document.getElementById('track1');
            const track2 = document.getElementById('track2');
            const panel = document.getElementById('globeInfoPanel');
            const modal = document.getElementById('projectModal');
            const modalClose = document.getElementById('modalClose');
            
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
                    
                    // Hover to update side panel
                    node.addEventListener('mouseenter', () => {{
                        nodes.forEach(n => n.el.classList.remove('active'));
                        node.classList.add('active');
                        updatePanel(proj);
                    }});
                    
                    // Click node to open modal
                    node.addEventListener('click', () => {{
                        openModal(proj);
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
            
            let currentProj = null;
            function updatePanel(proj) {{
                if(currentProj && currentProj.title === proj.title) return;
                currentProj = proj;
                panel.classList.add('morphing');
                setTimeout(() => {{
                    panel.innerHTML = `
                        <div class="globe-info-panel-logo">${{proj.logo}}</div>
                        <h3>${{proj.title}}</h3>
                        <p>${{proj.desc}}</p>
                        <div class="view-btn">View Details</div>
                    `;
                    panel.classList.remove('morphing');
                }}, 300);
            }}
            
            // Click panel to open modal
            panel.addEventListener('click', () => {{
                if (currentProj) openModal(currentProj);
            }});
            
            function openModal(proj) {{
                document.getElementById('modalLogo').innerHTML = proj.logo;
                document.getElementById('modalTitle').textContent = proj.title;
                document.getElementById('modalStatus').textContent = proj.status;
                document.getElementById('modalDesc').textContent = proj.long_desc;
                
                document.getElementById('modalMetric1Val').textContent = proj.metric1;
                document.getElementById('modalMetric1Lbl').textContent = proj.metric1_label;
                document.getElementById('modalMetric2Val').textContent = proj.metric2;
                document.getElementById('modalMetric2Lbl').textContent = proj.metric2_label;
                
                document.getElementById('modalProgressText').textContent = proj.progress + '%';
                
                // Reset progress bar to 0 before opening for animation
                document.getElementById('modalProgressFill').style.width = '0%';
                
                document.getElementById('modalLink').href = proj.link_url;
                document.getElementById('modalLink').textContent = proj.link_text;
                
                modal.classList.remove('hidden');
                
                // Trigger progress bar animation after a short delay
                setTimeout(() => {{
                    document.getElementById('modalProgressFill').style.width = proj.progress + '%';
                }}, 100);
            }}
            
            function closeModal() {{
                modal.classList.add('hidden');
            }}
            
            modalClose.addEventListener('click', closeModal);
            modal.addEventListener('click', (e) => {{
                if(e.target === modal) closeModal(); // Close if clicked outside
            }});
            
            if(globeProjects.length > 0) {{
                updatePanel(globeProjects[0]);
                nodes[0].el.classList.add('active');
            }}
            
            // Failsafe preloader hide
            window.addEventListener('load', () => {{ setTimeout(() => {{ const p = document.getElementById('premium-preloader'); if(p) p.classList.add('preloader-hidden'); }}, 3000); }});
            if(document.readyState === 'complete') {{ setTimeout(() => {{ const p = document.getElementById('premium-preloader'); if(p) p.classList.add('preloader-hidden'); }}, 3000); }}
        </script>
    </section>
"""

new_content = content[:sec_start] + new_html + content[sec_end:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Globe UI upgraded with large cards and interactive modal successfully!")
