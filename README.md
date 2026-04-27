<h1 align="left">Automatización de Mensajes de WhatsApp ✆</h1>

###

<p align="left">Este proyecto permite enviar mensajes personalizados de forma automática a múltiples contactos de WhatsApp utilizando Python. Es ideal para notificaciones, recordatorios o comunicación masiva controlada. No hace uso de la API de WhatsApp por lo que no hay un limite de mensajes e intentos, utiliza tiempos de espera para evitar el baneo de cuentas y es compatible con archivos de excel en caso de contar con una cartelera de clientes establecidos por enviar mensaje especifico y personalizado con sus datos.</p>

###

<h2 align="left">Características</h2>

###

<p align="left">- Envío automático de mensajes personalizados<br>- Lectura de contactos desde un archivo CSV<br>- Automatización del navegador para enviar mensajes<br>- Manejo de errores por contacto<br>- Pausas de seguridad para evitar bloqueos</p>

###

<h2 align="left">Tecnologías utilizadas</h2>

###

<p align="left">- Python 3<br>- pywhatkit<br>- pyautogui<br>- keyboard<br>- csv (librería estándar)<br>- os (librería estándar)<br>- time (librería estándar)</p>

###

<h2 align="left">Estructura del proyecto</h2>

###
```bash
Automate-WhatsApp-Messages
┣ whatssapp.py
┣ contactos.csv
┗ README.md

```
###

<h2 align="left">Requisitos</h2>

###

<p align="left">Antes de ejecutar el script, asegúrate de tener:<br><br>- Python instalado (recomendado 3.8 o superior)<br>- Google Chrome instalado<br>- Sesión activa en WhatsApp Web<br><br>Instala las dependencias con:</p>

  ```bash
  pip install pywhatkit pyautogui keyboard
```

###

<h2 align="left">Formato del archivo CSV</h2>

###

<p align="left">El archivo contactos.csv debe tener la siguiente estructura:<p/>
  
```bash
  nombre completo,numero de telefono
  Juan Perez,+50588888888
  Maria Lopez,+50577777777
```
  Importante:
  - El número debe incluir el código de país (ejemplo: +505 para Nicaragua)
  - No agregar espacios innecesarios

###

<h2 align="left">Uso</h2>

###

Clona el repositorio:
```bash
git clone https://github.com/oscarMolina1523/Automate-WhatsApp-Messages.git
```

Accede al proyecto:

```bash
cd Automate-WhatsApp-Messages
```
Ejecuta el script:
```bash
python whatssapp.py
```

<h2 align="left">¿Cómo funciona?</h2>

###

<p align="left">1. Lee los contactos desde el archivo CSV<br>2. Genera un mensaje personalizado por cada contacto<br>3. Abre WhatsApp Web automáticamente<br>4. Escribe el mensaje<br>5. Simula la tecla Enter para enviarlo<br>6. Espera unos segundos antes de continuar con el siguiente contacto</p>

###

<h2 align="left">Consideraciones importantes</h2>

###

<p align="left">- No envíes mensajes masivos de forma agresiva (puedes ser bloqueado por WhatsApp)<br>- Ajusta los tiempos (wait_time, sleep) según tu conexión<br>- Mantén el navegador visible (no minimizado)<br>- No uses el teclado/mouse mientras el script se ejecuta</p>

###

<h2 align="left">Manejo de errores</h2>

###

<p align="left">El sistema detecta errores por contacto y continúa con el siguiente sin detener todo el proceso.</p>

###

<h2 align="left">Personalización</h2>

###

<p align="left">Puedes modificar el mensaje en esta línea:

  ```bash
  mensaje = f"Hola {nombre} ..."
```

###

<h2 align="left">Ejemplo de salida</h2>

###

```bash
🚀 Procesando envío para: Juan Perez (+50588888888)...
✅ Mensaje enviado con éxito a Juan Perez
Esperando 10 segundos para el siguiente...
```

###

<h2 align="left">Contribuciones</h2>

###

<p align="left">Las contribuciones son bienvenidas. Puedes hacer un fork del proyecto y enviar un pull request.</p>

###

<h2 align="left">Licencia</h2>

###

<p align="left">Este proyecto es de uso libre para fines educativos y personales.</p>

###

<h2 align="left">Autor</h2>

###

<p align="left">Desarrollado por Oscar Molina<br><br>GitHub: https://github.com/oscarMolina1523</p>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
</div>

###
