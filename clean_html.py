import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove ALL instances of the preloader code
# The preloader code starts with "<!-- Premium Animated Preloader -->" and ends with "</script>" (the one right after <svg>)
preloader_pattern = r'\s*<!-- Premium Animated Preloader -->.*?<script>.*?</script>\s*'
# Wait, regex dotall could match too much. Let's make it non-greedy.
preloader_pattern_compiled = re.compile(r'\s*<!-- Premium Animated Preloader -->.*?</script>\s*', re.DOTALL)

clean_content = preloader_pattern_compiled.sub('\n', content)

# Check for duplicate <body> tags.
# I'll just remove the second <body> tag manually if it's there.
body_count = clean_content.count('<body>')
if body_count > 1:
    # Split by body and keep the first one
    parts = clean_content.split('<body>')
    # The first part is everything before the first <body>
    # The rest are after. Wait, if the second <body> was mistakenly added along with duplicated content, 
    # I might need to see what content was duplicated.
    pass

with open('index_cleaned_temp.html', 'w', encoding='utf-8') as f:
    f.write(clean_content)

print("Preloaders removed. Body count:", clean_content.count('<body>'))
print("html count:", clean_content.count('<html'))
