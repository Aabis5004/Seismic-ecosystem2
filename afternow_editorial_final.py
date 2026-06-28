import json

expanded_projects = [
    {
        "title": "Blend", 
        "desc": "Treasury-as-a-service for fintechs using private multi-currency accounts and robust yield instruments.", 
        "long_desc": "Blend brings sophisticated treasury management to growing fintechs. By leveraging Seismic's private layer, Blend offers multi-currency cash sweeps, automated yield generation, and complete data privacy for corporate treasuries.",
        "link_url": "https://blend.money/", "link_text": "VISIT BLEND \u2192", 
        "logo": "<img src=\"https://framerusercontent.com/images/oJ7QVYoyXBbQ4HvAmIeq5U7AGpo.png\" alt=\"Blend\">",
        "status": "MAINNET LIVE", "progress": 100, "metric1": "$4.2B", "metric1_label": "PROCESSED", "metric2": "120+", "metric2_label": "INSTITUTIONS"
    },
    {
        "title": "Vend", 
        "desc": "Infrastructure for autonomous commerce. Self-financing machines powered by revenue-based credit.",
        "long_desc": "Vend is revolutionizing the machine economy. Using encrypted data rails, autonomous vending machines and kiosks can instantly secure financing based on verified, completely private revenue streams.",
        "link_url": "https://vend.money/", "link_text": "VISIT VEND \u2192", 
        "logo": "<img src=\"https://framerusercontent.com/images/SARuWkuMvBKRbeQeXHS7HCejxQw.png\" alt=\"Vend\">",
        "status": "BETA", "progress": 75, "metric1": "8,500", "metric1_label": "ACTIVE MACHINES", "metric2": "$12M", "metric2_label": "FINANCED"
    },
    {
        "title": "Sedona", 
        "desc": "Your neobank. Your keys.", 
        "long_desc": "Sedona provides a consumer neobanking experience with self-custody at its core. Manage your fiat and crypto seamlessly without ever surrendering control of your assets or personal data.",
        "link_url": "https://sedona.fi/", "link_text": "EXPLORE SEDONA \u2192", 
        "logo": "<img src=\"https://sedona.fi/images/sedona-logo.svg\" alt=\"Sedona\">",
        "status": "MAINNET LIVE", "progress": 100, "metric1": "45K", "metric1_label": "USERS", "metric2": "$85M", "metric2_label": "TVL"
    },
    {
        "title": "Brookwell", 
        "desc": "Private stablecoin cash accounts. Earn DeFi yields while securely paying rent and payroll via normal channels.", 
        "long_desc": "Brookwell bridges the gap between decentralized yield and real-world utility. Hold your balance in high-yield stablecoins while routing payments directly to standard fiat bank accounts privately.",
        "link_url": "https://www.brookwell.com/", "link_text": "VIEW BROOKWELL \u2192", 
        "logo": "<img src=\"https://www.brookwell.com/_next/image?url=%2Flogo.png&w=1080&q=75\" alt=\"Brookwell\">",
        "status": "IN DEVELOPMENT", "progress": 40, "metric1": "Q4", "metric1_label": "EXPECTED LAUNCH", "metric2": "12K", "metric2_label": "WAITLIST"
    },
    {
        "title": "Cred Protocol", 
        "desc": "Private credit & working capital. Underwriting and lending for real-world businesses with zero data leaks.", 
        "long_desc": "Cred Protocol introduces zero-knowledge underwriting. Businesses can prove their cash flow and financial health to access on-chain credit pools without exposing sensitive trade secrets.",
        "link_url": "https://credprotocol.com/", "link_text": "EXPLORE CRED \u2192", 
        "logo": "<img src=\"https://framerusercontent.com/images/ly6CYDZguctn369Fter3suQOhA.png\" alt=\"Cred\">",
        "status": "TESTNET", "progress": 85, "metric1": "$250M", "metric1_label": "COMMITTED CAPITAL", "metric2": "1.2s", "metric2_label": "PROOF TIME"
    },
    {
        "title": "Specie", 
        "desc": "Modern banking for global businesses. Send, receive, and manage money worldwide with fast settlement across local and global rails.", 
        "long_desc": "Specie operates a next-generation clearing network. By leveraging Seismic's private layer, cross-border B2B payments settle instantly while complying with local data privacy regulations.",
        "link_url": "https://www.specie.finance/", "link_text": "EXPLORE SPECIE \u2192", 
        "logo": "<img src=\"https://framerusercontent.com/images/UgeAlOHZZ3FQwYhs7gAADiyTsio.svg\" alt=\"Specie\">",
        "status": "MAINNET LIVE", "progress": 100, "metric1": "14", "metric1_label": "SUPPORTED CORRIDORS", "metric2": "< 3s", "metric2_label": "SETTLEMENT"
    },
    {
        "title": "Via", 
        "desc": "Stablecoin-first finance. Borderless access to capital, seamless payments, and premium yield.", 
        "long_desc": "Via enables borderless commerce by natively integrating stablecoins into everyday financial operations, offering a secure yield engine and instant vendor payouts globally.",
        "link_url": "https://www.via.xyz/", "link_text": "EXPLORE VIA \u2192", 
        "logo": "<img src=\"https://framerusercontent.com/images/kztSbCmi83eGOrsXWs2bnEqc.png\" alt=\"Via\">",
        "status": "MAINNET LIVE", "progress": 100, "metric1": "20+", "metric1_label": "PARTNER NETWORKS", "metric2": "5.5%", "metric2_label": "AVG YIELD"
    },
    {
        "title": "Shift", 
        "desc": "The Membership That Pays You Back. Elite financial services, lifestyle privileges, and exclusive perks driven by real yield models.", 
        "long_desc": "Shift redefines premium card memberships. Instead of burning fees, your membership deposit earns private, on-chain yield that dynamically pays for luxury travel and lifestyle subscriptions.",
        "link_url": "https://www.shift-apply.com/", "link_text": "VISIT SHIFT \u2192", 
        "logo": "<img src=\"https://framerusercontent.com/images/H4Yn2rDLeq2wENXWMdowmAbKZs.png\" alt=\"Shift\">",
        "status": "PRIVATE BETA", "progress": 90, "metric1": "1,000", "metric1_label": "FOUNDING MEMBERS", "metric2": "TIER 1", "metric2_label": "PERKS ACTIVE"
    },
    {
        "title": "DashX", 
        "desc": "Cross-border payments powered by crypto. Accept USDC, track transactions, and withdraw INR globally through one unified stack.", 
        "long_desc": "DashX is the ultimate bridge for emerging markets. It enables merchants to accept global stablecoin payments and instantly off-ramp to local fiat currencies seamlessly.",
        "link_url": "https://dashx.xyz/", "link_text": "USE DASHX \u2192", 
        "logo": "<img src=\"https://framerusercontent.com/images/le7rHwmt4MoWogPPDnWwvEQo1sA.png\" alt=\"DashX\">",
        "status": "MAINNET LIVE", "progress": 100, "metric1": "$8.2M", "metric1_label": "MONTHLY VOLUME", "metric2": "0.1%", "metric2_label": "FX FEE"
    },
    {
        "title": "Avvio",
        "desc": "Global accounts for digital life. Save, invest, and spend your money worldwide with yield.",
        "long_desc": "Avvio offers an integrated borderless financial stack. Powered by Seismic's private layer, users can manage global accounts and earn high yields on cash reserves with fully protected financial records.",
        "link_url": "https://avvio.xyz/join",
        "link_text": "JOIN AVVIO \u2192",
        "logo": "<img src=\"https://framerusercontent.com/images/RaWkyzF3tA1zcBZe0YsE8QZLA.png\" alt=\"Avvio\">",
        "status": "IN DEVELOPMENT",
        "progress": 60,
        "metric1": "7.0%",
        "metric1_label": "MAX APY",
        "metric2": "Q4",
        "metric2_label": "EXPECTED LAUNCH"
    },
    {
        "title": "Meow",
        "desc": "Modern business banking for AI agents and global teams. Payments, yield, and treasury.",
        "long_desc": "Meow is a compliant banking and treasury platform built for global startups and AI agents. In partnership with Seismic, Meow implements secure, end-to-end data encryption for confidential treasury sweeps and transactions.",
        "link_url": "https://www.meow.com/",
        "link_text": "EXPLORE MEOW \u2192",
        "logo": "<img src=\"https://www.meow.com/apple-touch-icon.png\" alt=\"Meow\">",
        "status": "MAINNET LIVE",
        "progress": 100,
        "metric1": "$1.2B+",
        "metric1_label": "TOTAL DEPOSITS",
        "metric2": "3.96%",
        "metric2_label": "TARGET YIELD"
    }
]

import re

marquee_items = []
for p in expanded_projects:
    title = p["title"]
    img_html = p["logo"]
    
    if title == "Vend":
        img_html = img_html.replace("<img ", "<img style=\"filter: brightness(0);\" ")
        
    if title in ["Avvio", "Meow", "Brookwell"]: # These logos are just icons without wordmarks
        item_html = f'''
            <div class="marquee-item">
                {img_html}
                <span class="marquee-item-text">{title}</span>
            </div>
        '''
    else:
        item_html = f'''
            <div class="marquee-item">
                {img_html}
            </div>
        '''
    marquee_items.append(item_html)

marquee_html_base = "".join(marquee_items)
marquee_html = marquee_html_base + marquee_html_base

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seismic | The Private Layer for Web3 & Fintech</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    
    <!-- GSAP for Smooth Animations -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    
    <style>
        :root {{
            --bg-main: #F4F1EA;
            --bg-card: #FFFFFF;
            --text-main: #1A1A1A;
            --text-sub: #706E6A;
            --accent-green: #1A1A1A; /* Primary solid accent */
            --accent-yellow: #CF9B4E; /* Highlight accent */
            --accent-teal: #706E6A;
            --border-main: rgba(26, 26, 26, 0.1);
            
            --font-display: 'Space Grotesk', sans-serif;
            --font-body: 'Inter', sans-serif;
            --font-mono: 'Space Mono', monospace;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: var(--font-body); 
            background: var(--bg-main);
            color: var(--text-main); 
            overflow-x: hidden; 
            min-height: 100vh;
        }}

        /* Smooth Scroll & GSAP Initial States */
        html.lenis, html.lenis body {{ height: auto; width: 100vw; overflow-x: hidden; }}
        .lenis.lenis-smooth {{ scroll-behavior: auto !important; }}
        .lenis.lenis-smooth [data-scroll-container] {{ overflow: hidden; }}

        .scroll-reveal {{ opacity: 0; transform: translateY(40px) scale(0.97); filter: blur(8px); will-change: opacity, transform, filter; }}
        .hero-reveal {{ opacity: 0; transform: translateY(30px); filter: blur(8px); will-change: opacity, transform, filter; }}
        .footer-col {{ opacity: 0; transform: translateY(30px); filter: blur(8px); }}
        .gsap-parallax-scale {{ transform: scale(0.95); opacity: 0; }}
        
        /* Navbar */
        nav {{ 
            position: fixed; top: 0; width: 100%; height: 90px; 
            display: flex; align-items: center; justify-content: center; 
            z-index: 1000; background: transparent !important; 
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important; 
            border-bottom: 1px solid transparent !important;
        }}
        .nav-inner {{ width: 100%; max-width: 1400px; display: flex; justify-content: space-between; align-items: center; padding: 0 40px; }}
        .nav-logo img {{ height: 24px; filter: none; }}
        .nav-links {{ display: flex; gap: 40px; align-items: center; }}
        .nav-links a {{ color: var(--text-main) !important; text-decoration: none; font-size: 14px; font-family: var(--font-mono); text-transform: uppercase; letter-spacing: -0.02em; transition: opacity 0.2s; }}
        .nav-links a:hover {{ opacity: 0.6; }}
        
        /* The Editorial Pill Button */
        .btn-editorial {{
            background: var(--accent-green); 
            color: #F4F1EA !important; 
            padding: 14px 28px; 
            border-radius: 100px; 
            font-family: var(--font-mono); 
            font-size: 14px; text-transform: uppercase; 
            text-decoration: none; 
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: inline-flex; align-items: center; gap: 10px;
            font-weight: 700;
        }}
        .btn-editorial:hover {{
            border-radius: 0px;
            background: var(--accent-yellow);
            color: #1A1A1A !important;
            box-shadow: 0 10px 20px rgba(207, 155, 78, 0.2);
        }}
        
        nav.nav-scrolled {{ 
            height: 70px !important; 
            background: rgba(244, 241, 234, 0.95) !important; 
            backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(26, 26, 26, 0.08) !important;
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

        /* Hero */
        .nv-hero {{ 
            position: relative; padding: 200px 40px 100px; 
            background: transparent; overflow: hidden; min-height: 70vh; 
            display: flex; flex-direction: column; justify-content: center;
            max-width: 1400px; margin: 0 auto;
        }}
        .hero-tag-list {{ display: flex; gap: 8px; margin-bottom: 32px; }}
        .tag-item {{ 
            background: var(--bg-card); 
            border: 1px solid var(--border-main); 
            padding: 8px 16px; 
            font-family: var(--font-mono); 
            font-size: 12px; 
            text-transform: uppercase; 
            transition: all 0.3s;
        }}
        .tag-item:nth-child(odd) {{ border-radius: 100px; }}
        .tag-item:nth-child(even) {{ border-radius: 0px; }}
        .tag-item:hover {{ border-radius: 0px !important; background: var(--accent-green); color: var(--bg-main); }}

        
        h1 {{ font-family: var(--font-display); font-size: clamp(3.625rem, 2.06rem + 5.217vw, 6.625rem); font-weight: 600; line-height: 1.05; letter-spacing: -0.05em; color: var(--text-main); margin-bottom: 24px; max-width: 1100px; }}
        .nv-hero-subtitle {{ font-size: clamp(1rem, 0.935rem + 0.217vw, 1.25rem); color: var(--text-sub); line-height: 1.5; margin-bottom: 48px; max-width: 650px; font-weight: 400; }}
        
        /* Marquee */
        .nv-marquee-section {{ padding: 60px 0; background: var(--bg-card); overflow: hidden; position: relative; z-index: 10; border-top: 1px solid var(--border-main); border-bottom: 1px solid var(--border-main); }}
        .nv-marquee-track {{ display: flex; gap: 80px; width: max-content; animation: marquee 30s linear infinite; align-items: center; }}
        .marquee-item {{ display: flex; align-items: center; gap: 14px; opacity: 0.5; filter: grayscale(100%); transition: all 0.3s; cursor: pointer; }}
        .marquee-item:hover {{ opacity: 1; filter: none; }}
        .marquee-item img {{ height: 40px; object-fit: contain; }}
        .marquee-item-text {{ font-family: var(--font-display); font-size: 26px; font-weight: 700; color: var(--text-main); text-transform: uppercase; letter-spacing: -0.04em; margin-top: 2px; }}
        @keyframes marquee {{ 0% {{ transform: translateX(0); }} 100% {{ transform: translateX(-50%); }} }}

        /* Globe Base Layout */
        .globe-layout {{ display: flex; align-items: center; justify-content: space-between; max-width: 1400px; margin: 0 auto; padding: 120px 40px; }}
        .globe-wrapper {{ position: relative; width: 600px; height: 600px; flex-shrink: 0; }}
        
        /* Editorial Info Panel */
        .globe-info-panel {{ 
            width: 500px; min-height: 400px;
            background: rgba(255, 255, 255, 0.7); 
            border: 1px solid rgba(26, 26, 26, 0.08); 
            border-radius: 0px; padding: 48px; 
            color: var(--text-main); 
            z-index: 20; transform: translateY(0); 
            transition: opacity 0.4s, transform 0.4s; 
            cursor: pointer; position: relative; display: flex; flex-direction: column;
            box-shadow: 0 30px 60px rgba(26, 26, 26, 0.05);
            backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
        }}
        .globe-info-panel:hover {{
            transform: translateY(-4px);
            box-shadow: 0 40px 80px rgba(26, 26, 26, 0.08);
            border-color: rgba(26, 26, 26, 0.15);
        }}
        .globe-info-panel.morphing {{ opacity: 0; transform: translateY(10px); }}
        .globe-info-panel-logo {{ height: 60px; margin-bottom: 32px; display: flex; align-items: center; }}
        .globe-info-panel-logo img, .globe-info-panel-logo svg {{ max-height: 100%; max-width: 140px; filter: none; object-fit: contain; }}
        .globe-info-panel h3 {{ font-family: var(--font-display); font-size: clamp(1.875rem, 1.092rem + 2.609vw, 3.375rem); letter-spacing: -0.04em; margin-bottom: 16px; color: var(--text-main); line-height: 1.11; }}
        .globe-info-panel p {{ font-size: 16px; line-height: 1.5; color: var(--text-sub); margin-bottom: 40px; flex-grow: 1; }}

        /* HTML DOM Nodes for Globe */
        .globe-html-node {{ position: absolute; top: 0; left: 0; transform: translate(-50%, -50%); display: flex; flex-direction: column; align-items: center; gap: 8px; pointer-events: auto; cursor: pointer; transition: filter 0.3s; will-change: transform, opacity; z-index: 10; }}
        .html-node-glass {{ width: 68px; height: 68px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border-radius: 50%; display: flex; align-items: center; justify-content: center; padding: 14px; transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s; }}
        .html-node-glass img, .html-node-glass svg {{ width: 100%; height: 100%; object-fit: contain; }}
        .html-node-text {{ font-family: var(--font-mono); font-size: 14px; font-weight: 700; color: #FFFFFF; background: rgba(11, 8, 7, 0.85); border: 1px solid rgba(207, 155, 78, 0.3); padding: 6px 14px; border-radius: 6px; text-transform: uppercase; white-space: nowrap; box-shadow: 0 4px 12px rgba(0,0,0,0.5); opacity: 0; transform: translateY(-10px); transition: all 0.3s; }}
        .globe-html-node:hover .html-node-text {{ opacity: 1; transform: translateY(0); }}

        /* Modal Overlay */
        .modal-overlay {{
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(244, 241, 234, 0.85);
            backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px);
            z-index: 9999999;
            display: flex; align-items: center; justify-content: center;
            opacity: 1; visibility: visible;
            transition: opacity 0.4s ease, visibility 0.4s ease;
            padding: 20px;
        }}
        .modal-overlay.hidden {{ opacity: 0; visibility: hidden; pointer-events: none; }}
        
        /* Editorial Modal Content */
        .project-modal-content {{
            background: #FFFFFF;
            border: 1px solid rgba(26, 26, 26, 0.08);
            color: var(--text-main);
            width: 100%; max-width: 800px;
            padding: 60px;
            position: relative;
            transform: translateY(0);
            opacity: 1;
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease;
            box-shadow: 0 40px 80px rgba(26, 26, 26, 0.1);
            display: flex; flex-direction: column;
        }}
        .modal-overlay.hidden .project-modal-content {{ transform: translateY(40px); opacity: 0; }}
        
        .modal-close {{
            position: absolute; top: 30px; right: 30px;
            width: 40px; height: 40px;
            background: rgba(26, 26, 26, 0.03); border: 1px solid rgba(26, 26, 26, 0.08);
            display: flex; align-items: center; justify-content: center;
            cursor: pointer; transition: background 0.2s, border-radius 0.2s;
            border-radius: 100px;
        }}
        .modal-close:hover {{ border-radius: 0px; background: rgba(26, 26, 26, 0.08); }}
        .modal-close svg {{ width: 20px; height: 20px; fill: var(--text-main); }}
        
        .modal-header {{ display: flex; align-items: center; gap: 32px; margin-bottom: 40px; }}
        .modal-logo-box {{ width: 100px; height: 100px; background: rgba(26, 26, 26, 0.02); border: 1px solid rgba(26, 26, 26, 0.08); display: flex; align-items: center; justify-content: center; padding: 20px; flex-shrink: 0; }}
        .modal-logo-box img, .modal-logo-box svg {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
        .modal-title-area h2 {{ font-family: var(--font-display); font-size: clamp(1.875rem, 1.092rem + 2.609vw, 3.375rem); letter-spacing: -0.04em; color: var(--text-main); margin-bottom: 12px; }}
        .modal-status-tag {{ display: inline-block; padding: 6px 14px; background: var(--text-main); color: var(--bg-main); font-family: var(--font-mono); font-size: 12px; text-transform: uppercase; border: 1px solid var(--text-main); }}
        
        .modal-body p.modal-desc {{ font-size: 18px; color: var(--text-sub); line-height: 1.5; margin-bottom: 40px; }}
        
        .modal-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 40px; }}
        .modal-metric {{ border: 1px solid rgba(26, 26, 26, 0.08); padding: 24px; }}
        .modal-metric-val {{ font-family: var(--font-display); font-size: 40px; font-weight: 600; color: var(--text-main); margin-bottom: 8px; letter-spacing: -0.05em; line-height: 1; }}
        .modal-metric-lbl {{ font-family: var(--font-mono); font-size: 12px; color: var(--text-sub); text-transform: uppercase; }}
        
        .modal-progress-wrap {{ border: 1px solid rgba(26, 26, 26, 0.08); padding: 24px; margin-bottom: 40px; }}
        .modal-progress-header {{ display: flex; justify-content: space-between; margin-bottom: 16px; font-family: var(--font-mono); font-size: 12px; color: var(--text-sub); text-transform: uppercase; }}
        .modal-progress-bar-bg {{ width: 100%; height: 4px; background: rgba(26, 26, 26, 0.08); overflow: hidden; }}
        .modal-progress-bar-fill {{ height: 100%; background: var(--text-main); transition: width 1.5s cubic-bezier(0.16, 1, 0.3, 1); }}
        
        /* Footer */
        footer {{ background: #1A1A1A; padding: 80px 40px; color: #F4F1EA; position: relative; z-index: 10; border-top: 1px solid rgba(26, 26, 26, 0.1); }}
        .footer-grid {{ display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 60px; max-width: 1400px; margin: 0 auto; }}
        .footer-logo {{ font-family: var(--font-display); font-size: 24px; font-weight: 700; letter-spacing: -0.05em; margin-bottom: 24px; color: #F4F1EA; text-transform: uppercase; }}
        .footer-links h4 {{ font-family: var(--font-mono); font-size: 12px; margin-bottom: 24px; color: #CF9B4E; text-transform: uppercase; letter-spacing: 0px; }}
        .footer-links ul {{ list-style: none; }}
        .footer-links li {{ margin-bottom: 12px; }}
        .footer-links a {{ color: #C4C0B8; text-decoration: none; transition: color 0.2s; font-size: 15px; font-weight: 400; }}
        .footer-links a:hover {{ color: #FFFFFF; }}
        
        @media (max-width: 1024px) {{ 
            .globe-layout {{ flex-direction: column; gap: 60px; }} 
            .globe-wrapper {{ width: 350px; height: 350px; }} 
            .globe-core {{ width: 200px; height: 200px; }} 
            .orbit-node {{ width: 44px; height: 44px; margin: -22px 0 0 -22px; }} 
            .orbit-node img, .orbit-node svg {{ max-width: 28px; max-height: 28px; }} 
            .globe-info-panel {{ width: 100%; max-width: 500px; padding: 32px; }} 
            .footer-grid {{ grid-template-columns: 1fr; gap: 40px; }}
        }}
        /* Ecosystem Dark Overrides */
        #ecosystem {{
            background: #0B0807 !important;
            border-top: 1px solid rgba(207, 155, 78, 0.12) !important;
            border-bottom: 1px solid rgba(207, 155, 78, 0.12) !important;
        }}
        #ecosystem .globe-info-panel {{
            background: rgba(19, 16, 15, 0.85) !important;
            border: 1px solid rgba(207, 155, 78, 0.15) !important;
            color: #F3EBD6 !important;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.6) !important;
            backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
        }}
        #ecosystem .globe-info-panel h3 {{
            color: #F3EBD6 !important;
        }}
        #ecosystem .globe-info-panel p {{
            color: #C4C0B8 !important;
        }}
        #ecosystem .globe-info-panel-logo img, 
        #ecosystem .globe-info-panel-logo svg {{
            filter: brightness(0) invert(1) !important;
        }}
    </style>
</head>
<body>

    <!-- Minimal Preloader -->
    <div id="premium-preloader">
        <svg class="loader-svg" viewBox="0 0 100 100">
            <g>
                <circle class="blob-center" cx="50" cy="50" r="14" fill="#1A1A1A" />
                <circle class="blob-1" cx="28" cy="50" r="14" fill="#CF9B4E" />
                <circle class="blob-2" cx="72" cy="50" r="14" fill="#706E6A" />
            </g>
        </svg>
    </div>

    <nav>
        <div class="nav-inner">
            <a href="#" class="nav-logo">
                <img src="https://framerusercontent.com/images/RNHqhN9OPcfhYMA27iXglrnSM.svg" alt="Seismic">
            </a>
            <div class="nav-links">
                <a href="https://docs.seismic.systems/" target="_blank">Docs</a>
            </div>
        </div>
    </nav>

    <section class="nv-hero">
        <div class="hero-tag-list hero-reveal">
            <div class="tag-item">Infrastructure</div>
            <div class="tag-item">Ecosystem</div>
            <div class="tag-item">2026</div>
        </div>
        <h1 class="hero-reveal">Projects Building on Seismic</h1>
        <p class="nv-hero-subtitle hero-reveal">Explore the applications and teams shaping the future of encrypted blockchain infrastructure through a privacy first lens</p>
        <div style="display: flex; gap: 16px; margin-top: 24px;" class="hero-reveal">
            <a href="#ecosystem" class="btn-editorial">EXPLORE NETWORK &rarr;</a>
        </div>
    </section>

    <div class="nv-marquee-section scroll-reveal">
        <div class="nv-marquee-track">
            {marquee_html}
        </div>
    </div>

    <!-- 3D GLOBE SECTION WITH MODAL -->
    <section class="ecosystem-section" id="ecosystem" style="background: var(--bg-main); overflow: hidden; position: relative; border-top: 1px solid rgba(26, 26, 26, 0.08); border-bottom: 1px solid rgba(26, 26, 26, 0.08); transition: background 0.5s ease;">
        
        <div class="globe-layout gsap-parallax-scale">
            <div class="globe-wrapper" id="globeWrapper" style="display: flex; align-items: center; justify-content: center; position: relative;">
                <canvas id="globeCanvas" style="width: 100%; height: 100%; cursor: grab;"></canvas>
                <div id="globe-nodes-layer" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; overflow: visible;"></div>
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
                        <a href="#" id="modalLink" class="btn-editorial" target="_blank" style="display: flex; justify-content: center; width: 100%;">Visit Project</a>
                    </div>
                </div>
            </div>
        </div>
        
        <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.19/bundled/lenis.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const globeProjects = {json.dumps(expanded_projects)};
            const panel = document.getElementById('globeInfoPanel');
            const modal = document.getElementById('projectModal');
            const modalClose = document.getElementById('modalClose');
            const globeWrapper = document.getElementById('globeWrapper');

            // Project Colors Mapping (Visual Identities)
            const projectColors = {{
                "Blend": "#FFB800", "Vend": "#FF5C00", "Sedona": "#00F0FF",
                "Brookwell": "#10B981", "Cred Protocol": "#EF4444", "Specie": "#8B5CF6",
                "Via": "#3B82F6", "Shift": "#EC4899", "DashX": "#D946EF",
                "Avvio": "#10E7E2", "Meow": "#FF6B00"
            }};

            // === THREE.JS SCENE SETUP ===
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 1000);
            camera.position.set(0, 0, 4.8); // Closer camera for larger globe visual

            const canvas = document.getElementById('globeCanvas');
            const renderer = new THREE.WebGLRenderer({{ canvas: canvas, antialias: true, alpha: true }});
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            renderer.setClearColor(0x000000, 0);
            renderer.outputEncoding = THREE.sRGBEncoding;

            function onResize() {{
                const rect = globeWrapper.getBoundingClientRect();
                camera.aspect = rect.width / rect.height;
                camera.updateProjectionMatrix();
                renderer.setSize(rect.width, rect.height);
            }}
            window.addEventListener('resize', onResize);
            onResize();

            // === HOLOGRAPHIC DIGITAL GLOBE ===
            const GLOBE_R = 1.6;
            const globeGroup = new THREE.Group();
            scene.add(globeGroup);

            // 1. Atmosphere halo glow (custom shader - edge only, dark center)
            const atmosMat = new THREE.ShaderMaterial({{
                vertexShader: `varying vec3 vNormal; void main() {{ vNormal = normalize(normalMatrix * normal); gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }}`,
                fragmentShader: `varying vec3 vNormal; void main() {{ float intensity = pow(1.0 - abs(vNormal.z), 3.0); gl_FragColor = vec4(0.81, 0.61, 0.31, 1.0) * intensity * 0.75; }}`,
                blending: THREE.AdditiveBlending,
                side: THREE.BackSide,
                transparent: true
            }});
            const atmos = new THREE.Mesh(new THREE.SphereGeometry(GLOBE_R * 1.15, 64, 64), atmosMat);
            globeGroup.add(atmos);

            // 2. Wireframe grid
            const gridMat = new THREE.MeshBasicMaterial({{
                color: 0xCF9B4E,
                wireframe: true,
                transparent: true,
                opacity: 0.08
            }});
            const grid = new THREE.Mesh(new THREE.SphereGeometry(GLOBE_R, 30, 20), gridMat);
            globeGroup.add(grid);

            // 3. Dotted Continent Points
            const dotGeo = new THREE.BufferGeometry();
            const positions = [];
            const colors = [];
            const opacities = [];

            const continents = [
                {{ lat: 0.6, lon: -1.7, radius: 0.9 }},   // North America
                {{ lat: -0.2, lon: -1.1, radius: 0.8 }},  // South America
                {{ lat: 0.8, lon: 0.6, radius: 1.1 }},    // Eurasia
                {{ lat: 0.1, lon: 0.3, radius: 0.8 }},    // Africa
                {{ lat: -0.4, lon: 2.2, radius: 0.7 }}     // Australia
            ];

            const pointCount = 1800;
            const goldenRatio = (1 + Math.sqrt(5)) / 2;
            for (let i = 0; i < pointCount; i++) {{
                const y = 1 - (i / (pointCount - 1)) * 2;
                const radiusAtY = Math.sqrt(1 - y * y);
                const theta = i * 2 * Math.PI / goldenRatio;
                
                const nx = Math.cos(theta) * radiusAtY;
                const ny = y;
                const nz = Math.sin(theta) * radiusAtY;
                
                // Convert unit coords to spherical angles for continent test
                const lat = Math.asin(ny);
                const lon = Math.atan2(nz, nx);
                
                let isLand = false;
                for (let c of continents) {{
                    const dLat = lat - c.lat;
                    const dLon = lon - c.lon;
                    if (dLat * dLat + dLon * dLon < c.radius * c.radius) {{
                        isLand = true;
                        break;
                    }}
                }}

                const r = GLOBE_R * 1.005;
                positions.push(nx * r, ny * r, nz * r);

                const c = new THREE.Color(isLand ? 0xCF9B4E : 0xCF9B4E);
                colors.push(c.r, c.g, c.b);
                opacities.push(isLand ? 0.65 : 0.08);
            }}

            dotGeo.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
            dotGeo.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
            dotGeo.setAttribute('opacity', new THREE.Float32BufferAttribute(opacities, 1));

            // Custom Points shader to support individual point opacities
            const pointsMat = new THREE.ShaderMaterial({{
                vertexShader: `
                    attribute vec3 color;
                    attribute float opacity;
                    varying vec3 vColor;
                    varying float vOpacity;
                    void main() {{
                        vColor = color;
                        vOpacity = opacity;
                        vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
                        gl_PointSize = 12.0 / -mvPosition.z;
                        gl_Position = projectionMatrix * mvPosition;
                    }}
                `,
                fragmentShader: `
                    varying vec3 vColor;
                    varying float vOpacity;
                    void main() {{
                        float dist = length(gl_PointCoord - vec2(0.5));
                        if (dist > 0.5) discard;
                        gl_FragColor = vec4(vColor, vOpacity);
                    }}
                `,
                transparent: true,
                depthWrite: false
            }});

            const points = new THREE.Points(dotGeo, pointsMat);
            globeGroup.add(points);

            // 4. Floating space particles
            const starGeo = new THREE.BufferGeometry();
            const starPos = [];
            for (let i = 0; i < 200; i++) {{
                const r = GLOBE_R * (1.2 + Math.random() * 1.5);
                const t = Math.random() * Math.PI * 2;
                const p = Math.random() * Math.PI - Math.PI / 2;
                starPos.push(
                    r * Math.cos(p) * Math.cos(t),
                    r * Math.sin(p),
                    r * Math.cos(p) * Math.sin(t)
                );
            }}
            starGeo.setAttribute('position', new THREE.Float32BufferAttribute(starPos, 3));
            const starPoints = new THREE.Points(starGeo, new THREE.PointsMaterial({{
                color: 0xCF9B4E, size: 0.012, transparent: true, opacity: 0.25, sizeAttenuation: true
            }}));
            globeGroup.add(starPoints);

            // === LIGHTING ===
            scene.add(new THREE.AmbientLight(0xFFFFFF, 0.4));
            const keyLight = new THREE.DirectionalLight(0xF3EBD6, 0.8);
            keyLight.position.set(5, 3, 5);
            scene.add(keyLight);

            // === PROJECT NODES (HTML OVERLAYS) ===
            const projectNodes = [];
            const nodeGroup = new THREE.Group();
            globeGroup.add(nodeGroup);
            
            const htmlNodesLayer = document.getElementById('globe-nodes-layer');

            globeProjects.forEach((proj, i) => {{
                const N = globeProjects.length;
                const y = 1 - (2 * i) / (N - 1);
                const theta = Math.asin(y);
                const phi = i * 2.39996; // Golden angle
                
                const nx = Math.cos(theta) * Math.cos(phi);
                const ny = y;
                const nz = Math.cos(theta) * Math.sin(phi);
                const surfaceR = GLOBE_R * 1.02;

                const colorHex = projectColors[proj.title] || "#CF9B4E";
                const color = new THREE.Color(colorHex);

                // Invisible 3D Container (Anchor for HTML tracking and arcs)
                const container = new THREE.Group();
                const pos = new THREE.Vector3(nx * surfaceR, ny * surfaceR, nz * surfaceR);
                container.position.copy(pos);
                container.lookAt(0, 0, 0);
                container.rotateY(Math.PI);
                nodeGroup.add(container);

                // HTML Overlay Element
                const el = document.createElement('div');
                el.className = 'globe-html-node';
                el.innerHTML = `
                    <div class="html-node-glass" style="box-shadow: 0 10px 30px ${{colorHex}}40, inset 0 0 0 1px rgba(255,255,255,0.2);">
                        ${{proj.logo}}
                    </div>
                    <div class="html-node-text">${{proj.title}}</div>
                `;
                htmlNodesLayer.appendChild(el);
                
                // Interactions handled natively by HTML
                el.addEventListener('mouseenter', () => {{
                    hoveredNode = projectNodes[i];
                    updatePanel(proj);
                }});
                el.addEventListener('mouseleave', () => {{
                    if (hoveredNode === projectNodes[i]) hoveredNode = null;
                }});
                el.addEventListener('click', () => {{
                    openModal(proj);
                    focusCameraTarget = pos.clone().normalize().multiplyScalar(3.2);
                }});

                projectNodes.push({{
                    proj, container, el,
                    color, colorHex, pos, index: i,
                    revealScale: 0, targetReveal: 0,
                    hoverScale: 0, targetHover: 0
                }});
            }});

            // === CONNECTIVITY NETWORK ARCS ===
            const arcGroup = new THREE.Group();
            globeGroup.add(arcGroup);
            
            const activeArcs = [];

            // Draw curved arches between nodes
            for (let i = 0; i < projectNodes.length; i++) {{
                for (let j = i + 1; j < projectNodes.length; j++) {{
                    const nodeA = projectNodes[i];
                    const nodeB = projectNodes[j];
                    const d = nodeA.pos.distanceTo(nodeB.pos);
                    
                    if (d < GLOBE_R * 1.7) {{
                        const points = [];
                        const divisions = 40;
                        
                        for (let k = 0; k <= divisions; k++) {{
                            const t = k / divisions;
                            const p = new THREE.Vector3().lerpVectors(nodeA.pos, nodeB.pos, t);
                            p.normalize();
                            // Compute height offset (arch shape)
                            const h = GLOBE_R * (1.0 + Math.sin(t * Math.PI) * 0.18);
                            p.multiplyScalar(h);
                            points.push(p);
                        }}

                        const curve = new THREE.CatmullRomCurve3(points);
                        const pointsCurve = curve.getPoints(50);
                        const lineGeo = new THREE.BufferGeometry().setFromPoints(pointsCurve);
                        const lineMat = new THREE.LineBasicMaterial({{ color: 0xCF9B4E, transparent: true, opacity: 0.08 }});
                        const line = new THREE.Line(lineGeo, lineMat);
                        arcGroup.add(line);

                        activeArcs.push({{
                            line, lineMat, curve,
                            nodeA, nodeB,
                            targetOpacity: 0.08
                        }});
                    }}
                }}
            }}

            // === ENERGY PULSE PARTICLES ===
            const pulseParticles = [];
            const pulseGeo = new THREE.SphereGeometry(0.015, 8, 8);
            const pulseCount = 10;
            for (let k = 0; k < pulseCount; k++) {{
                const pulseMat = new THREE.MeshBasicMaterial({{ color: 0xCF9B4E, transparent: true, opacity: 0.9 }});
                const pulseMesh = new THREE.Mesh(pulseGeo, pulseMat);
                pulseMesh.visible = false;
                scene.add(pulseMesh);
                pulseParticles.push({{
                    mesh: pulseMesh, mat: pulseMat,
                    arc: null, progress: Math.random(),
                    speed: 0.2 + Math.random() * 0.3
                }});
            }}

            // === SCROLL REVEAL ===
            const revealState = {{ progress: 0 }};
            gsap.to(revealState, {{
                progress: 1,
                scrollTrigger: {{
                    trigger: "#ecosystem",
                    start: "top 75%",
                    end: "top 15%",
                    scrub: 1.5
                }}
            }});

            // === ROTATION & DRAGGING WITH INERTIA ===
            let rotY = 0, rotX = 0.3;
            let velY = 0.002, velX = 0;
            let isDragging = false;
            let prevMouseX = 0, prevMouseY = 0;
            let mouseX = 0, mouseY = 0; // Parallax coords
            
            let hoveredNode = null;
            let focusCameraTarget = null;

            const raycaster = new THREE.Raycaster();
            const mouse2d = new THREE.Vector2();

            renderer.domElement.addEventListener('mousedown', (e) => {{
                isDragging = true;
                prevMouseX = e.clientX;
                prevMouseY = e.clientY;
                renderer.domElement.style.cursor = 'grabbing';
            }});

            window.addEventListener('mousemove', (e) => {{
                const rect = renderer.domElement.getBoundingClientRect();
                mouseX = ((e.clientX - rect.left) / rect.width) * 2 - 1;
                mouseY = -((e.clientY - rect.top) / rect.height) * 2 + 1;

                if (isDragging) {{
                    const dx = e.clientX - prevMouseX;
                    const dy = e.clientY - prevMouseY;
                    velY = dx * 0.003;
                    velX = dy * 0.002;
                    prevMouseX = e.clientX;
                    prevMouseY = e.clientY;
                }}
            }});

            window.addEventListener('mouseup', () => {{
                isDragging = false;
                renderer.domElement.style.cursor = 'grab';
            }});

            // === SPECIFICATIONS MODAL ===
            let currentProj = null;
            function updatePanel(proj) {{
                if (currentProj && currentProj.title === proj.title) return;
                currentProj = proj;
                panel.classList.add('morphing');
                setTimeout(() => {{
                    panel.innerHTML = `
                        <div class="globe-info-panel-logo">${{proj.logo}}</div>
                        <h3>${{proj.title}}</h3>
                        <p>${{proj.desc}}</p>
                        <div class="btn-editorial" style="align-self: flex-start;">VIEW DETAILS &rarr;</div>
                    `;
                    panel.classList.remove('morphing');
                }}, 300);
            }}

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
                document.getElementById('modalProgressFill').style.width = '0%';
                
                document.getElementById('modalLink').href = proj.link_url;
                document.getElementById('modalLink').textContent = proj.link_text;
                
                modal.classList.remove('hidden');
                
                setTimeout(() => {{
                    document.getElementById('modalProgressFill').style.width = proj.progress + '%';
                }}, 100);
            }}

            function closeModal() {{
                modal.classList.add('hidden');
                focusCameraTarget = null;
            }}

            modalClose.addEventListener('click', closeModal);
            modal.addEventListener('click', (e) => {{
                if (e.target === modal) closeModal();
            }});

            if (globeProjects.length > 0) {{
                updatePanel(globeProjects[0]);
            }}

            // === RENDER LOOP ===
            const clock = new THREE.Clock();

            function animate() {{
                requestAnimationFrame(animate);
                const dt = Math.min(clock.getDelta(), 0.05);
                const time = clock.getElapsedTime();

                // Rotate globe with inertia
                if (!isDragging) {{
                    velY *= 0.96;
                    velX *= 0.95;
                    // Auto rotation base speed
                    if (Math.abs(velY) < 0.0005 && !focusCameraTarget) {{
                        velY = 0.002;
                    }}
                }}
                rotY += velY;
                rotX += velX;
                rotX = Math.max(-1.1, Math.min(1.1, rotX));

                // Apply rotation matrices to group
                globeGroup.rotation.set(rotX, rotY, 0);

                // Smooth camera zoom and positioning
                const targetCamX = mouseX * 0.22;
                const targetCamY = mouseY * 0.15;
                if (focusCameraTarget) {{
                    camera.position.lerp(focusCameraTarget, 0.035);
                }} else {{
                    const defaultCam = new THREE.Vector3(targetCamX, targetCamY, 5.2);
                    camera.position.lerp(defaultCam, 0.035);
                }}
                camera.lookAt(0, 0, 0);

                // Subtle ambient particles rotation
                starPoints.rotation.y = time * 0.03;
                starPoints.rotation.x = Math.sin(time * 0.02) * 0.08;

                const widthHalf = canvas.clientWidth / 2;
                const heightHalf = canvas.clientHeight / 2;
                const camDir = camera.position.clone().normalize();
                const nodeWorldPos = new THREE.Vector3();

                // Staggered node scale & opacity reveal via HTML DOM projection
                projectNodes.forEach((n, idx) => {{
                    n.container.getWorldPosition(nodeWorldPos);
                    const nodeDir = nodeWorldPos.clone().normalize();
                    const dot = nodeDir.dot(camDir);
                    // Node is visible if facing the front hemisphere
                    const isFacing = dot > -0.15;
                    
                    // Only start showing when the scroll reveal is at least partially active
                    n.targetReveal = (isFacing && revealState.progress > 0.05) ? 1 : 0;
                    n.revealScale += (n.targetReveal - n.revealScale) * 0.045; // Smooth slow appearance

                    n.targetHover = (hoveredNode === n) ? 1 : 0;
                    n.hoverScale += (n.targetHover - n.hoverScale) * 0.085;

                    if (n.revealScale > 0.01) {{
                        n.el.style.display = 'flex';
                        
                        // 3D to 2D Screen projection
                        const projected = nodeWorldPos.clone().project(camera);
                        const x = (projected.x * widthHalf) + widthHalf;
                        const y = -(projected.y * heightHalf) + heightHalf;
                        
                        // Scale based on Z depth and hover
                        const depthScale = Math.max(0.6, 1.0 - (projected.z * 0.2));
                        const finalScale = n.revealScale * depthScale * (1.0 + n.hoverScale * 0.15);
                        
                        n.el.style.transform = `translate(-50%, -50%) translate(${{x}}px, ${{y}}px) scale(${{finalScale}})`;
                        n.el.style.opacity = n.revealScale;
                        n.el.style.zIndex = Math.round((1 - projected.z) * 100);

                        const glass = n.el.querySelector('.html-node-glass');
                        // Dim unselected nodes on hover
                        if (hoveredNode && hoveredNode !== n) {{
                            n.el.style.opacity = n.revealScale * 0.35;
                            n.el.style.filter = 'blur(3px)';
                        }} else {{
                            n.el.style.filter = 'none';
                            if (hoveredNode === n) {{
                                glass.style.boxShadow = `0 15px 40px ${{n.colorHex}}90, inset 0 0 0 1px rgba(255,255,255,0.6)`;
                                glass.style.background = 'rgba(255, 255, 255, 1.0)';
                            }} else {{
                                glass.style.boxShadow = `0 10px 30px ${{n.colorHex}}40, inset 0 0 0 1px rgba(255,255,255,0.2)`;
                                glass.style.background = 'rgba(255, 255, 255, 0.9)';
                            }}
                        }}
                    }} else {{
                        n.el.style.display = 'none';
                    }}
                }});

                // Staggered connection arcs reveal
                activeArcs.forEach(arc => {{
                    const bothRevealed = arc.nodeA.revealScale > 0.55 && arc.nodeB.revealScale > 0.55;
                    const hoverSelected = (hoveredNode === arc.nodeA || hoveredNode === arc.nodeB);
                    arc.targetOpacity = bothRevealed ? (hoverSelected ? 0.32 : 0.08) : 0;
                    arc.lineMat.opacity += (arc.targetOpacity - arc.lineMat.opacity) * 0.05;
                }});

                // Volumetric energy particles travel
                pulseParticles.forEach(p => {{
                    // Pick a random revealed arc if not currently active
                    if (!p.arc) {{
                        const eligibleArcs = activeArcs.filter(a => a.nodeA.revealScale > 0.8 && a.nodeB.revealScale > 0.8);
                        if (eligibleArcs.length > 0) {{
                            p.arc = eligibleArcs[Math.floor(Math.random() * eligibleArcs.length)];
                            p.progress = 0;
                            p.mesh.visible = true;
                        }}
                    }}

                    if (p.arc) {{
                        p.progress += dt * p.speed;
                        if (p.progress >= 1.0) {{
                            p.arc = null;
                            p.mesh.visible = false;
                        }} else {{
                            // Compute Bezier point in global coordinate space
                            const point = p.arc.curve.getPointAt(p.progress);
                            // Apply rotation matrix offset dynamically
                            point.applyEuler(globeGroup.rotation);
                            p.mesh.position.copy(point);
                            p.mat.opacity = Math.sin(p.progress * Math.PI) * 0.9;
                        }}
                    }}
                }});

                renderer.render(scene, camera);
            }}
            animate();

            // Preloader hide logic
            function hidePreloader() {{
                const p = document.getElementById('premium-preloader');
                if (p && !p.classList.contains('preloader-hidden')) {{
                    p.classList.add('preloader-hidden');
                    gsap.to(".hero-reveal", {{
                        opacity: 1, y: 0, filter: "blur(0px)", duration: 1.0,
                        ease: "power3.out", stagger: 0.15
                    }});
                }}
            }}
            window.addEventListener('load', () => {{ setTimeout(hidePreloader, 1000); }});
            if (document.readyState === 'complete') {{ setTimeout(hidePreloader, 1000); }}
        </script>

    </section>

    <footer>
        <div class="footer-grid">
            <div class="footer-col">
                <div class="footer-logo">SEISMIC</div>
                <p style="color: var(--text-sub); line-height: 1.6; font-size: 15px;">Native encryption for a secure, decentralized world.</p>
            </div>
            <div class="footer-col footer-links">
                <h4>Ecosystem</h4>
                <ul><li><a href="#ecosystem">Partners</a></li><li><a href="https://docs.seismic.systems/">Documentation</a></li></ul>
            </div>
            <div class="footer-col footer-links">
                <h4>Community</h4>
                <ul><li><a href="https://x.com/SeismicSys">@SeismicSys</a></li><li><a href="https://discord.gg/seismic">Discord</a></li></ul>
            </div>
        </div>
    </footer>

    <!-- GSAP Animation Logic -->
    <script>
        document.addEventListener("DOMContentLoaded", (event) => {{
            gsap.registerPlugin(ScrollTrigger);

            // Initialize Lenis for Smooth Scrolling
            const lenis = new Lenis({{
                duration: 1.2,
                easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
                direction: 'vertical',
                gestureDirection: 'vertical',
                smooth: true,
                mouseMultiplier: 1,
                smoothTouch: false,
                touchMultiplier: 2,
                infinite: false,
            }});

            lenis.on('scroll', ScrollTrigger.update);
            gsap.ticker.add((time) => {{ lenis.raf(time * 1000); }});
            gsap.ticker.lagSmoothing(0);
            
            // Advanced Staggered Scroll-Triggered Reveals
            ScrollTrigger.batch(".scroll-reveal", {{
                onEnter: batch => gsap.to(batch, {{
                    opacity: 1, y: 0, scale: 1, filter: "blur(0px)",
                    stagger: 0.15, duration: 1.2, ease: "power3.out"
                }}),
                start: "top 85%"
            }});
            
            ScrollTrigger.batch(".footer-col", {{
                onEnter: batch => gsap.to(batch, {{
                    opacity: 1, y: 0, filter: "blur(0px)",
                    stagger: 0.15, duration: 1.0, ease: "power3.out"
                }}),
                start: "top 90%"
            }});

            // Subdued Globe Parallax Effect
            gsap.to(".globe-wrapper", {{
                y: 100, // Move down slightly as you scroll past
                ease: "none",
                scrollTrigger: {{
                    trigger: "#ecosystem",
                    start: "top bottom",
                    end: "bottom top",
                    scrub: true
                }}
            }});
            
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
                    nav.classList.add('nav-hidden');
                }} else {{
                    nav.classList.remove('nav-hidden');
                }}
                lastScrollY = window.scrollY;
            }});
            
            // 2. Hero foreground parallax 
            gsap.to(".nv-hero h1", {{
                y: -60,
                ease: "none",
                scrollTrigger: {{
                    trigger: ".nv-hero",
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }}
            }});
            
            // 3. Marquee Reveal
            gsap.to(".gsap-reveal", {{
                scrollTrigger: {{
                    trigger: ".gsap-reveal",
                    start: "top 85%", 
                    toggleActions: "play none none reverse"
                }},
                autoAlpha: 1, 
                y: 0,
                duration: 1.0,
                ease: "power3.out"
            }});
            
            // 4. Parallax Scale-In for Globe
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

print("AfterNow Editorial Theme applied successfully!")
