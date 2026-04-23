import pywhatkit as kit
import time
import keyboard
import pyautogui
import csv  # Librería nativa para leer archivos CSV
import os

# Configuración del archivo
archivo_datos = "contactos.csv"

# Obtener el tamaño de la pantalla para el clic de enfoque
width, height = pyautogui.size()

# Verificar si el archivo existe antes de empezar
if not os.path.exists(archivo_datos):
    print(f"❌ Error: No se encontró el archivo '{archivo_datos}' en la carpeta.")
else:
    with open(archivo_datos, mode='r', encoding='utf-8-sig') as file:
        # Leemos el CSV usando el encabezado
        lector_csv = csv.DictReader(file)
        
        for fila in lector_csv:
            # Extraemos los datos de las columnas específicas
            nombre = fila['nombre completo']
            numero = fila['numero de telefono']
            
            try:
                mensaje = f"Hola {nombre} soy joshua, este es un mensaje personalizado de whatsap para automatizar envios de mensajes."
                print(f"🚀 Procesando envío para: {nombre} ({numero})...")
                
                # 1. Abrir WhatsApp y escribir el mensaje
                kit.sendwhatmsg_instantly(
                    phone_no=numero, 
                    message=mensaje, 
                    wait_time=22, 
                    tab_close=True,
                    close_time=3
                )
                
                # 2. Clic en el centro para asegurar el foco
                pyautogui.click(width / 2, height / 2) 
                time.sleep(1)
                
                # 3. Presionar Enter para enviar
                keyboard.press('enter')
                
                print(f"✅ Mensaje enviado con éxito a {nombre}")
                
                # Espera de seguridad entre contactos (evita bloqueos)
                print("Esperando 10 segundos para el siguiente...")
                time.sleep(10) 
                
            except Exception as e:
                print(f"❌ Error al enviar a {nombre}: {e}")

print("--- 🏁 Proceso de envío masivo completado ---")