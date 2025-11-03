# Ejercicio 7 – Guardar video procesado
#
# Basado en: Ejemplo005_videoIO.py
#   • Lee un video de entrada.
#   • Aplica un filtro (Canny o Sobel).
#   • Guarda el resultado con cv.VideoWriter.
#   • Asegúrate de que el archivo de salida tenga el mismo tamaño y FPS.
# Objetivo: practicar escritura de video en disco.

import cv2 as cv
import numpy as np

# --- CONFIGURACIÓN Y APERTURA DE VIDEO ---
video_path = "video.mp4"
output_path = "salida_sobel.mp4"

# Abrir el archivo de video de entrada
cap = cv.VideoCapture(video_path)
if not cap.isOpened():
    print("Error al abrir el video. Asegúrate de que 'video.mp4' existe.")
    exit()

# Obtener propiedades del video original (Necesario para VideoWriter)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

# Configurar el objeto para guardar video
fourcc = cv.VideoWriter_fourcc(*'mp4v')
# isColor=False porque la salida de Sobel combinada es de un solo canal (gris/bordes)
out = cv.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

# Crear ventanas
cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.resizeWindow("Original", 400, 300)

cv.namedWindow("Bordes (Sobel)", cv.WINDOW_NORMAL)
cv.resizeWindow("Bordes (Sobel)", 400, 300)

print(f"Video en procesamiento. Aplicando filtro Sobel. Guardando en: {output_path}")

# --- BUCLE PRINCIPAL DE PROCESAMIENTO ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("Fin del video")
        break

    # 1. Convertir a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 2. Aplicar detección de bordes Sobel
    # cv.Sobel(src, ddepth, dx, dy, ksize)

    # Derivada en la dirección X (detecta bordes verticales)
    sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)

    # Derivada en la dirección Y (detecta bordes horizontales)
    sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)

    # Convertir a valores absolutos y escalar a 8-bit para la visualización (Sobel usa valores negativos)
    abs_sobelx = cv.convertScaleAbs(sobelx)
    abs_sobely = cv.convertScaleAbs(sobely)

    # Combinar las dos derivadas para obtener la magnitud total del gradiente
    # Esta es la imagen que vamos a mostrar y guardar
    sobel_combined = cv.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)

    # Mostrar resultados
    cv.imshow("Original", frame)
    cv.imshow("Bordes (Sobel)", sobel_combined)

    # Guardar frame procesado en el archivo de salida
    out.write(sobel_combined)  # Escribimos la imagen combinada de Sobel

    # Salir con la tecla 'q'
    key = cv.waitKey(25) & 0xFF
    if key == ord('q'):
        break

# --- LIBERAR RECURSOS ---
cap.release()
out.release()
cv.destroyAllWindows()
print("Proceso finalizado. El video de bordes (Sobel) ha sido guardado.")