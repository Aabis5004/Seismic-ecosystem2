import codecs
import re

f = 'c:/Users/lonea/Downloads/seismic-mainnet.html'
text = codecs.open(f, 'r', 'utf-8').read()

new_css = """
        /* Rox.com Inspired Sections */
        .rox-dark-section { background-color: #000000; color: #ffffff; font-family: 'JetBrains Mono', monospace; position: relative; z-index: 2; padding: 120px 0; border-top: 1px solid rgba(255,255,255,0.05); }
        .rox-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 80px; }
        .rox-card { background: #050505; border: 1px solid rgba(255,255,255,0.06); border-radius: 16px; padding: 48px; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: flex-start; }
        .rox-card::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(800px circle at top left, rgba(255,255,255,0.03), transparent); pointer-events: none; }
        .rox-card:hover { border-color: rgba(255,255,255,0.15); transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,0.8); }
        .rox-card-icon { font-size: 32px; margin-bottom: 24px; display: inline-block; background: rgba(255,255,255,0.05); width: 60px; height: 60px; border-radius: 50%; text-align: center; line-height: 60px; }
        .rox-card h3 { font-family: 'Syne', sans-serif; font-size: 32px; font-weight: 600; margin-bottom: 20px; letter-spacing: -1px; color: #ffffff; }
        .rox-card p { color: rgba(255,255,255,0.6); font-size: 15px; line-height: 1.7; margin-bottom: 30px; }
        .rox-header { text-align: center; margin-bottom: 80px; }
        .rox-pill { display: inline-flex; align-items: center; gap: 8px; border: 1px solid rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 100px; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px; color: rgba(255,255,255,0.8); }
        .rox-pill .dot { width: 6px; height: 6px; border-radius: 50%; background: #00ff9f; box-shadow: 0 0 10px #00ff9f; }
        .rox-header h2 { font-family: 'Syne', sans-serif; font-size: 56px; font-weight: 600; line-height: 1.1; letter-spacing: -2px; }
        .rox-backers { padding: 80px 0; border-top: 1px solid rgba(255,255,255,0.05); }
        .backers-grid-rox { display: flex; flex-wrap: wrap; justify-content: center; gap: 60px; align-items: center; margin-top: 60px; }
        .backer-item { font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 700; color: rgba(255,255,255,0.4); letter-spacing: -1px; transition: all 0.3s ease; cursor: default; }
        .backer-item:hover { color: #ffffff; transform: scale(1.05); }
        .rox-footer { background: #000000; padding: 80px 0 40px; border-top: 1px solid rgba(255,255,255,0.05); }
        .footer-grid-rox { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 40px; }
        .footer-brand-rox { font-family: 'Syne', sans-serif; font-size: 32px; font-weight: 800; color: #fff; margin-bottom: 20px; }
        .footer-col h4 { font-family: 'Syne', sans-serif; color: #ffffff; margin-bottom: 24px; font-size: 16px; }
        .footer-col ul { list-style: none; padding: 0; }
        .footer-col ul li { margin-bottom: 12px; }
        .footer-col ul li a { color: rgba(255,255,255,0.5); text-decoration: none; font-size: 14px; transition: color 0.2s ease; }
        .footer-col ul li a:hover { color: #ffffff; }
        .rox-copyright { margin-top: 80px; padding-top: 40px; border-top: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; color: rgba(255,255,255,0.4); font-size: 13px; }
        @media (max-width: 768px) { .rox-grid { grid-template-columns: 1fr; } .footer-grid-rox { grid-template-columns: 1fr; gap: 60px; } .rox-header h2 { font-size: 40px; } }
"""
text = text.replace('    </style>', new_css + '    </style>')

text = re.sub(r' +<!-- Value Section \(Sellix Inspired\).*?</footer>', '', text, flags=re.DOTALL)

new_html = """
    <!-- Value Section (Rox Inspired) -->
    <section class="rox-dark-section" id="value">
        <div class="container">
            <div class="rox-header scroll-reveal">
                <div class="rox-pill"><div class="dot"></div> THE PRIVACY LAYER</div>
                <h2>Bridging Web2 and Web3<br>with privacy-first fintech</h2>
            </div>
            <div class="rox-grid">
                <div class="rox-card scroll-reveal">
                    <div class="rox-card-icon">🏦</div>
                    <h3>Brookwell & Blend</h3>
                    <p><strong>Brookwell:</strong> Private stablecoin cash accounts. Earn DeFi yields while paying rent and payroll via normal channels securely.</p>
                    <p><strong>Blend:</strong> Treasury-as-a-service for fintechs using private multi-currency accounts and robust yield instruments.</p>
                </div>
                <div class="rox-card scroll-reveal">
                    <div class="rox-card-icon">🤝</div>
                    <h3>Cred & Vend Money</h3>
                    <p><strong>Cred:</strong> Private credit & working capital. Underwriting and lending for real-world businesses with zero data leaks.</p>
                    <p><strong>Vend Money:</strong> Infrastructure for autonomous commerce. Self-financing machines powered by revenue-based credit.</p>
                </div>
                <div class="rox-card scroll-reveal">
                    <div class="rox-card-icon">🔒</div>
                    <h3>Encrypted DeFi Primitives</h3>
                    <p>Finally build private lending, swaps, and treasuries that real-world institutions will actively use without fear of public snooping. Compute seamlessly over shared private state.</p>
                </div>
                <div class="rox-card scroll-reveal">
                    <div class="rox-card-icon">🛡️</div>
                    <h3>New Market Moats</h3>
                    <p>Privacy completely unblocks entry into finance, healthcare, identity, and supply chain solutions. Once private balances and data live on Seismic, a winner-take-most privacy moat creates massive long-term stickiness.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Backers Section (Rox Inspired) -->
    <section class="rox-dark-section rox-backers">
        <div class="container">
            <div class="rox-header scroll-reveal" style="margin-bottom: 40px;">
                <h2 style="font-size: 32px;">Backed By The Best</h2>
            </div>
            <div class="backers-grid-rox scroll-reveal">
                <span class="backer-item">a16z crypto</span>
                <span class="backer-item">Polychain</span>
                <span class="backer-item">Galaxy Digital</span>
                <span class="backer-item">IOSG VC</span>
                <span class="backer-item">Electric Capital</span>
                <span class="backer-item">Multicoin</span>
                <span class="backer-item">Alliance</span>
                <span class="backer-item">1kx</span>
            </div>
        </div>
    </section>

    <!-- Clean Footer (Rox Inspired) -->
    <footer class="rox-footer">
        <div class="container">
            <div class="footer-grid-rox scroll-reveal">
                <div class="footer-col" style="padding-right: 40px;">
                    <div class="footer-brand-rox">SEISMIC</div>
                    <p style="color: rgba(255,255,255,0.5); font-size: 14px; line-height: 1.6;">
                        Building the future of privacy-preserving blockchain infrastructure. Native encryption for a secure, decentralized world.
                    </p>
                </div>
                <div class="footer-col">
                    <h4>Product</h4>
                    <ul>
                        <li><a href="#ecosystem">Ecosystem</a></li>
                        <li><a href="#">Mainnet</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="https://docs.seismic.systems" target="_blank">Documentation</a></li>
                        <li><a href="#">Whitepaper</a></li>
                        <li><a href="#">Blog</a></li>
                        <li><a href="#">Support</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Community</h4>
                    <ul>
                        <li><a href="https://twitter.com/SeismicSys" target="_blank">Twitter</a></li>
                        <li><a href="#">Discord</a></li>
                        <li><a href="#">GitHub</a></li>
                        <li><a href="#">Forum</a></li>
                    </ul>
                </div>
            </div>
            <div class="rox-copyright scroll-reveal">
                <span>&copy; 2026 Seismic. All rights reserved.</span>
                <div style="display: flex; gap: 24px;">
                    <a href="#" style="color: inherit; text-decoration: none;">Privacy Policy</a>
                    <a href="#" style="color: inherit; text-decoration: none;">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>
"""

text = text.replace('</body>', new_html + '</body>')
codecs.open(f, 'w', 'utf-8').write(text)
print("SUCCESS")
