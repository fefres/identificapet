# Guía de Despliegue Completa - AdoptaIA

## 🚀 Despliegue Rápido en GitHub Pages

### Paso 1: Preparar los Archivos
Asegúrate de tener todos estos archivos listos:
- ✅ `index.html` (página principal)
- ✅ `styles/main.css` (estilos personalizados)
- ✅ `scripts/main.js` (funcionalidad JavaScript)
- ✅ `images/` (carpeta con todas las imágenes)
- ✅ `README.md` (documentación)

### Paso 2: Crear Repositorio en GitHub

1. **Ve a GitHub.com** e inicia sesión
2. **Haz clic en "New"** (botón verde)
3. **Configura el repositorio:**
   - Nombre: `adoptaia-web` (o el que prefieras)
   - Descripción: "Plataforma de adopción de mascotas con IA"
   - Público ✓ (necesario para GitHub Pages gratuito)
   - NO inicialices con README
4. **Haz clic en "Create repository"**

### Paso 3: Subir Archivos

#### Opción A: Arrastrar y Soltar (Más Fácil)
1. **En tu repositorio vacío**, haz clic en "uploading an existing file"
2. **Arrastra todos los archivos** desde tu carpeta local
3. **Confirma la subida** de todos los archivos
4. **Escribe el mensaje**: "Initial commit: AdoptaIA website"
5. **Haz clic en "Commit changes"**

#### Opción B: Usando Git (Para Usuarios Avanzados)
```bash
# 1. Clona el repositorio
git clone https://github.com/TU-USUARIO/adoptaia-web.git
cd adoptaia-web

# 2. Copia todos los archivos a la carpeta
# (manual, arrastrando archivos)

# 3. Añade y confirma cambios
git add .
git commit -m "Initial commit: AdoptaIA website"

# 4. Sube al repositorio
git push origin main
```

### Paso 4: Activar GitHub Pages

1. **Ve a Settings** en tu repositorio
2. **Busca "Pages"** en el menú lateral izquierdo
3. **En Source**, selecciona:
   - "Deploy from a branch"
   - "main" (o "master")
   - "/ (root)"
4. **Haz clic en "Save"**
5. **Espera 2-5 minutos** para que se active

### Paso 5: Verificar Funcionamiento

Tu sitio estará disponible en:
`https://TU-USUARIO.github.io/adoptaia-web/`

**Verifica que funcione:**
- ✅ La página carga correctamente
- ✅ El diseño se ve bien en móvil y escritorio
- ✅ Las imágenes se muestran
- ✅ Los enlaces de navegación funcionan

## 🔧 Personalización Adicional

### Cambiar el Nombre del Repositorio
Si quieres cambiar el nombre:
1. Ve a Settings del repositorio
2. Cambia el nombre en "Repository name"
3. La URL cambiará a: `https://TU-USUARIO.github.io/NUEVO-NOMBRE/`

### Usar un Dominio Personalizado
Para usar tu propio dominio (ej: `adoptaia.com`):

1. **En GitHub Pages Settings:**
   - En "Custom domain", añade tu dominio
   - Marca "Enforce HTTPS"

2. **En tu proveedor de DNS:**
   - Añade un registro CNAME: `www.adoptaia.com → TU-USUARIO.github.io`
   - Añade un registro A: `adoptaia.com → 185.199.108.153`

### Automatización con GitHub Actions

Crea el archivo `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./
```

## 📱 Testing y Optimización

### Pruebas de Compatibilidad
- **Navegadores**: Chrome, Firefox, Safari, Edge
- **Dispositivos**: Desktop, tablet, móvil
- **Velocidad**: Usa Google PageSpeed Insights

### Optimizaciones Recomendadas
1. **Comprimir imágenes** antes de subir
2. **Minificar CSS y JS** para producción
3. **Usar CDN** para recursos externos
4. **Implementar lazy loading** (ya incluido)

## 🐛 Solución de Problemas Comunes

### Error 404 - Página No Encontrada
- ✅ Verifica que `index.html` esté en la raíz
- ✅ Confirma que el repositorio sea público
- ✅ Revisa que GitHub Pages esté activado

### Imágenes No Cargan
- ✅ Verifica que las imágenes estén en `/images/`
- ✅ Confirma que los nombres coincidan exactamente
- ✅ Usa formatos web (JPG, PNG, WebP)

### CSS No Se Aplica
- ✅ Confirma que `styles/main.css` esté en la raíz
- ✅ Verifica la conexión a Tailwind CSS CDN
- ✅ Revisa la consola del navegador para errores

### El Sitio No Se Ve en Móvil
- ✅ Confirma que uses clases responsive de Tailwind
- ✅ Prueba en diferentes tamaños de pantalla
- ✅ Verifica que el viewport meta tag esté presente

## 📞 Recursos de Ayuda

### Documentación Oficial
- **GitHub Pages**: https://docs.github.com/en/pages
- **Tailwind CSS**: https://tailwindcss.com/docs
- **HTML5**: https://developer.mozilla.org/en-US/docs/Web/HTML

### Comunidades
- **Stack Overflow**: Para preguntas técnicas específicas
- **GitHub Community**: Para problemas con GitHub
- **Discord/Slack**: Comunidades de desarrollo

### Herramientas Útiles
- **Chrome DevTools**: Para debugging
- **Responsively**: Para testing responsive
- **Lighthouse**: Para auditoría de performance

## 🎉 ¡Felicitaciones!

Si llegaste hasta aquí, tienes una página web profesional funcionando en GitHub Pages. 

**Próximos pasos sugeridos:**
1. 🎨 Personalizar colores y contenido
2. 📝 Agregar más secciones o páginas
3. 🔗 Integrar con redes sociales
4. 📊 Añadir Google Analytics
5. 🚀 Configurar dominio personalizado

---

**Creado por MiniMax Agent** 🤖  
*¿Necesitas ayuda adicional? No dudes en preguntar.*