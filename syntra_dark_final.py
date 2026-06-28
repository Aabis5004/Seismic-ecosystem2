import json

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

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seismic | The Private Layer for Web3 & Fintech</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- GSAP for Smooth Animations -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    
    <style>
        :root {{
            --bg-main: #020617; /* Very Dark Navy */
            --text-main: #F8FAFC; 
            --text-sub: #94A3B8;
            --accent-blue: #2563EB;
            --accent-cyan: #06B6D4;
            --accent-light: #60A5FA;
            --glass-dark: rgba(15, 23, 42, 0.6);
            --shadow-glow: 0 0 80px rgba(37, 99, 235, 0.4);
            --border-glass: 1px solid rgba(255, 255, 255, 0.08);
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Inter', sans-serif; 
            background: var(--bg-main);
            color: var(--text-main); 
            overflow-x: hidden; 
            min-height: 100vh;
        }}

        /* GSAP Initial States (Crucial for scroll effects) */
        .gsap-blur-reveal {{ opacity: 0; visibility: hidden; filter: blur(20px); transform: translateY(60px); }}
        .gsap-parallax-scale {{ transform: scale(0.95); opacity: 0; }}
        
        /* Navbar */
        nav {{ 
            position: fixed; top: 0; width: 100%; height: 100px; 
            display: flex; align-items: center; justify-content: center; 
            z-index: 1000; background: transparent !important; 
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important; 
            border-bottom: 1px solid transparent !important;
        }}
        .nav-inner {{ width: 100%; max-width: 1400px; display: flex; justify-content: space-between; align-items: center; padding: 0 40px; }}
        .nav-logo img {{ height: 28px; filter: brightness(0) invert(1); }}
        .nav-links {{ display: flex; gap: 40px; align-items: center; }}
        .nav-links a {{ color: var(--text-sub) !important; text-decoration: none; font-size: 15px; font-weight: 500; transition: color 0.2s; }}
        .nav-links a:hover {{ color: var(--text-main) !important; }}
        .nav-cta {{ background: rgba(255,255,255,0.05) !important; border: 1px solid rgba(255,255,255,0.1); color: #fff !important; padding: 12px 24px; border-radius: 100px; font-weight: 600; text-decoration: none; font-size: 14px; transition: background 0.2s, box-shadow 0.2s; backdrop-filter: blur(10px); }}
        .nav-cta:hover {{ background: rgba(255,255,255,0.1) !important; box-shadow: 0 0 20px rgba(255,255,255,0.1); }}
        
        nav.nav-scrolled {{ 
            height: 70px !important; 
            background: rgba(2, 6, 23, 0.8) !important; 
            backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
            border-bottom: var(--border-glass) !important;
        }}
        nav.nav-hidden {{ transform: translateY(-100%); }}

        /* Preloader */
        #premium-preloader {{ position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: var(--bg-main); z-index: 999999; display: flex; align-items: center; justify-content: center; transition: opacity 0.8s ease, visibility 0.8s ease; }}
        #premium-preloader.preloader-hidden {{ opacity: 0; visibility: hidden; pointer-events: none; }}
        .loader-svg {{ width: 80px; height: 80px; overflow: visible; }}
        .loader-svg .blob-center {{ transform-origin: 40px 40px; animation: pulse-center 3s ease-in-out infinite; }}
        .loader-svg .blob-1 {{ transform-origin: 40px 40px; animation: orbit-1 3s cubic-bezier(0.4, 0, 0.2, 1) infinite; }}
        .loader-svg .blob-2 {{ transform-origin: 40px 40px; animation: orbit-2 3s cubic-bezier(0.4, 0, 0.2, 1) infinite; }}
        .loader-svg .loader-circle {{ stroke-dasharray: 220; stroke-dashoffset: 220; animation: draw-circle 3s cubic-bezier(0.6, 0.04, 0.15, 0.95) infinite; transform-origin: 40px 40px; transform: rotate(-90deg); }}
        @keyframes pulse-center {{ 0% {{ transform: scale(0.9); }} 50% {{ transform: scale(1.1); }} 100% {{ transform: scale(0.9); }} }}
        @keyframes orbit-1 {{ 0% {{ transform: rotate(0deg) translateX(0); }} 50% {{ transform: rotate(180deg) translateX(-15px) scale(0.8); }} 100% {{ transform: rotate(360deg) translateX(0); }} }}
        @keyframes orbit-2 {{ 0% {{ transform: rotate(0deg) translateX(0); }} 50% {{ transform: rotate(180deg) translateX(15px) scale(0.8); }} 100% {{ transform: rotate(360deg) translateX(0); }} }}
        @keyframes draw-circle {{ 0% {{ stroke-dashoffset: 220; }} 50% {{ stroke-dashoffset: 0; }} 100% {{ stroke-dashoffset: -220; }} }}

        /* Ambient Background Shapes (Parallax Targets) */
        .ambient-shape {{ position: absolute; border-radius: 50%; filter: blur(150px); opacity: 0.4; pointer-events: none; z-index: 1; }}
        .ambient-1 {{ width: 800px; height: 500px; background: var(--accent-blue); bottom: -100px; left: 50%; transform: translateX(-50%); opacity: 0.25; }}

        /* Hero */
        .nv-hero {{ 
            position: relative; padding: 220px 20px 140px; text-align: center; 
            background: transparent; overflow: hidden; min-height: 80vh; 
            display: flex; flex-direction: column; align-items: center; justify-content: center;
        }}
        .hero-glow-base {{
            position: absolute; bottom: 0; left: 50%; transform: translateX(-50%);
            width: 120vw; height: 500px;
            background: radial-gradient(ellipse at bottom, rgba(37, 99, 235, 0.3) 0%, rgba(2, 6, 23, 0) 70%);
            z-index: 1; pointer-events: none;
        }}
        .nv-hero-content {{ position: relative; z-index: 10; max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; }}
        
        .hero-pill {{
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 8px 16px;
            border-radius: 100px;
            display: flex; align-items: center; gap: 8px;
            font-size: 14px; font-weight: 500; color: var(--accent-light);
            margin-bottom: 24px;
            box-shadow: 0 0 20px rgba(37, 99, 235, 0.1);
        }}
        .hero-pill svg {{ width: 16px; height: 16px; fill: var(--accent-cyan); }}
        
        h1 {{ font-family: 'Inter', sans-serif; font-size: 56px; font-weight: 600; line-height: 1.1; letter-spacing: -1px; color: var(--text-main); margin-bottom: 24px; text-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
        .nv-hero-subtitle {{ font-size: 20px; color: var(--text-sub); line-height: 1.6; margin-bottom: 48px; max-width: 650px; font-weight: 400; }}
        
        /* Marquee */
        .nv-marquee-section {{ padding: 60px 0; background: transparent; overflow: hidden; position: relative; z-index: 10; border-top: 1px solid rgba(255,255,255,0.02); border-bottom: 1px solid rgba(255,255,255,0.02); }}
        .nv-marquee-track {{ display: flex; gap: 100px; width: max-content; animation: marquee 30s linear infinite; align-items: center; opacity: 0.6; }}
        .nv-project-logo {{ height: 32px; filter: brightness(0) invert(1) opacity(0.7); transition: all 0.3s; object-fit: contain; }}
        .nv-project-logo:hover {{ filter: brightness(0) invert(1) opacity(1); transform: scale(1.05); }}
        @keyframes marquee {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}

        /* Globe Base Layout */
        .globe-layout {{ display: flex; align-items: center; justify-content: center; gap: 80px; max-width: 1400px; margin: 0 auto; padding: 120px 20px 60px; }}
        .globe-wrapper {{ position: relative; width: 750px; height: 750px; perspective: 1200px; flex-shrink: 0; }}
        
        /* Syntra Globe Core */
        .globe-core {{ 
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); 
            width: 400px; height: 400px; border-radius: 50%; 
            background: radial-gradient(circle at 30% 30%, #3B82F6, #1E3A8A); 
            box-shadow: 0 0 120px rgba(37, 99, 235, 0.5), inset -20px -20px 60px rgba(0,0,0,0.8); 
            border: 1px solid rgba(96, 165, 250, 0.3); z-index: 5; 
        }}
        
        .globe-grid {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-radius: 50%; transform-style: preserve-3d; animation: spin-globe 30s linear infinite; z-index: 6; opacity: 0.8; }}
        .globe-meridian {{ position: absolute; top: 15%; left: 15%; width: 70%; height: 70%; border: 1px solid rgba(96, 165, 250, 0.15); border-radius: 50%; }}
        .globe-meridian:nth-child(1) {{ transform: rotateY(0deg); }} .globe-meridian:nth-child(2) {{ transform: rotateY(45deg); }} .globe-meridian:nth-child(3) {{ transform: rotateY(90deg); }} .globe-meridian:nth-child(4) {{ transform: rotateY(135deg); }}
        .globe-equator {{ position: absolute; top: 15%; left: 15%; width: 70%; height: 70%; border: 1px solid rgba(96, 165, 250, 0.15); border-radius: 50%; transform: rotateX(90deg); }}
        @keyframes spin-globe {{ 0% {{ transform: rotateY(0deg) rotateX(15deg); }} 100% {{ transform: rotateY(360deg) rotateX(15deg); }} }}
        
        .orbit-track {{ position: absolute; top: 50%; left: 50%; border: 1px dashed rgba(255, 255, 255, 0.1); border-radius: 50%; transform-style: preserve-3d; z-index: 10; }}
        
        /* Syntra Nodes */
        .orbit-node {{ 
            position: absolute; top: 50%; left: 50%; 
            width: 80px; height: 80px; margin: -40px 0 0 -40px; 
            background: var(--glass-dark); backdrop-filter: blur(16px); 
            border-radius: 20px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.1); 
            display: flex; align-items: center; justify-content: center; cursor: pointer; 
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s, background 0.4s; 
            transform-style: preserve-3d; 
        }}
        .orbit-node:hover, .orbit-node.active {{ 
            transform: scale(1.2) !important; 
            background: rgba(30, 58, 138, 0.8);
            box-shadow: 0 15px 40px rgba(37, 99, 235, 0.4), inset 0 0 0 1px rgba(96, 165, 250, 0.5); 
            z-index: 100; 
        }}
        .orbit-node img, .orbit-node svg {{ max-width: 44px; max-height: 44px; object-fit: contain; filter: brightness(0) invert(1); }}
        
        /* Dark Glass Side Panel */
        .globe-info-panel {{ 
            width: 480px; min-height: 400px;
            background: var(--glass-dark); 
            border: var(--border-glass); 
            border-radius: 24px; padding: 48px; 
            color: var(--text-main); 
            box-shadow: 0 30px 60px rgba(0,0,0,0.6); 
            z-index: 20; transform: translateY(0) scale(1); 
            transition: opacity 0.4s, transform 0.4s, box-shadow 0.4s; 
            cursor: pointer; position: relative; display: flex; flex-direction: column;
            backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
        }}
        .globe-info-panel:hover {{
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 40px 80px rgba(0,0,0,0.8), 0 0 40px rgba(37, 99, 235, 0.2);
        }}
        .globe-info-panel.morphing {{ opacity: 0; transform: translateY(20px) scale(0.95); }}
        .globe-info-panel-logo {{ height: 60px; margin-bottom: 32px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 12px; display: inline-flex; align-items: center; justify-content: center; min-width: 80px; align-self: flex-start; }}
        .globe-info-panel-logo img, .globe-info-panel-logo svg {{ max-height: 100%; max-width: 140px; filter: brightness(0) invert(1); }}
        .globe-info-panel h3 {{ font-size: 32px; font-weight: 600; margin-bottom: 12px; color: var(--text-main); letter-spacing: -0.5px; }}
        .globe-info-panel p {{ font-size: 16px; line-height: 1.6; color: var(--text-sub); margin-bottom: 40px; flex-grow: 1; font-weight: 400; }}
        .globe-info-panel .view-btn {{ 
            background: var(--text-main); 
            color: var(--bg-main); padding: 14px 28px; border-radius: 100px; 
            font-weight: 600; font-size: 14px; text-align: center;
            transition: transform 0.3s, box-shadow 0.3s; 
            pointer-events: none; 
        }}

        /* Modal Overlay */
        .modal-overlay {{
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(2, 6, 23, 0.8);
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            z-index: 9999999;
            display: flex; align-items: center; justify-content: center;
            opacity: 1; visibility: visible;
            transition: opacity 0.5s ease, visibility 0.5s ease;
            padding: 20px;
        }}
        .modal-overlay.hidden {{ opacity: 0; visibility: hidden; pointer-events: none; }}
        
        /* Syntra Modal Content */
        .project-modal-content {{
            background: var(--glass-dark);
            border: var(--border-glass);
            color: var(--text-main);
            width: 100%; max-width: 800px;
            border-radius: 24px;
            padding: 48px;
            position: relative;
            transform: scale(1) translateY(0);
            opacity: 1;
            transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.5s ease;
            box-shadow: 0 40px 100px rgba(0,0,0,0.8), 0 0 60px rgba(37, 99, 235, 0.15);
            display: flex; flex-direction: column;
        }}
        .modal-overlay.hidden .project-modal-content {{ transform: scale(0.9) translateY(40px); opacity: 0; filter: blur(10px); }}
        
        .modal-close {{
            position: absolute; top: 24px; right: 24px;
            width: 40px; height: 40px;
            background: rgba(255,255,255,0.05); border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; transition: background 0.2s, transform 0.2s; border: var(--border-glass);
        }}
        .modal-close:hover {{ background: rgba(255,255,255,0.1); transform: rotate(90deg); }}
        .modal-close svg {{ width: 20px; height: 20px; fill: var(--text-main); }}
        
        .modal-header {{ display: flex; align-items: center; gap: 24px; margin-bottom: 40px; }}
        .modal-logo-box {{ width: 90px; height: 90px; background: rgba(255,255,255,0.03); border: var(--border-glass); border-radius: 20px; display: flex; align-items: center; justify-content: center; padding: 20px; flex-shrink: 0; }}
        .modal-logo-box img, .modal-logo-box svg {{ max-width: 100%; max-height: 100%; object-fit: contain; filter: brightness(0) invert(1); }}
        .modal-title-area h2 {{ font-size: 36px; font-weight: 600; color: var(--text-main); margin-bottom: 8px; letter-spacing: -1px; }}
        .modal-status-tag {{ display: inline-block; padding: 6px 14px; background: rgba(96, 165, 250, 0.1); color: var(--accent-light); font-size: 13px; font-weight: 600; border-radius: 100px; border: 1px solid rgba(96, 165, 250, 0.2); }}
        
        .modal-body p.modal-desc {{ font-size: 18px; color: var(--text-sub); line-height: 1.6; margin-bottom: 40px; }}
        
        .modal-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 40px; }}
        .modal-metric {{ background: rgba(255,255,255,0.02); border: var(--border-glass); border-radius: 16px; padding: 24px; }}
        .modal-metric-val {{ font-size: 32px; font-weight: 700; color: var(--text-main); margin-bottom: 6px; letter-spacing: -0.5px; }}
        .modal-metric-lbl {{ font-size: 13px; color: var(--text-sub); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }}
        
        .modal-progress-wrap {{ background: rgba(255,255,255,0.02); border: var(--border-glass); border-radius: 16px; padding: 24px; margin-bottom: 40px; }}
        .modal-progress-header {{ display: flex; justify-content: space-between; margin-bottom: 12px; font-weight: 600; color: var(--text-main); font-size: 14px; }}
        .modal-progress-bar-bg {{ width: 100%; height: 8px; background: rgba(255,255,255,0.05); border-radius: 10px; overflow: hidden; }}
        .modal-progress-bar-fill {{ height: 100%; background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue)); border-radius: 10px; transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1); box-shadow: 0 0 10px rgba(6, 182, 212, 0.5); }}
        
        .modal-action a {{ display: block; width: 100%; text-align: center; background: var(--text-main); color: var(--bg-main); padding: 16px; border-radius: 100px; font-size: 16px; font-weight: 600; text-decoration: none; transition: transform 0.2s, box-shadow 0.2s; }}
        .modal-action a:hover {{ transform: translateY(-3px); box-shadow: 0 10px 25px rgba(255,255,255,0.1); }}

        /* Footer */
        footer {{ background: transparent; padding: 80px 40px; color: var(--text-main); border-top: var(--border-glass); margin-top: 80px; position: relative; z-index: 10; }}
        .footer-grid {{ display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 60px; max-width: 1400px; margin: 0 auto; }}
        .footer-logo {{ font-size: 24px; font-weight: 700; letter-spacing: -0.5px; margin-bottom: 16px; color: var(--text-main); }}
        .footer-links h4 {{ font-size: 14px; font-weight: 600; margin-bottom: 20px; color: var(--text-sub); text-transform: uppercase; letter-spacing: 0.5px; }}
        .footer-links ul {{ list-style: none; }}
        .footer-links li {{ margin-bottom: 12px; }}
        .footer-links a {{ color: var(--text-sub); text-decoration: none; transition: color 0.2s; font-size: 15px; font-weight: 400; }}
        .footer-links a:hover {{ color: var(--text-main); }}
        
        @media (max-width: 1024px) {{ 
            .globe-layout {{ flex-direction: column; gap: 40px; }} 
            .globe-wrapper {{ width: 350px; height: 350px; }} 
            .globe-core {{ width: 180px; height: 180px; }} 
            .orbit-node {{ width: 44px; height: 44px; margin: -22px 0 0 -22px; }} 
            .orbit-node img, .orbit-node svg {{ max-width: 28px; max-height: 28px; }} 
            .globe-info-panel {{ width: 100%; max-width: 500px; padding: 32px; min-height: 300px; }} 
            .globe-info-panel h3 {{ font-size: 26px; }}
            .globe-info-panel p {{ font-size: 15px; }}
            .footer-grid {{ grid-template-columns: 1fr; gap: 40px; }}
            h1 {{ font-size: 40px; }}
        }}
    </style>
</head>
<body>

    <!-- Premium Animated Preloader -->
    <div id="premium-preloader">
        <svg class="loader-svg" viewBox="0 0 100 100">
            <defs>
                <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#06B6D4" />
                    <stop offset="100%" stop-color="#2563EB" />
                </linearGradient>
            </defs>
            <g>
                <circle class="blob-center" cx="50" cy="50" r="14" fill="#60A5FA" />
                <circle class="blob-1" cx="28" cy="50" r="14" fill="url(#grad1)" />
                <circle class="blob-2" cx="72" cy="50" r="14" fill="#06B6D4" />
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

    <div class="ambient-shape ambient-1"></div>
    <div class="hero-glow-base"></div>

    <section class="nv-hero">
        <div class="nv-hero-content">
            <div class="hero-pill gsap-blur-reveal">
                <svg viewBox="0 0 24 24"><path d="M12 2L2 22h20L12 2zm0 3.8l7.1 14.2H4.9L12 5.8z"/></svg>
                Seismic Ecosystem
            </div>
            <h1 class="gsap-blur-reveal">Projects Building on Seismic</h1>
            <p class="nv-hero-subtitle gsap-blur-reveal">Explore apps and teams shaping the future of encrypted blockchain infrastructure.</p>
            <div style="display: flex; gap: 16px; justify-content: center;" class="gsap-blur-reveal">
                <a href="#ecosystem" style="background:var(--text-main); color:var(--bg-main); padding: 14px 32px; border-radius: 100px; font-weight: 600; text-decoration: none; font-size: 15px; box-shadow: 0 4px 15px rgba(255,255,255,0.1);">Get Started</a>
                <a href="https://docs.seismic.systems/" target="_blank" style="background:rgba(255,255,255,0.05); color:var(--text-main); border: var(--border-glass); padding: 14px 32px; border-radius: 100px; font-weight: 600; text-decoration: none; font-size: 15px; backdrop-filter: blur(10px);">Read Docs</a>
            </div>
        </div>
    </section>

    <div class="nv-marquee-section gsap-blur-reveal">
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

    <!-- 3D GLOBE SECTION WITH MODAL -->
    <section class="ecosystem-section" id="ecosystem" style="padding: 100px 0; background: transparent; overflow: hidden; position: relative;">
        <div class="section-header" style="position: relative; z-index: 10; text-align: center;">
            <h2 class="gsap-blur-reveal" style="color: var(--text-main); font-size: 40px; margin-bottom: 16px; font-weight: 600; letter-spacing: -0.5px;">Ecosystem Network</h2>
            <p class="gsap-blur-reveal" style="color: var(--text-sub); font-size: 18px; max-width: 600px; margin: 0 auto; font-weight: 400;">Building the foundation for private, scalable financial services.</p>
        </div>
        
        <div class="globe-layout gsap-parallax-scale">
            <div class="globe-wrapper" id="globeWrapper">
                <div class="globe-core"></div>
                <div class="globe-grid">
                    <div class="globe-meridian"></div>
                    <div class="globe-meridian"></div>
                    <div class="globe-meridian"></div>
                    <div class="globe-meridian"></div>
                    <div class="globe-equator"></div>
                </div>
                <div class="orbit-track" id="track1"></div>
                <div class="orbit-track" id="track2"></div>
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
            const r1 = isMob ? 200 : 280; 
            const r2 = isMob ? 280 : 380; 
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
                    n.el.style.transform = `translate(${{x}}px, ${{y}}px) rotateX(${{unRotateX}}deg) rotateY(${{unRotateY}}deg)`;
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
            window.addEventListener('load', () => {{ setTimeout(() => {{ const p = document.getElementById('premium-preloader'); if(p) p.classList.add('preloader-hidden'); }}, 2500); }});
            if(document.readyState === 'complete') {{ setTimeout(() => {{ const p = document.getElementById('premium-preloader'); if(p) p.classList.add('preloader-hidden'); }}, 2500); }}
        </script>
    </section>

    <footer>
        <div class="footer-grid">
            <div class="gsap-blur-reveal footer-col">
                <div class="footer-logo">SEISMIC</div>
                <p style="color: var(--text-sub); line-height: 1.6; font-size: 15px;">Native encryption for a secure, decentralized world.</p>
            </div>
            <div class="footer-links gsap-blur-reveal footer-col">
                <h4>Ecosystem</h4>
                <ul><li><a href="#ecosystem">Partners</a></li><li><a href="https://docs.seismic.systems/">Documentation</a></li></ul>
            </div>
            <div class="footer-links gsap-blur-reveal footer-col">
                <h4>Community</h4>
                <ul><li><a href="https://x.com/SeismicSys">@SeismicSys</a></li><li><a href="https://discord.gg/seismic">Discord</a></li></ul>
            </div>
        </div>
    </footer>

    <!-- GSAP Animation Logic (Advanced Physics) -->
    <script>
        document.addEventListener("DOMContentLoaded", (event) => {{
            gsap.registerPlugin(ScrollTrigger);
            
            // 1. Smart Navbar Logic
            let lastScrollY = window.scrollY;
            const nav = document.querySelector('nav');
            
            window.addEventListener('scroll', () => {{
                if (window.scrollY > 50) {{
                    nav.classList.add('nav-scrolled');
                }} else {{
                    nav.classList.remove('nav-scrolled');
                }}
                
                if (window.scrollY > lastScrollY && window.scrollY > 200) {{
                    // Scrolling down
                    nav.classList.add('nav-hidden');
                }} else {{
                    // Scrolling up
                    nav.classList.remove('nav-hidden');
                }}
                lastScrollY = window.scrollY;
            }});
            
            // 2. Parallax Effects for Multi-Layer Depth
            // Background ambient shapes parallax (moves very slow)
            gsap.to(".ambient-1", {{
                y: 100,
                ease: "none",
                scrollTrigger: {{
                    trigger: "body",
                    start: "top top",
                    end: "bottom top",
                    scrub: 1.5 // Smooth scrubbing
                }}
            }});
            
            // Hero foreground parallax (moves up faster than scroll)
            gsap.to(".nv-hero-content", {{
                y: -80,
                ease: "none",
                scrollTrigger: {{
                    trigger: ".nv-hero",
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }}
            }});
            
            // 3. Staggered Blur-to-Clear Reveals
            
            // Universal reveal function for all .gsap-blur-reveal elements
            const revealElements = gsap.utils.toArray('.gsap-blur-reveal');
            revealElements.forEach((elem) => {{
                gsap.to(elem, {{
                    scrollTrigger: {{
                        trigger: elem,
                        start: "top 85%", // Trigger when top of element hits 85% down viewport
                        toggleActions: "play none none reverse"
                    }},
                    autoAlpha: 1, // Handles both opacity and visibility
                    y: 0,
                    filter: "blur(0px)",
                    duration: 1.2,
                    ease: "power3.out"
                }});
            }});
            
            // 4. Parallax Scale-In for the Globe Section
            gsap.to(".gsap-parallax-scale", {{
                scrollTrigger: {{
                    trigger: "#ecosystem",
                    start: "top 90%",
                    end: "top 30%",
                    scrub: 1
                }},
                scale: 1,
                opacity: 1,
                ease: "power2.out"
            }});
            
            // 5. Staggered Footer
            gsap.fromTo(".footer-col",
                {{ autoAlpha: 0, y: 30 }},
                {{ 
                    autoAlpha: 1, y: 0, duration: 0.8, stagger: 0.15, ease: "power2.out",
                    scrollTrigger: {{ trigger: "footer", start: "top 95%" }}
                }}
            );
        }});
    </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Syntra Dark Blue Theme applied successfully!")
