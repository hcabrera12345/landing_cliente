from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_fill_color(21, 82, 32)
        self.rect(0, 0, 210, 18, 'F')
        self.set_font('Helvetica', 'B', 13)
        self.set_text_color(255, 255, 255)
        self.set_y(4)
        self.cell(0, 10, 'NIXAGA PETROL SRL - Resumen del Proyecto Web', align='C')
        self.set_text_color(0, 0, 0)
        self.ln(14)

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f'Pagina {self.page_no()} | Nixaga Petrol SRL (c) 2025', align='C')

    def section_title(self, title):
        self.set_fill_color(21, 82, 32)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 8, title, fill=True, new_x='LMARGIN', new_y='NEXT')
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def body_text(self, text, bold=False):
        self.set_font('Helvetica', 'B' if bold else '', 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, text)
        self.ln(1)

    def table_row(self, col1, col2, header=False):
        if header:
            self.set_fill_color(61, 184, 94)
            self.set_text_color(255, 255, 255)
            self.set_font('Helvetica', 'B', 9)
        else:
            self.set_fill_color(245, 250, 245)
            self.set_text_color(40, 40, 40)
            self.set_font('Helvetica', '', 9)
        self.cell(70, 7, col1, border=1, fill=True)
        self.cell(0, 7, col2, border=1, fill=not header, new_x='LMARGIN', new_y='NEXT')
        self.set_text_color(0, 0, 0)

    def bullet(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        self.cell(6, 6, chr(149))
        self.multi_cell(0, 6, text)
        self.ln(1)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()
pdf.set_margins(15, 22, 15)

# ─── INTRODUCCION ───
pdf.set_font('Helvetica', 'B', 14)
pdf.set_text_color(21, 82, 32)
pdf.cell(0, 10, 'Que construimos?', new_x='LMARGIN', new_y='NEXT')
pdf.set_text_color(40, 40, 40)
pdf.set_font('Helvetica', '', 10)
pdf.multi_cell(0, 6, 'Sitio web corporativo profesional para Nixaga Petrol SRL, empresa boliviana de importacion y comercializacion de combustibles liquidos, completamente funcional con todas las integraciones necesarias para operar en linea.')
pdf.ln(3)

items = [
    'Diseno moderno, responsivo y animado',
    'Carrusel de imagenes fotografico con navegacion tactil',
    'Formulario de contacto funcional (envia correos reales)',
    'Redes sociales integradas: Facebook, TikTok, Instagram',
    'Google Analytics para medir el trafico web',
    'Despliegue automatizado (cada cambio se publica solo)',
    'Correos corporativos @nixagapetrol.com (IMAP/SMTP)',
    'Protocolos de seguridad avanzados (.htaccess)',
]
for item in items:
    pdf.bullet(item)

pdf.ln(5)

# ─── FASE 1 ───
pdf.section_title(' FASE 1: Preparacion del Codigo')
pdf.table_row('Paso', 'Descripcion', header=True)
pdf.table_row('1.1 Archivo original', 'Recibimos el HTML con todo el codigo embebido en un solo archivo')
pdf.table_row('1.2 Modularizacion', 'Convertimos a proyecto moderno con Vite (Build Tool)')
pdf.table_row('1.3 Separacion de archivos', 'CSS, JavaScript e imagenes en carpetas separadas')
pdf.table_row('1.4 SEO', 'Optimizamos metaetiquetas, Open Graph y estructura semantica')
pdf.ln(5)

# ─── FASE 2 ───
pdf.section_title(' FASE 2: Diseno y Contenido Visual')
pdf.table_row('Elemento', 'Decision', header=True)
pdf.table_row('Color principal', 'Verde corporativo #155220 + Negro #080808')
pdf.table_row('Tipografia titulos', 'Oswald (industrial, fuerte, energetica)')
pdf.table_row('Tipografia cuerpo', 'Inter (limpia, moderna, legible)')
pdf.table_row('Secciones', 'Hero, Estadisticas, Servicios, Nosotros, Mercados, Productos, Contacto, Footer')
pdf.table_row('Carrusel', '4 fotografias con navegacion por puntos y swipe tactil')
pdf.table_row('Animaciones', 'Fade-up al hacer scroll (IntersectionObserver)')
pdf.table_row('Redes sociales', 'Botones Facebook, TikTok, Instagram en contacto y footer')
pdf.ln(5)

# ─── ESTRUCTURA ───
pdf.section_title(' Estructura de Carpetas del Proyecto')
pdf.set_font('Courier', '', 9)
pdf.set_text_color(30, 30, 30)
estructura = [
    'Nixaga/',
    '  index.html         <- Estructura HTML de la pagina',
    '  src/',
    '    style.css        <- Todo el diseno visual (CSS)',
    '    main.js          <- Interactividad (carrusel, menu, formulario)',
    '  public/',
    '    hero.jpg         <- Imagenes del carrusel',
    '    image_2.jpg',
    '    image_3.jpg',
    '    image_4.jpg',
    '  .github/',
    '    workflows/',
    '      deploy.yml     <- Robot de despliegue automatico',
]
for line in estructura:
    pdf.cell(0, 5, line, new_x='LMARGIN', new_y='NEXT')
pdf.set_text_color(0, 0, 0)
pdf.ln(5)

# ─── FASE 3 ───
pdf.add_page()
pdf.section_title(' FASE 3: Repositorio y Automatizacion')
pdf.table_row('Paso', 'Descripcion', header=True)
pdf.table_row('3.1 GitHub', 'Creamos repositorio privado: hcabrera12345/landing_cliente')
pdf.table_row('3.2 Conexion local', 'Vinculamos carpeta local con GitHub (git init, remote)')
pdf.table_row('3.3 GitHub Actions', 'Robot que compila y sube archivos automaticamente a Hostinger')
pdf.table_row('3.4 Secrets', 'Credenciales FTP guardadas de forma segura en GitHub Secrets')
pdf.ln(3)
pdf.body_text('Comandos para publicar cualquier cambio futuro:', bold=True)
pdf.set_font('Courier', 'B', 11)
pdf.set_fill_color(30, 30, 30)
pdf.set_text_color(61, 184, 94)
pdf.multi_cell(0, 7, '  git add .\n  git commit -m "descripcion del cambio"\n  git push origin main', fill=True)
pdf.set_text_color(0, 0, 0)
pdf.ln(5)

# ─── FASE 4 ───
pdf.section_title(' FASE 4: Servidor y Dominio (Hostinger)')
pdf.table_row('Configuracion', 'Estado', header=True)
pdf.table_row('Plan de hosting Premium', 'Activo')
pdf.table_row('Certificado SSL (candadito verde)', 'Activo - HTTPS forzado')
pdf.table_row('Cache LiteSpeed', 'Activo - velocidad maxima')
pdf.table_row('Correos @nixagapetrol.com', 'Configurados')
pdf.table_row('Seguridad .htaccess', '7 protocolos activos')
pdf.table_row('File Manager / FTP', 'Configurado y operativo')
pdf.ln(5)

# ─── FASE 5 ───
pdf.section_title(' FASE 5: Servicios Externos Integrados')
pdf.table_row('Servicio', 'Funcion', header=True)
pdf.table_row('Google Analytics 4', 'Medir visitas, paises, dispositivos, comportamiento')
pdf.table_row('Web3Forms', 'Formulario -> correo real a informaciones@nixagapetrol.com')
pdf.table_row('Google Fonts', 'Tipografias Oswald e Inter cargadas desde CDN')
pdf.ln(5)

# ─── FASE 6 ───
pdf.section_title(' FASE 6: Correos Corporativos')
pdf.body_text('Configuracion IMAP/SMTP para Outlook, Gmail, iPhone y Android:')
pdf.table_row('Parametro', 'Valor', header=True)
pdf.table_row('Servidor Entrante (IMAP)', 'imap.hostinger.com | Puerto 993 | SSL/TLS')
pdf.table_row('Servidor Saliente (SMTP)', 'smtp.hostinger.com | Puerto 465 | SSL/TLS')
pdf.table_row('Usuario', 'correo completo (ej. gerencia@nixagapetrol.com)')
pdf.table_row('Contrasena', 'La asignada en el panel de Hostinger')
pdf.ln(5)

# ─── SEGURIDAD ───
pdf.section_title(' Protocolos de Seguridad (.htaccess)')
pdf.table_row('N', 'Protocolo - Protege contra', header=True)
pdf.table_row('1', 'Redireccion HTTPS - Conexiones no cifradas')
pdf.table_row('2', 'HSTS (1 ano) - Downgrade de seguridad')
pdf.table_row('3', 'X-Frame-Options - Clonacion de la pagina (Clickjacking)')
pdf.table_row('4', 'MIME Sniffing - Archivos disfrazados de malware')
pdf.table_row('5', 'XSS Protection - Inyeccion de scripts maliciosos')
pdf.table_row('6', 'Referrer-Policy - Fuga de datos internos')
pdf.table_row('7', 'Content-Security-Policy - Scripts no autorizados')
pdf.ln(5)

# ─── STACK ───
pdf.add_page()
pdf.section_title(' Stack Tecnologico Completo')
pdf.table_row('Area', 'Tecnologia', header=True)
pdf.table_row('Frontend', 'HTML5 + CSS3 Vanilla + JavaScript ES6+')
pdf.table_row('Build Tool', 'Vite')
pdf.table_row('Tipografia', 'Oswald + Inter (Google Fonts)')
pdf.table_row('Analytics', 'Google Analytics 4 (GA4)')
pdf.table_row('Formulario', 'Web3Forms (API gratuita)')
pdf.table_row('CI/CD', 'GitHub Actions (automatizacion)')
pdf.table_row('Hosting', 'Hostinger Plan Premium')
pdf.table_row('Dominio', 'nixagapetrol.com')
pdf.table_row('Correos', 'Hostinger Mail (IMAP/SMTP)')
pdf.table_row('Seguridad', '.htaccess + SSL Let\'s Encrypt')
pdf.ln(5)

# ─── ACCESOS ───
pdf.section_title(' Accesos Rapidos - Paneles de Administracion')
pdf.table_row('Recurso', 'URL / Dato', header=True)
pdf.table_row('Sitio web', 'nixagapetrol.com')
pdf.table_row('Repositorio de codigo', 'github.com/hcabrera12345/landing_cliente')
pdf.table_row('Panel de Hosting', 'hpanel.hostinger.com')
pdf.table_row('Webmail', 'mail.hostinger.com')
pdf.table_row('Google Analytics', 'analytics.google.com')
pdf.table_row('Formulario Web3Forms', 'web3forms.com (dashboard)')
pdf.table_row('Codigo local', r'C:\Users\herna\.gemini\antigravity\playground\ancient-planck\Nixaga')
pdf.ln(5)

# ─── ESPECIFICACIONES IMAGENES CARRUSEL ───
pdf.section_title(' Especificaciones para Imagenes del Carrusel')
pdf.table_row('Parametro', 'Ideal / Minimo aceptable', header=True)
pdf.table_row('Ancho', '1920px (ideal) / 1280px (minimo)')
pdf.table_row('Alto', '1080px (ideal) / 720px (minimo)')
pdf.table_row('Orientacion', 'HORIZONTAL obligatoriamente (nunca vertical)')
pdf.table_row('Formato', 'JPG o WebP')
pdf.table_row('Peso maximo', '500 KB por imagen')
pdf.table_row('Herramienta para comprimir', 'squoosh.app (gratis)')
pdf.table_row('Cantidad de slides', '4 imagenes (reemplazables)')
pdf.ln(3)
pdf.body_text('Tip: Cualquier foto tomada en horizontal con un smartphone moderno tiene la calidad suficiente. Solo comprimela en squoosh.app antes de enviarla.')

# ─── FOOTER FINAL ───
pdf.ln(8)
pdf.set_fill_color(21, 82, 32)
pdf.set_text_color(255, 255, 255)
pdf.set_font('Helvetica', 'B', 10)
pdf.cell(0, 10, '  NIXAGA PETROL SRL - Proveedor Internacional de Hidrocarburos - nixagapetrol.com', fill=True, align='L')

output_path = r'C:\Users\herna\.gemini\antigravity\playground\ancient-planck\Nixaga\Nixaga_Petrol_Resumen_Proyecto.pdf'
pdf.output(output_path)
print(f'PDF generado exitosamente en: {output_path}')
