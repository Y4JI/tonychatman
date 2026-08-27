import re

with open('resources.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Original header HTML to be replaced (remove the nav buttons from the top)
old_header_pattern = r'<!-- Navigation arrows -->\s*<div class="carousel-nav" style="display: flex; gap: 10px; margin-bottom: 20px;">\s*<button id="blog-prev".*?</button>\s*<button id="blog-next".*?</button>\s*</div>'

content = re.sub(old_header_pattern, '', content, flags=re.DOTALL)

# Now, we need to inject the arrows into the container holding the carousel
# Find the container:
# <div class="container reveal">
#     <style>
#         #blog-carousel::-webkit-scrollbar {

old_container_start = r'(<div class="container reveal">)(\s*<style>\s*#blog-carousel::-webkit-scrollbar {)'

# We replace it with position relative and add the previous button
# and we add the next button after the carousel.

def replace_carousel_container(match):
    return f"""<div class="container reveal" style="position: relative;">
            <button id="blog-prev" class="btn btn-outline" style="position: absolute; top: 50%; left: -20px; transform: translateY(-50%); z-index: 10; width: 44px; height: 44px; border-radius: 50%; padding: 0; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.3s ease; background: var(--bg-white); box-shadow: 0 4px 10px rgba(0,0,0,0.1);"><i class="fa-solid fa-chevron-left"></i></button>
            <button id="blog-next" class="btn btn-outline" style="position: absolute; top: 50%; right: -20px; transform: translateY(-50%); z-index: 10; width: 44px; height: 44px; border-radius: 50%; padding: 0; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.3s ease; background: var(--bg-white); box-shadow: 0 4px 10px rgba(0,0,0,0.1);"><i class="fa-solid fa-chevron-right"></i></button>{match.group(2)}"""

content = re.sub(old_container_start, replace_carousel_container, content)

with open('resources.html', 'w', encoding='utf-8') as f:
    f.write(content)
