# Mobile PWA para Registro de Jornada

Este prototipo permite a los operarios registrar el inicio y cierre de su jornada conectando con Odoo.

## Configuración
1. Edita `config.js` y coloca la URL de tu servidor Odoo (`ODOO_URL`).
2. Abre `index.html` desde un servidor web (puedes usar `python3 -m http.server`).
3. Ingresa base de datos, usuario y contraseña para autenticar.

## Funcionalidades
- Selección de obra existente en Odoo.
- Inicio y fin de jornada con registro de materiales.
- Datos almacenados temporalmente si no hay conexión.
- Compatible como Progressive Web App para uso offline básico.

## Despliegue
Al ser una PWA estática, solo debes servir los archivos del directorio.
