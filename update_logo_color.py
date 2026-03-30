import codecs
import re

file = 'c:/Users/lonea/Downloads/seismic-mainnet.html'
with codecs.open(file, 'r', 'utf-8') as f:
    text = f.read()

# Remove the ugly SVG style color overrides Dribbble injects
text = re.sub(r'style="stop-color:#[A-Za-z0-9]+;[^"]*"', '', text)

# Map vintage rose colors to Cyberpunk neon
text = text.replace('stop-color="#D0A0B7"', 'stop-color="#00ff9f"')  # Neon Green
text = text.replace('stop-color="#6A525D"', 'stop-color="#00d4ff"')  # Cyan
text = text.replace('stop-color="#8D6477"', 'stop-color="#00ff9f"')  # More Green

with codecs.open(file, 'w', 'utf-8') as f:
    f.write(text)

print("SVG Gradients Updated to matches website theme")
