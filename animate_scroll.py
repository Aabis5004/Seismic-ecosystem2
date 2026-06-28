import re

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Inject GSAP CDNs into <head>
if "gsap.min.js" not in content:
    head_injection = """
    <!-- GSAP for Smooth Animations -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    
    <style>
        /* GSAP Initial States */
        .gsap-reveal { opacity: 0; visibility: hidden; }
        
        /* Navbar Scroll States */
        nav { transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important; }
        nav.nav-scrolled { 
            height: 70px !important; 
            background: rgba(255, 255, 255, 0.8) !important; 
            backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
            border-bottom-color: transparent !important;
        }
        nav.nav-hidden { transform: translateY(-100%); }
        nav.nav-scrolled .nav-logo img { height: 28px !important; transition: height 0.4s; }
        
        /* Ambient Background Shapes for Hero */
        .ambient-shape { position: absolute; border-radius: 50%; filter: blur(60px); opacity: 0.5; pointer-events: none; z-index: 1; }
        .ambient-1 { width: 400px; height: 400px; background: #004D40; top: -100px; left: -100px; animation: floatShape 15s ease-in-out infinite alternate; }
        .ambient-2 { width: 500px; height: 500px; background: #00211d; bottom: -200px; right: -100px; animation: floatShape 20s ease-in-out infinite alternate-reverse; }
        @keyframes floatShape { 0% { transform: translate(0, 0) scale(1); } 100% { transform: translate(50px, 30px) scale(1.1); } }
        
        /* Ensure content sits above ambient shapes */
        .nv-hero-content { position: relative; z-index: 10; }
    </style>
</head>"""
    content = content.replace('</head>', head_injection)


# 2. Add GSAP Reveal Classes and Ambient Shapes to HTML
# Hero Content
content = content.replace('<div class="nv-hero-content">', 
    '<div class="ambient-shape ambient-1" data-speed="0.5"></div>\n        <div class="ambient-shape ambient-2" data-speed="0.8"></div>\n        <div class="nv-hero-content">')
content = content.replace('<h1>Projects Building on Seismic</h1>', '<h1 class="gsap-reveal">Projects Building on Seismic</h1>')
content = content.replace('<p class="nv-hero-subtitle">', '<p class="nv-hero-subtitle gsap-reveal">')
content = content.replace('<div style="display: flex; gap: 16px; justify-content: center;">', '<div style="display: flex; gap: 16px; justify-content: center;" class="gsap-reveal">')

# Marquee
content = content.replace('<div class="nv-marquee-section">', '<div class="nv-marquee-section gsap-reveal">')

# Section Header
content = content.replace('<h2 style="color: #fff; font-size: 52px; margin-bottom: 16px; font-family: \'Syne\', sans-serif;">Ecosystem Network</h2>',
    '<h2 class="gsap-reveal" style="color: #fff; font-size: 52px; margin-bottom: 16px; font-family: \'Syne\', sans-serif;">Ecosystem Network</h2>')
content = content.replace('<p style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px; margin: 0 auto;">Building the foundation for private, scalable financial services.</p>',
    '<p class="gsap-reveal" style="color: rgba(255,255,255,0.7); font-size: 18px; max-width: 600px; margin: 0 auto;">Building the foundation for private, scalable financial services.</p>')

# Footer Columns
content = content.replace('<div>\n                <div class="footer-logo">SEISMIC</div>', '<div class="gsap-reveal footer-col">\n                <div class="footer-logo">SEISMIC</div>')
content = content.replace('<div class="footer-links">', '<div class="footer-links gsap-reveal footer-col">')

# 3. Inject JS Logic
gsap_script = """
    <!-- GSAP Animation Logic -->
    <script>
        document.addEventListener("DOMContentLoaded", (event) => {
            gsap.registerPlugin(ScrollTrigger);
            
            // 1. Smart Navbar Logic
            let lastScrollY = window.scrollY;
            const nav = document.querySelector('nav');
            
            window.addEventListener('scroll', () => {
                if (window.scrollY > 50) {
                    nav.classList.add('nav-scrolled');
                } else {
                    nav.classList.remove('nav-scrolled');
                }
                
                if (window.scrollY > lastScrollY && window.scrollY > 200) {
                    // Scrolling down
                    nav.classList.add('nav-hidden');
                } else {
                    // Scrolling up
                    nav.classList.remove('nav-hidden');
                }
                lastScrollY = window.scrollY;
            });
            
            // 2. Parallax Effects
            // Hero background parallax
            gsap.to(".ambient-1", {
                y: 100,
                ease: "none",
                scrollTrigger: {
                    trigger: ".nv-hero",
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }
            });
            gsap.to(".ambient-2", {
                y: -150,
                ease: "none",
                scrollTrigger: {
                    trigger: ".nv-hero",
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }
            });
            
            // Hero content parallax (moves up slightly faster than scroll)
            gsap.to(".nv-hero-content", {
                y: -80,
                ease: "none",
                scrollTrigger: {
                    trigger: ".nv-hero",
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }
            });
            
            // 3. Staggered Blur-to-Clear Reveals
            
            // Hero elements animate in on load
            gsap.fromTo(".nv-hero .gsap-reveal", 
                { y: 40, autoAlpha: 0, scale: 0.95, filter: "blur(10px)" },
                { y: 0, autoAlpha: 1, scale: 1, filter: "blur(0px)", duration: 1.2, stagger: 0.15, ease: "power3.out", delay: 0.2 }
            );
            
            // Marquee Reveal
            gsap.fromTo(".nv-marquee-section.gsap-reveal",
                { autoAlpha: 0, y: 30, filter: "blur(10px)" },
                { 
                    autoAlpha: 1, y: 0, filter: "blur(0px)", duration: 1, ease: "power3.out",
                    scrollTrigger: { trigger: ".nv-marquee-section", start: "top 85%" }
                }
            );
            
            // Ecosystem Header Reveal
            gsap.fromTo("#ecosystem .gsap-reveal",
                { autoAlpha: 0, y: 40, scale: 0.98, filter: "blur(8px)" },
                { 
                    autoAlpha: 1, y: 0, scale: 1, filter: "blur(0px)", duration: 1, stagger: 0.1, ease: "power3.out",
                    scrollTrigger: { trigger: "#ecosystem", start: "top 75%" }
                }
            );
            
            // Globe Elements Reveal (Staggering the globe and info panel)
            gsap.fromTo(".globe-layout",
                { autoAlpha: 0, y: 50 },
                { 
                    autoAlpha: 1, y: 0, duration: 1.2, ease: "power3.out",
                    scrollTrigger: { trigger: ".globe-layout", start: "top 80%" }
                }
            );
            
            // Footer Staggered Reveal
            gsap.fromTo(".footer-col",
                { autoAlpha: 0, y: 30 },
                { 
                    autoAlpha: 1, y: 0, duration: 0.8, stagger: 0.15, ease: "power2.out",
                    scrollTrigger: { trigger: "footer", start: "top 90%" }
                }
            );
        });
    </script>
</body>"""

content = content.replace('</body>', gsap_script)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Scroll animations injected successfully!")
