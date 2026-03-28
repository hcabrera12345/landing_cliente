const fs = require('fs');
const path = require('path');

const sourceHtml = 'C:\\Users\\herna\\Downloads\\nixaga-petrol-v11.html';
const targetHtml = 'index.html';
const targetCss = path.join('src', 'style.css');
const targetDir = 'public';

if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
}

let htmlContent = fs.readFileSync(sourceHtml, 'utf-8');

// Extract CSS
const cssMatch = htmlContent.match(/<style>([\s\S]*?)<\/style>/);
let cssContent = "";
if (cssMatch) {
    cssContent = cssMatch[1].trim();
    htmlContent = htmlContent.replace(cssMatch[0], "");
}

// Write CSS
fs.writeFileSync(targetCss, cssContent, 'utf-8');

// Extract and save images
let imgCount = 1;

htmlContent = htmlContent.replace(/src="(data:image\/[^"]+)"/g, (match, dataUri) => {
    if (dataUri.includes('base64,')) {
        const [metadata, base64Data] = dataUri.split('base64,');
        let ext = 'jpg';
        if (metadata.toLowerCase().includes('png')) ext = 'png';
        else if (metadata.toLowerCase().includes('gif')) ext = 'gif';
        else if (metadata.toLowerCase().includes('webp')) ext = 'webp';
        
        if (base64Data.startsWith('/9j/')) ext = 'jpg';
        
        let filename = `image_${imgCount}.${ext}`;
        if (imgCount === 1) filename = `hero.${ext}`;
        
        const filepath = path.join(targetDir, filename);
        fs.writeFileSync(filepath, Buffer.from(base64Data, 'base64'));
        
        imgCount++;
        return `src="/${filename}"`;
    }
    return match;
});

// Process HTML to include correct Vite links
htmlContent = htmlContent.replace('</head>', '  <link rel="stylesheet" href="/src/style.css">\n</head>');
htmlContent = htmlContent.replace('</body>', '  <script type="module" src="/src/main.js"></script>\n</body>');

fs.writeFileSync(targetHtml, htmlContent, 'utf-8');

console.log(`Extracted ${imgCount - 1} image(s). CSS saved to ${targetCss}. HTML updated.`);
