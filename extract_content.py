#!/usr/bin/env python3
import re
import os
from pathlib import Path

def extract_and_organize_html():
    """Extraer contenido del HTML original y organizarlo en archivos separados"""
    
    # Leer el archivo HTML original
    with open('/workspace/user_input_files/index.html.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    print("📄 Archivo original leído. Tamaño:", len(html_content), "caracteres")
    
    # Crear directorios necesarios
    os.makedirs('styles', exist_ok=True)
    os.makedirs('scripts', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    
    # 1. Extraer CSS embebido
    css_pattern = r'<style[^>]*>(.*?)</style>'
    css_matches = re.findall(css_pattern, html_content, re.DOTALL)
    
    all_css = ""
    for css in css_matches:
        all_css += css + "\n\n"
    
    if all_css:
        with open('styles/main.css', 'w', encoding='utf-8') as f:
            f.write(all_css)
        print("✅ CSS extraído a styles/main.css")
    
    # 2. Extraer JavaScript embebido
    js_pattern = r'<script[^>]*>(.*?)</script>'
    js_matches = re.findall(js_pattern, html_content, re.DOTALL)
    
    # Filtrar solo JavaScript (no JSON-LD)
    js_content = ""
    for js in js_matches:
        if not js.strip().startswith('{') and '"@context"' not in js:
            js_content += js + "\n\n"
    
    if js_content:
        with open('scripts/main.js', 'w', encoding='utf-8') as f:
            f.write(js_content)
        print("✅ JavaScript extraído a scripts/main.js")
    
    # 3. Extraer imágenes embebidas (data:image)
    img_pattern = r'data:image/([^;]+);base64,([^"\'>\s]+)'
    img_matches = re.findall(img_pattern, html_content)
    
    img_files = []
    for i, (img_type, img_data) in enumerate(img_matches, 1):
        filename = f"images/embedded_image_{i}.{img_type}"
        try:
            import base64
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(img_data))
            img_files.append(filename)
            print(f"✅ Imagen extraída: {filename}")
        except Exception as e:
            print(f"❌ Error extrayendo imagen {i}: {e}")
    
    # 4. Crear HTML limpio sin CSS/JS embebido
    # Remover estilos embebidos
    html_clean = re.sub(css_pattern, '', html_content, flags=re.DOTALL)
    
    # Remover JavaScript embebido (pero mantener JSON-LD)
    for js in js_matches:
        if not js.strip().startswith('{') and '"@context"' not in js:
            html_clean = html_clean.replace(f'<script>{js}</script>', '')
            html_clean = html_clean.replace(f'<script type="text/javascript">{js}</script>', '')
    
    # 5. Actualizar referencias en el HTML limpio
    # Agregar enlaces a archivos externos
    head_insert = '''
    <!-- External CSS -->
    <link rel="stylesheet" href="styles/main.css">
    
    <!-- External JavaScript -->
    <script src="scripts/main.js"></script>
    '''
    
    # Insertar enlaces antes de </head>
    html_clean = html_clean.replace('</head>', head_insert + '\n</head>')
    
    # 6. Guardar HTML limpio
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_clean)
    print("✅ HTML limpio guardado como index.html")
    
    # 7. Crear favicon.svg simple
    favicon_svg = '''<svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
  <rect width="32" height="32" fill="#3B82F6" rx="4"/>
  <text x="16" y="20" font-family="Arial" font-size="10" fill="white" text-anchor="middle">AI</text>
</svg>'''
    
    with open('images/favicon.svg', 'w', encoding='utf-8') as f:
        f.write(favicon_svg)
    print("✅ Favicon creado")
    
    # 8. Actualizar referencias de imágenes en HTML si es necesario
    # Si hay imágenes embebidas, agregar un script para reemplazarlas
    if img_files:
        js_replacement = '''
// Reemplazar imágenes embebidas con archivos
document.addEventListener('DOMContentLoaded', function() {
    const imgElements = document.querySelectorAll('img[data-base64]');
    imgElements.forEach((img, index) => {
        const base64 = img.getAttribute('data-base64');
        if (base64) {
            const imgSrc = 'data:image/' + base64;
            img.src = imgSrc;
        }
    });
});
'''
        with open('scripts/image-replacement.js', 'w', encoding='utf-8') as f:
            f.write(js_replacement)
        
        # Agregar referencia al script de reemplazo en index.html
        html_final = open('index.html', 'r', encoding='utf-8').read()
        html_final = html_final.replace('</body>', '<script src="scripts/image-replacement.js"></script>\n</body>')
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_final)
        print("✅ Script de reemplazo de imágenes agregado")
    
    print("\n🎉 ¡Extracción completada!")
    print("📁 Archivos creados:")
    print("   - index.html")
    print("   - styles/main.css")
    print("   - scripts/main.js")
    print("   - images/favicon.svg")
    if img_files:
        for img in img_files:
            print(f"   - {img}")

if __name__ == "__main__":
    extract_and_organize_html()
