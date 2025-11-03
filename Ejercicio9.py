# Ejercicio 9 – Dibujar bordes sobre el video original
#
# Basado en: ej004_ArchivoVideo.py o Ejemplo005_videoIO.py
#   • Calcula bordes con Canny.
#   • Usa cv.addWeighted() o cv.cvtColor(edges, cv.COLOR_GRAY2BGR) para superponerlos al video original (borde coloreado).
# Objetivo: combinar resultados de procesamiento con imágenes originales.

import cv2 as cv
import numpy as np

# --- CONFIGURACIÓN Y APERTURA DE VIDEO ---
video_path = "video.mp4"
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error abriendo el video:", video_path)
    exit()

cv.namedWindow("Video Original", cv.WINDOW_AUTOSIZE)
cv.namedWindow("Bordes Superpuestos", cv.WINDOW_AUTOSIZE)

print("Aplicando Canny y superponiendo bordes al video original. Presiona 'q' para salir.")

# --- BUCLE PRINCIPAL DE PROCESAMIENTO ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("Fin del video o error de lectura.")
        break

    # 1. Calcular bordes con Canny
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Canny genera una imagen binaria (blanco y negro) de 1 canal.
    edges = cv.Canny(gray, 50, 150)

    # 2. Preparar el mapa de bordes para la superposición

    # Convertir la imagen de bordes de 1 canal (gris) a 3 canales (BGR).
    # En este punto, los bordes seguirán siendo blancos.
    edges_color = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)

    # Creamos un frame de color rojo puro con el mismo tamaño que 'edges_color'
    red_color = np.zeros_like(edges_color)
    red_color[:, :] = [0, 0, 255]  # Establece todos los píxeles a Rojo (0, 0, 255)

    # Se aplica el color rojo solo en los píxeles donde 'edges' es blanco (255)
    borde_rojo = cv.bitwise_and(red_color, red_color, mask=edges)

    # 3. Superponer los bordes al video original usando cv.addWeighted()
    # Pesar la imagen original (frame) y los bordes coloreados (borde_rojo).
    # frame_superpuesto = frame + borde_rojo

    # Para superponer, a la imagen original le quitamos los píxeles donde hay bordes,
    # y luego le sumamos los bordes de color.

    # Eliminamos el borde del frame original (blackout)
    frame_sin_borde = cv.bitwise_and(frame, frame, mask=cv.bitwise_not(edges))

    # Sumamos el fondo sin bordes más el borde rojo
    frame_superpuesto = cv.add(frame_sin_borde, borde_rojo)

    # --- MOSTRAR RESULTADOS ---
    cv.imshow("Video Original", frame)
    cv.imshow("Bordes Superpuestos", frame_superpuesto)

    # --- CONTROL DE TECLADO ---
    key = cv.waitKey(25) & 0xFF
    if key == ord('q'):
        break

# --- LIBERAR RECURSOS ---
cap.release()
cv.destroyAllWindows()
print("Proceso finalizado.")