import re

with open(r'C:\Users\MyPC\.gemini\antigravity-ide\brain\55ea8ebc-c71a-49a9-9a6f-695ee8e0eb4c\.system_generated\steps\5\content.md', 'r', encoding='utf-8') as f:
    content = f.read()

# find all h1, h2, h3 tags
headings = re.findall(r'<(h[1-6])[^>]*>(.*?)</\1>', content, re.IGNORECASE | re.DOTALL)

for tag, text in headings:
    # remove inner tags
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    if clean_text:
        print(f"{tag}: {clean_text}")
