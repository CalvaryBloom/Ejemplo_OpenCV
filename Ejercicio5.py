# Ejercicio 5 – Filtro Laplaciano en video
#
# Basado en: ej004_ArchivoVideo.py
#   • Lee un video desde archivo.
#   • Convierte a gris y aplica un filtro Laplaciano.
#   • Muestra el video original y el de bordes.
# Objetivo: procesar un video frame a frame y usar convoluciones.

import cv2 as cv
import numpy as np

# --- CONFIGURACIÓN Y APERTURA DE VIDEO ---
# Ruta del archivo de video
video_path = "video.mp4"

# Abrir el archivo de video para lectura frame a frame
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error al abrir el video: {video_path}. Asegúrate de que existe el archivo.")
    exit()

# Kernel para detección de bordes (Laplace)
# Esta matriz 3x3 aproxima el Laplaciano, que detecta bordes.
kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])

# Crear ventanas y fijar tamaño inicial
cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.resizeWindow("Original", 854, 480)

cv.namedWindow("Bordes", cv.WINDOW_NORMAL)
cv.resizeWindow("Bordes", 854, 480)

print("Video abierto y filtro Laplaciano aplicado. Presiona 'q' para salir.")

# --- BUCLE PRINCIPAL DE PROCESAMIENTO ---
while True:
    # Leer el siguiente frame
    ret, frame = cap.read()

    # Si no hay más frames o hay un error de lectura, salir del bucle
    if not ret:
        print("Fin del video o error al leer el archivo. Saliendo...")
        break

    # 1. Convertir a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 2. Aplicar filtro Laplaciano (convolución)
    # convoluciona la imagen gris con el kernel
    edges = cv.filter2D(gray, -1, kernel)

    # 3. Mostrar resultados en ventanas
    cv.imshow("Original", frame)
    cv.imshow("Bordes", edges)

    # Esperar tecla (25 ms). El valor 25 ms intenta simular unos 40 FPS de visualización.
    key = cv.waitKey(25) & 0xFF

    # Salir si presionamos 'q'
    if key == ord('q'):
        break

# --- LIBERAR RECURSOS ---
cap.release()
cv.destroyAllWindows()
print("Proceso finalizado.")