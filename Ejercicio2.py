# Ejercicio 2 – Mostrar video de la cámara
#
# Basado en: ej002_Camera.py
#   • Abre la cámara (cv.VideoCapture(0)).
#   • Muestra el video original en color y en escala de grises.
#   • Cierra con la tecla q.
# Objetivo: usar lectura de cámara en tiempo real y control de teclado (cv.waitKey).

import cv2 as cv
import numpy as np

# --- CONFIGURACIÓN Y APERTURA DE LA CÁMARA ---
# Abrir la cámara principal (índice 0)
camera = cv.VideoCapture(0)

# Comprobar si la cámara se abrió correctamente
if not camera.isOpened():
    print("Error: No se pudo abrir el flujo de video o archivo.")
    exit()  # Salir completamente si no se puede abrir la cámara

print("Cámara abierta. Mostrando video en color y gris. Presiona 'q' para salir.")

# --- BUCLE PRINCIPAL DE PROCESAMIENTO ---
while True:
    # Capturar el siguiente fotograma
    ret, frame = camera.read()
    # ret (booleano) indica si la lectura fue exitosa; frame contiene la imagen

    # Si no se pudo leer el fotograma (ret es False), salir del bucle
    if not ret:
        print("⚠️ Advertencia: Error leyendo el flujo de video. Saliendo...")
        break  # Se usa 'break' para poder limpiar los recursos al final

    # CONVERSIÓN
    # Convertir el fotograma a escala de grises
    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # MOSTRAR
    # Muestra el video original en color
    cv.imshow("1. Video Original (Color)", frame)
    # Muestra el video en escala de grises
    cv.imshow("2. Video Escala de Grises", gray_image)

    # CONTROL DE TECLADO
    # Espera 1ms por un evento de teclado.
    key = cv.waitKey(1) & 0xFF

    # Si la tecla presionada es 'q', salir del bucle
    if key == ord('q'):
        print("Tecla 'q' presionada. Cerrando las ventanas...")
        break

    # --- LIBERAR RECURSOS ---
# Liberar el objeto VideoCapture
if camera.isOpened():
    camera.release()

# Cerrar todas las ventanas de OpenCV
cv.destroyAllWindows()
print("Proceso finalizado.")