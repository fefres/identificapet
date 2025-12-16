# AdoptaIA - Página Web para GitHub Pages

Una página web moderna y responsive para la plataforma de adopción de mascotas AdoptaIA, optimizada para GitHub Pages.

## 🚀 Características

- **Diseño Responsive**: Adaptado para desktop, tablet y móvil
- **Tailwind CSS**: Framework de CSS utilitario para estilos rápidos
- **JavaScript Interactivo**: Funcionalidades dinámicas y animaciones
- **SEO Optimizado**: Meta tags y structured data para mejor posicionamiento
- **Accesibilidad**: Cumple estándares de accesibilidad web
- **Performance**: Optimizado para carga rápida

## 📁 Estructura de Archivos

```
/
├── index.html              # Página principal
├── styles/
│   └── main.css           # Estilos personalizados
├── scripts/
│   └── main.js            # JavaScript funcional
├── images/
│   ├── favicon.svg        # Icono del sitio
│   ├── hero-dog.jpg       # Imagen hero (placeholder)
│   ├── pet1.jpg           # Imagen mascota 1 (placeholder)
│   ├── pet2.jpg           # Imagen mascota 2 (placeholder)
│   └── pet3.jpg           # Imagen mascota 3 (placeholder)
└── README.md              # Este archivo
```

## 🛠️ Instrucciones para GitHub Pages

### Paso 1: Crear Repositorio en GitHub

1. Ve a [GitHub.com](https://github.com) e inicia sesión
2. Haz clic en el botón "New" o "+" → "New repository"
3. Nombre del repositorio: `adoptaia-web` (o el nombre que prefieras)
4. Marca "Public" (requerido para GitHub Pages gratuito)
5. **NO** inicialices con README, .gitignore o license
6. Haz clic en "Create repository"

### Paso 2: Subir Archivos

**Opción A: Usando la interfaz web de GitHub**

1. Una vez creado el repositorio, haz clic en "uploading an existing file"
2. Arrastra y suelta todos los archivos de esta carpeta:
   - `index.html`
   - `styles/main.css`
   - `scripts/main.js`
   - `images/` (carpeta completa con todas las imágenes)
3. En el mensaje de commit escribe: "Initial commit: AdoptaIA website"
4. Haz clic en "Commit changes"

**Opción B: Usando Git (para usuarios avanzados)**

```bash
# Clona el repositorio
git clone https://github.com/TU-USUARIO/adoptaia-web.git
cd adoptaia-web

# Copia todos los archivos a la carpeta del repositorio
# Luego:
git add .
git commit -m "Initial commit: AdoptaIA website"
git push origin main
```

### Paso 3: Activar GitHub Pages

1. Ve a la pestaña "Settings" de tu repositorio
2. Desplázate hasta la sección "Pages" en el menú lateral
3. En "Source", selecciona "Deploy from a branch"
4. Selecciona "main" (o "master") como rama
5. Selecciona "/ (root)" como carpeta
6. Haz clic en "Save"

### Paso 4: Acceder a tu Página

Tu página estará disponible en:
`https://TU-USUARIO.github.io/adoptaia-web/`

## 🎨 Personalización

### Cambiar Contenido

1. **Textos**: Edita directamente en `index.html`
2. **Colores**: Modifica las clases de Tailwind CSS en el HTML
3. **Imágenes**: Reemplaza las imágenes en la carpeta `images/`

### Agregar Funcionalidades

- **Formularios**: El JavaScript incluye manejo básico de formularios
- **Búsqueda**: Estructura preparada para integrar APIs de búsqueda
- **Base de datos**: Preparado para conectar con APIs externas

## 🔧 Tecnologías Utilizadas

- **HTML5**: Estructura semántica moderna
- **Tailwind CSS**: Framework de CSS utilitario
- **JavaScript ES6+**: Funcionalidad interactiva
- **SVG**: Iconos y gráficos vectoriales
- **Responsive Design**: Adaptable a todos los dispositivos

## 📱 Características Móviles

- **Menú hamburguesa**: Navegación optimizada para móvil
- **Touch-friendly**: Botones y enlaces optimizados para touch
- **Imágenes responsive**: Se adaptan automáticamente al tamaño de pantalla

## 🔍 SEO y Rendimiento

- **Meta tags completos**: Title, description, keywords
- **Open Graph**: Optimizado para redes sociales
- **Structured Data**: JSON-LD para mejor indexación
- **Lazy loading**: Carga optimizada de imágenes
- **Minificación**: CSS y JS optimizados para producción

## 🐛 Solución de Problemas

### La página no se muestra correctamente

1. Verifica que el repositorio sea público
2. Confirma que GitHub Pages esté activado
3. Revisa que todos los archivos estén en la raíz del repositorio

### Las imágenes no cargan

1. Asegúrate de que las imágenes estén en la carpeta `images/`
2. Verifica que las rutas en el HTML sean correctas
3. Usa formatos de imagen web (JPG, PNG, WebP)

### El CSS no se aplica

1. Confirma que `styles/main.css` esté en la raíz
2. Verifica la conexión a Tailwind CSS CDN
3. Revisa la consola del navegador para errores

## 🚀 Próximos Pasos

1. **Agregar imágenes reales**: Reemplaza los placeholders con fotos de mascotas
2. **Integrar backend**: Conectar con base de datos para gestión de mascotas
3. **Formularios funcionales**: Implementar envío real de formularios
4. **Analytics**: Agregar Google Analytics para seguimiento
5. **Dominio personalizado**: Configurar tu propio dominio

## 📞 Soporte

Si necesitas ayuda adicional:

1. Revisa la [documentación de GitHub Pages](https://docs.github.com/en/pages)
2. Consulta la [documentación de Tailwind CSS](https://tailwindcss.com/docs)
3. Busca en la [comunidad de GitHub](https://github.community)

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

---

**Creado por MiniMax Agent** 🤖
*Plataforma de adopción de mascotas con IA*