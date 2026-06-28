import os

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure we don't duplicate
if 'id="premium-preloader"' not in content:
    preloader_code = """
    <!-- Premium Animated Preloader -->
    <style>
        #premium-preloader {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: #FFFFFF; display: flex; align-items: center; justify-content: center;
            z-index: 999999;
            transition: opacity 0.8s ease-in-out, visibility 0.8s ease-in-out;
        }
        .preloader-hidden {
            opacity: 0 !important;
            visibility: hidden !important;
        }
        .loader-svg {
            width: 140px; height: 140px;
            animation: main-pulse 3s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        }
        .blob-center {
            animation: blob-pulse 3s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
            transform-origin: 50% 50%;
        }
        .blob-1 {
            animation: blob-orbit-1 3s cubic-bezier(0.65, 0, 0.35, 1) infinite;
            transform-origin: 50px 50px;
        }
        .blob-2 {
            animation: blob-orbit-2 3s cubic-bezier(0.65, 0, 0.35, 1) infinite;
            transform-origin: 50px 50px;
        }
        .loader-circle {
            stroke-dasharray: 220;
            stroke-dashoffset: 220;
            stroke-linecap: round;
            transform-origin: 50% 50%;
            animation: draw-ring 3s cubic-bezier(0.65, 0, 0.35, 1) infinite;
        }

        @keyframes main-pulse {
            0% { transform: scale(0.95) rotate(0deg); filter: drop-shadow(0 10px 20px rgba(69,27,110,0.1)); }
            50% { transform: scale(1) rotate(5deg); filter: drop-shadow(0 20px 40px rgba(203,33,36,0.15)); }
            100% { transform: scale(0.95) rotate(0deg); filter: drop-shadow(0 10px 20px rgba(69,27,110,0.1)); }
        }

        @keyframes blob-pulse {
            0% { transform: scale(0.5); fill: #FFEEEA; }
            50% { transform: scale(1.3); fill: #D0A0B5; }
            100% { transform: scale(0.5); fill: #FFEEEA; }
        }

        @keyframes blob-orbit-1 {
            0% { transform: rotate(0deg) translateX(0) scale(1); }
            50% { transform: rotate(180deg) translateX(12px) scale(0.5); }
            100% { transform: rotate(360deg) translateX(0) scale(1); }
        }

        @keyframes blob-orbit-2 {
            0% { transform: rotate(0deg) translateX(0) scale(1); }
            50% { transform: rotate(-180deg) translateX(-12px) scale(0.5); }
            100% { transform: rotate(-360deg) translateX(0) scale(1); }
        }

        @keyframes draw-ring {
            0% { stroke-dashoffset: 220; transform: rotate(-90deg); }
            50% { stroke-dashoffset: 0; transform: rotate(90deg); }
            100% { stroke-dashoffset: -220; transform: rotate(270deg); }
        }
    </style>
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
    <script>
        // Dismiss preloader after 3 seconds for demo purposes
        window.addEventListener('load', () => {
            setTimeout(() => {
                document.getElementById('premium-preloader').classList.add('preloader-hidden');
            }, 3000); // exactly one 3s loop
        });
    </script>
    """
    
    # Insert right after body tag
    body_pos = content.find('<body>')
    if body_pos != -1:
        insert_idx = body_pos + len('<body>')
        new_content = content[:insert_idx] + "\n" + preloader_code + content[insert_idx:]
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Preloader added successfully!")
    else:
        print("Could not find <body> tag")
else:
    print("Preloader already exists.")
