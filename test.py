import pywhatkit as kit
import time
import keyboard
import pyautogui  # Importante para controlar el mouse

# Lista de contactos
contactos = [
    ("Mario", "+50586917823")
]

# Obtener el tamaño de la pantalla para hacer clic en el centro
width, height = pyautogui.size()

for nombre, numero in contactos:
    try:
        mensaje = f"Hola {nombre} soy joshua, este es un mensaje personalizado de whatsap para automatizar envios de mensajes."
        print(f"Preparando envío para {nombre}...")
        
        # 1. Abrir WhatsApp y escribir el mensaje
        kit.sendwhatmsg_instantly(
            phone_no=numero, 
            message=mensaje, 
            wait_time=22, # Un poco más de tiempo por si el internet está lento
            tab_close=True,
            close_time=3
        )
        
        # 2. ASEGURAR EL FOCO: Hacemos un clic en el centro de la pantalla
        # Esto asegura que el navegador esté activo y el cursor en el chat
        pyautogui.click(width / 2, height / 2) 
        time.sleep(1)
        
        # 3. PRESIONAR ENTER
        keyboard.press('enter')
        
        print(f"✅ Mensaje enviado a {nombre}")
        
        # Espera de seguridad entre personas
        time.sleep(8) 
        
    except Exception as e:
        print(f"❌ Error con {nombre}: {e}")

print("--- Proceso completado ---")