import os
from bs4 import BeautifulSoup
from PIL import Image
import urllib.request
import io

html_files = [
    'index.html', 'coaching.html', 'contact.html', 'executiveadvisory.html',
    'meet-tony.html', 'resources.html', 'speaking.html', 'training.html'
]

def get_image_size(src):
    try:
        if src.startswith('http'):
            # try to get from url
            req = urllib.request.Request(src, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as url:
                f = io.BytesIO(url.read())
                img = Image.open(f)
                return img.width, img.height
        else:
            # local file
            img = Image.open(src)
            return img.width, img.height
    except Exception as e:
        print(f"Could not get size for {src}: {e}")
        return None, None

for filename in html_files:
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        continue

    with open(filename, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Get all images
    images = soup.find_all('img')
    
    if not images:
        continue

    # Assume the first image is the hero image
    for i, img in enumerate(images):
        src = img.get('src', '')
        
        # Get width and height if not present
        if not img.has_attr('width') or not img.has_attr('height'):
            w, h = get_image_size(src)
            if w and h:
                img['width'] = str(w)
                img['height'] = str(h)
        
        if i == 0 or 'hero' in str(img.parent).lower() or 'banner' in str(img.parent).lower():
            # Hero / Above the fold
            img['fetchpriority'] = 'high'
            img['decoding'] = 'async'
            if 'loading' in img.attrs:
                del img['loading']
        else:
            # Below the fold
            img['loading'] = 'lazy'
            img['decoding'] = 'async'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    
    print(f"Updated {filename}")
