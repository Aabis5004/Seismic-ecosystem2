import codecs
import re

file_path = 'c:/Users/lonea/Downloads/seismic-mainnet.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    text = f.read()

# 1. Restore the precise original defs block with the Rose Gold layout.
original_defs = """<defs>
                <filter id="filter0_n_5_119" x="0" y="0" width="145.736" height="208.757" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
                <feFlood flood-opacity="0" result="BackgroundImageFix"/>
                <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
                <feTurbulence type="fractalNoise" baseFrequency="2.0310719013214111 2.0310719013214111" stitchTiles="stitch" numOctaves="3" result="noise" seed="9417" />
                <feColorMatrix in="noise" type="luminanceToAlpha" result="alphaNoise" />
                <feComponentTransfer in="alphaNoise" result="coloredNoise1">
                <feFuncA type="discrete" tableValues="1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 "/>
                </feComponentTransfer>
                <feComposite operator="in" in2="shape" in="coloredNoise1" result="noise1Clipped" />
                <feFlood flood-color="rgba(0, 0, 0, 0.25)" result="color1Flood" />
                <feComposite operator="in" in2="noise1Clipped" in="color1Flood" result="color1" />
                <feMerge result="effect1_noise_5_119">
                <feMergeNode in="shape" />
                <feMergeNode in="color1" />
                </feMerge>
                </filter>
                <linearGradient id="paint0_linear_5_119" x1="35.2736" y1="128.918" x2="-19.7574" y2="14.92" gradientUnits="userSpaceOnUse">
                <stop stop-color="#D0A0B7" style="stop-color:#D0A0B7;stop-color:color(display-p3 0.8173 0.6293 0.7161);stop-opacity:1;"/>
                <stop offset="1" stop-color="#6A525D" style="stop-color:#6A525D;stop-color:color(display-p3 0.4173 0.3213 0.3656);stop-opacity:1;"/>
                </linearGradient>
                <linearGradient id="paint1_linear_5_119" x1="97.7281" y1="106.222" x2="52.9004" y2="11.6542" gradientUnits="userSpaceOnUse">
                <stop stop-color="#D0A0B7" style="stop-color:#D0A0B7;stop-color:color(display-p3 0.8173 0.6293 0.7161);stop-opacity:1;"/>
                <stop offset="1" stop-color="#6A525D" style="stop-color:#6A525D;stop-color:color(display-p3 0.4173 0.3213 0.3656);stop-opacity:1;"/>
                </linearGradient>
                <linearGradient id="paint2_linear_5_119" x1="132.906" y1="136.996" x2="72.6075" y2="84.5536" gradientUnits="userSpaceOnUse">
                <stop stop-color="#D0A0B7" style="stop-color:#D0A0B7;stop-color:color(display-p3 0.8173 0.6293 0.7161);stop-opacity:1;"/>
                <stop offset="1" stop-color="#6A525D" style="stop-color:#6A525D;stop-color:color(display-p3 0.4173 0.3213 0.3656);stop-opacity:1;"/>
                </linearGradient>
                <linearGradient id="paint3_linear_5_119" x1="85.4225" y1="208.613" x2="47.6119" y2="111.729" gradientUnits="userSpaceOnUse">
                <stop stop-color="#8D6477" style="stop-color:#8D6477;stop-color:color(display-p3 0.5545 0.3923 0.4671);stop-opacity:1;"/>
                <stop offset="0.600962" stop-color="#6A525D" style="stop-color:#6A525D;stop-color:color(display-p3 0.4173 0.3213 0.3656);stop-opacity:1;"/>
                </linearGradient>
                <linearGradient id="paint4_linear_5_119" x1="60.0382" y1="208.614" x2="-0.932334" y2="45.8254" gradientUnits="userSpaceOnUse">
                <stop stop-color="#D0A0B7" style="stop-color:#D0A0B7;stop-color:color(display-p3 0.8173 0.6293 0.7161);stop-opacity:1;"/>
                <stop offset="1" stop-color="#6A525D" style="stop-color:#6A525D;stop-color:color(display-p3 0.4173 0.3213 0.3656);stop-opacity:1;"/>
                </linearGradient>
                <clipPath id="clip0_5_119">
                <rect width="145.736" height="208.757" fill="white" style="fill:white;fill-opacity:1;"/>
                </clipPath>
                </defs>"""

text = re.sub(r'<defs>.*?</defs>', original_defs, text, flags=re.DOTALL)

# 2. Update the color of the navbar logo.
css_to_replace = """        .logo {
            font-family: 'Syne', sans-serif;
            font-size: 28px;
            font-weight: 800;
            background: var(--gradient-main);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 2px;
        }"""

css_replacement = """        .logo {
            font-family: 'Syne', sans-serif;
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(135deg, #D0A0B7, #6A525D);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: 2px;
        }"""

text = text.replace(css_to_replace, css_replacement)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(text)

print("done")
