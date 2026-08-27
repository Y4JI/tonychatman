import os
import re

# Read index.html to extract header and js
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header CSS and HTML
header_match = re.search(r'(<!-- Desktop Header CSS -->.*?</header>)', index_content, re.DOTALL)
header_block = header_match.group(1) if header_match else ""

if not header_block:
    print("Failed to extract header block")
    exit(1)

# Extract JS for header scroll
js_scroll = """        // Header Scroll Effect
        const topUtilityBar = document.querySelector('.top-utility-bar');
        const mainHeader = document.getElementById('mainHeader');
        
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                if(topUtilityBar) topUtilityBar.classList.add('scrolled');
                if(mainHeader) mainHeader.classList.add('scrolled');
            } else {
                if(topUtilityBar) topUtilityBar.classList.remove('scrolled');
                if(mainHeader) mainHeader.classList.remove('scrolled');
            }
        });"""

files_to_update = [
    'contact.html',
    'meet-tony.html',
    'resources.html',
    'speaking.html',
    'training.html'
]

for file in files_to_update:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace existing header
    # Check if there's an existing <!-- Top Utility Bar --> ... </header>
    # OR just <!-- Header Navigation --> ... </header>
    
    # First, let's remove any existing top utility bar if it's there
    content = re.sub(r'<!-- Top Utility Bar -->.*?</div>\s*<!-- Header Navigation -->', '<!-- Header Navigation -->', content, flags=re.DOTALL)
    
    if "<!-- Header Navigation -->" in content:
        content = re.sub(r'<!-- Header Navigation -->.*?</header>', header_block, content, flags=re.DOTALL)
    elif "<header" in content:
        content = re.sub(r'<header.*?</header>', header_block, content, flags=re.DOTALL)
        
    # Inject JS before </body>
    if "// Header Scroll Effect" not in content:
        content = content.replace("</body>", f"<script>\n{js_scroll}\n    </script>\n</body>")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
