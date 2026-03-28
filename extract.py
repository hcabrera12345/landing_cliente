import re
import base64
import os

source_html = r"C:\Users\herna\Downloads\nixaga-petrol-v11.html"
target_html = r"index.html"
target_css = r"src\style.css"
target_dir = r"public"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

with open(source_html, "r", encoding="utf-8") as f:
    html_content = f.read()

# Extract CSS
css_match = re.search(r"<style>(.*?)</style>", html_content, flags=re.DOTALL)
css_content = ""
if css_match:
    css_content = css_match.group(1).strip()
    html_content = html_content.replace(css_match.group(0), "")

# Write CSS
with open(target_css, "w", encoding="utf-8") as f:
    f.write(css_content)

# Extract and save images
img_count = 1
def replace_img(match):
    global img_count
    # The whole src attribute content
    data_uri = match.group(1)
    
    # Split the metadata and the actual base64 data
    if "base64," in data_uri:
        metadata, base64_data = data_uri.split("base64,", 1)
        # Determine extension
        ext = "jpg" # default
        if "png" in metadata.lower():
            ext = "png"
        elif "gif" in metadata.lower():
            ext = "gif"
        elif "webp" in metadata.lower():
            ext = "webp"
        
        # If the start indicates jpeg
        if base64_data.startswith("/9j/"):
            ext = "jpg"

        filename = f"image_{img_count}.{ext}"
        if img_count == 1:
            filename = f"hero.{ext}"
        
        filepath = os.path.join(target_dir, filename)
        
        with open(filepath, "wb") as img_file:
            img_file.write(base64.b64decode(base64_data))
        
        img_count += 1
        return f'src="/{filename}"'
            
    return match.group(0)

# We use regex to find src attributes with data:image
new_html_content = re.sub(r'src="(data:image/[^"]+)"', replace_img, html_content)

# Process the HTML to add the <link> for the CSS and JS for Vite
# Let's add the link to style.css in the head
new_html_content = new_html_content.replace("</head>", '  <link rel="stylesheet" href="/src/style.css">\n</head>')

# Add the script tag right before </body>
new_html_content = new_html_content.replace("</body>", '  <script type="module" src="/src/main.js"></script>\n</body>')

with open(target_html, "w", encoding="utf-8") as f:
    f.write(new_html_content)

print(f"Extracted {img_count - 1} image(s). CSS written to {target_css}. HTML updated.")
