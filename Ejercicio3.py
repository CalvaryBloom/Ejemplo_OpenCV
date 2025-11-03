# Ejercicio 3 – Filtro de desenfoque
#
# Basado en: ejemplo003_kernels.py
#   • Usa un kernel de 3×3 de promedio (np.ones((3,3))/9) para aplicar un blur.
#   • Muestra la imagen original y la filtrada.
# Objetivo: comprender el uso de cv.filter2D y matrices kernel.

import cv2 as cv
import numpy as np

# --- CONFIGURACIÓN Y APERTURA DE LA CÁMARA ---
# Abrir el flujo de video de la cámara predeterminada (índice 0)
camera = cv.VideoCapture(0)

# Comprobar si la cámara se abrió correctamente
if not camera.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Definición del Kernel de Desenfoque (Blur)
# np.ones((3,3))/9 crea una matriz 3x3 de unos, dividida por 9.
# Esto toma el valor promedio de los 9 píxeles alrededor de cada punto, desenfocando la imagen.
BLUR_KERNEL = np.ones((3, 3), np.float32) / 9

print("Cámara abierta. Mostrando video original y desenfocado. Presiona 'q' para salir.")

# --- BUCLE PRINCIPAL DE PROCESAMIENTO ---
while True:
    # Capturar el siguiente fotograma
    ret, frame = camera.read()

    # Si no se pudo leer el fotograma, salir del bucle
    if not ret:
        print("Advertencia: Error leyendo el flujo de video. Saliendo...")
        break

    # APLICAR FILTRO
    # cv.filter2D aplica la convolución 2D.
    # - frame: La imagen original (entrada).
    # - -1: Indica que la profundidad de bits de la salida será la misma que la de la entrada (8 bits por canal).
    # - BLUR_KERNEL: La matriz que define la operación de filtrado.
    filtered_image = cv.filter2D(frame, -1, BLUR_KERNEL)

    # MOSTRAR
    # Mostrar la imagen original
    cv.imshow("1. Imagen Original", frame)
    # Mostrar la imagen con el filtro de desenfoque aplicado
    cv.imshow("2. Imagen Filtrada (Desenfoque 3x3)", filtered_image)

    # CONTROL DE TECLADO
    # Espera 1ms por un evento de teclado. Salir con 'q'.
    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        print("Tecla 'q' presionada. Cerrando la aplicación...")
        break

    # --- LIBERAR RECURSOS ---
# Liberar el objeto VideoCapture
if camera.isOpened():
    camera.release()

# Cerrar todas las ventanas de OpenCV
cv.destroyAllWindows()
print("Proceso finalizado.")