import os
import re

files_to_update = [
    'index.html',
    'contact.html',
    'meet-tony.html',
    'resources.html',
    'speaking.html',
    'training.html'
]

# Read index.html to get the gold standard header
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Remove chevrons from index.html content
chevron_pattern = r'\s*<i class="fa-solid fa-chevron-down"[^>]*></i>'
index_content = re.sub(chevron_pattern, '', index_content)

# Extract header CSS and HTML
header_match = re.search(r'(<!-- Desktop Header CSS -->.*?</header>)', index_content, re.DOTALL)
if not header_match:
    print("Failed to extract header block")
    exit(1)

header_block = header_match.group(1)

# Enforce uniform dimensions that might be overridden elsewhere
explicit_css = """
            /* Explicit enforcement of uniform sizes */
            .main-header {
                height: 64px !important;
                padding: 0 35px !important;
                box-sizing: border-box !important;
            }
            .main-header .logo img {
                height: 35px !important;
                width: auto !important;
                display: inline-block !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .main-header ul {
                margin: 0 !important;
                padding: 0 !important;
                display: flex !important;
                align-items: center !important;
                gap: 30px !important;
            }
            .main-header ul li {
                list-style: none !important;
                margin: 0 !important;
                padding: 0 !important;
            }
            .top-utility-bar {
                height: 45px !important;
                padding: 0 40px !important;
                box-sizing: border-box !important;
            }
"""
# Inject explicit_css into header_block right before `</style>`
header_block = header_block.replace("</style>", explicit_css + "\n    </style>")

for file in files_to_update:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove chevrons just in case they exist elsewhere
    content = re.sub(chevron_pattern, '', content)
    
    # Replace existing header block
    if "<!-- Desktop Header CSS -->" in content:
        content = re.sub(r'<!-- Desktop Header CSS -->.*?</header>', header_block, content, flags=re.DOTALL)
    elif "<!-- Header Navigation -->" in content:
        content = re.sub(r'<!-- Header Navigation -->.*?</header>', header_block, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
