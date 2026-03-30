import codecs
import re

file_path = 'c:/Users/lonea/Downloads/seismic-mainnet.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    text = f.read()

# 1. Inject Bento CSS before </style>
css = """
        /* Outcrowd Bento Grid Section */
        .bento-section { background-color: #030303; color: #ffffff; font-family: 'Syne', sans-serif; position: relative; z-index: 2; padding: 140px 0; overflow: hidden; display: flex; justify-content: center; }
        .bento-grid-container { max-width: 1200px; width: 100%; display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: minmax(280px, auto); gap: 24px; padding: 0 24px; position: relative; }
        .bento-bg-circles { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 140vw; height: 140vw; display: grid; grid-template-columns: repeat(6, 1fr); gap: 40px; opacity: 0.15; z-index: 0; pointer-events: none; }
        .bento-bg-circles div { background: #1a1a24; border-radius: 50%; width: 100%; aspect-ratio: 1/1; box-shadow: inset -10px -10px 30px rgba(0,0,0,0.5); }
        .bento-header-card { grid-column: span 4; padding: 40px 0 60px 0; z-index: 1; text-align: center;}
        .bento-header-card h2 { font-size: 56px; font-weight: 800; line-height: 1.1; letter-spacing: -2px; color: #ffffff; margin-bottom: 20px; }
        .bento-header-pill { display: inline-flex; align-items: center; gap: 8px; background: rgba(255,255,255,0.05); padding: 8px 16px; border-radius: 100px; font-family: 'JetBrains Mono', monospace; font-size: 13px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px; }
        .bento-card { border-radius: 32px; padding: 36px; position: relative; overflow: hidden; z-index: 1; transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease; box-shadow: 0 10px 30px rgba(0,0,0,0.5); display: flex; flex-direction: column; justify-content: space-between; color: #000; }
        .bento-card:hover { transform: translateY(-8px) scale(1.02); box-shadow: 0 20px 40px rgba(0,0,0,0.8); z-index: 3; }
        .bento-card-plus { position: absolute; top: 24px; left: 24px; font-family: monospace; font-size: 20px; font-weight: 400; opacity: 0.6; }
        .bento-card-header { margin-top: 20px; margin-bottom: 24px; }
        .bento-card.tall { grid-row: span 2; }
        .bento-card.wide { grid-column: span 2; }
        .bento-card.large { grid-column: span 2; grid-row: span 2; }
        .bento-card h3 { font-size: 32px; font-weight: 700; line-height: 1.1; letter-spacing: -1px; margin-bottom: 16px; font-family: 'Syne', sans-serif;}
        .bento-card p { font-family: 'JetBrains Mono', monospace; font-size: 14px; line-height: 1.6; opacity: 0.8; font-weight: 400; }
        .card-purple { background: #b084e9; }
        .card-yellow { background: #FCE694; }
        .card-cyan { background: #85D4E0; }
        .card-pink { background: #F1B5CB; }
        .card-mint { background: #A7E4C4; }
        .card-dark { background: #1C1C1F; color: #fff; }
        .bento-btn { display: inline-flex; align-items: center; justify-content: space-between; width: 100%; background: rgba(0,0,0,0.1); color: inherit; padding: 16px 24px; border-radius: 100px; text-decoration: none; font-weight: 600; font-size: 15px; margin-top: 32px; transition: all 0.3s ease; cursor: pointer; border: 1px solid rgba(0,0,0,0.1); font-family: 'Syne', sans-serif;}
        .card-dark .bento-btn { background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1); }
        .bento-btn:hover { background: rgba(0,0,0,0.2); transform: scale(1.02); }
        .card-dark .bento-btn:hover { background: rgba(255,255,255,0.1); }
        .bento-card-logo-box { width: 64px; height: 64px; background: rgba(0,0,0,0.05); border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 32px; margin-bottom: 24px; }
        @media (max-width: 992px) { .bento-grid-container { grid-template-columns: repeat(2, 1fr); } .bento-card.tall { grid-row: span 1; } }
        @media (max-width: 768px) { .bento-grid-container { grid-template-columns: 1fr; } .bento-card.wide, .bento-card.large { grid-column: span 1; } .bento-header-card h2 { font-size: 40px; } }
"""
if "/* Outcrowd Bento Grid Section */" not in text:
    text = text.replace('    </style>', css + '\n    </style>')

html = """
    <!-- Outcrowd Bento Grid Section -->
    <section class="bento-section" id="value">
        <div class="bento-bg-circles">
            <div></div><div></div><div></div><div></div><div></div><div></div>
            <div></div><div></div><div></div><div></div><div></div><div></div>
            <div></div><div></div><div></div><div></div><div></div><div></div>
            <div></div><div></div><div></div><div></div><div></div><div></div>
        </div>

        <div class="bento-grid-container">
            <div class="bento-header-card scroll-reveal">
                <div class="bento-header-pill">THE PRIVACY LAYER</div>
                <h2>Bridging Web2 and Web3<br>with privacy-first fintech.</h2>
            </div>

            <!-- Blend: Tall Cyan -->
            <div class="bento-card tall card-cyan scroll-reveal" style="transition-delay: 0.1s;">
                <div class="bento-card-plus">+</div>
                <div>
                    <div class="bento-card-header">
                        <img src="https://blend.money/favicon.ico" alt="Blend" style="width: 48px; border-radius: 12px; margin-bottom: 20px;">
                        <h3>Blend</h3>
                    </div>
                    <p>Treasury-as-a-service for fintechs using private multi-currency accounts and robust yield instruments.</p>
                </div>
                <a href="https://blend.money/" target="_blank" class="bento-btn">Visit Blend <span>↗</span></a>
            </div>

            <!-- Encrypted DeFi: Large Purple -->
            <div class="bento-card large card-purple scroll-reveal" style="transition-delay: 0.2s;">
                <div class="bento-card-plus">+</div>
                <div>
                    <div class="bento-card-logo-box">🔒</div>
                    <h3>Encrypted DeFi Primitives</h3>
                    <p style="font-size: 16px;">Finally build private lending, swaps, and treasuries that real-world institutions will actively use without fear of public snooping. Compute seamlessly over shared private state.</p>
                </div>
                <div class="bento-btn" style="width: auto; align-self: flex-start; padding: 16px 40px;">Build Privacy <span>→</span></div>
            </div>

            <!-- Cred: Yellow -->
            <div class="bento-card card-yellow scroll-reveal" style="transition-delay: 0.3s;">
                <div class="bento-card-plus">+</div>
                <div style="margin-top:20px;">
                    <h3>Cred</h3>
                    <p>Private credit & working capital. Underwriting and lending for real-world businesses with zero data leaks.</p>
                </div>
                <a href="#" class="bento-btn">Explore Cred <span>↗</span></a>
            </div>

            <!-- vend Money: Pink -->
            <div class="bento-card card-pink scroll-reveal" style="transition-delay: 0.4s;">
                <div class="bento-card-plus">+</div>
                <div style="margin-top:20px;">
                    <h3>Vend Money</h3>
                    <p>Infrastructure for autonomous commerce. Self-financing machines powered by revenue-based credit.</p>
                </div>
                <a href="#" class="bento-btn">Vend Platform <span>↗</span></a>
            </div>

            <!-- Brookwell: Mint -->
            <div class="bento-card wide card-mint scroll-reveal" style="transition-delay: 0.5s;">
                <div class="bento-card-plus">+</div>
                <div style="margin-top:20px;">
                    <h3>Brookwell</h3>
                    <p>Private stablecoin cash accounts. Earn DeFi yields while securely paying rent and payroll via normal channels.</p>
                </div>
                <a href="#" class="bento-btn" style="width: auto; align-self: flex-start;">View Brookwell <span>↗</span></a>
            </div>

            <!-- New Moats: Wide Dark -->
            <div class="bento-card wide card-dark scroll-reveal" style="transition-delay: 0.6s;">
                <div class="bento-card-plus" style="opacity: 0.3;">+</div>
                <div style="margin-top:20px;">
                    <h3>New Market Moats</h3>
                    <p>Privacy completely unblocks entry into finance, healthcare, identity, and supply chain solutions. Once private balances and data live on Seismic, a winner-take-most privacy moat creates massive long-term stickiness.</p>
                </div>
                <a href="#" class="bento-btn" style="width: auto; align-self: flex-start;">Learn More <span>→</span></a>
            </div>
        </div>
    </section>
"""

# Replace the previous .rox-dark-section with the id="value" 
pattern = r'<!-- Value Section \(Rox Inspired\).*?</section>'
if re.search(pattern, text, re.DOTALL):
    text = re.sub(pattern, html, text, flags=re.DOTALL)
else:
    print("Could not find Rox Inspired pattern!")

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(text)

print("done")
