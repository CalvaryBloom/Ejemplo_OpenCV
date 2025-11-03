# Ejercicio 4 – Comparar filtros
#
# Basado en: ejemplo003_kernels.py
#   • Aplica 3 kernels distintos al mismo frame: desenfoque, realce y bordes verticales.
#   • Muestra las tres imágenes en ventanas diferentes.
# Objetivo: observar cómo cambia el resultado con diferentes kernels.

import cv2 as cv
import numpy as np

# --- CONFIGURACIÓN Y APERTURA DE LA CÁMARA ---
camera = cv.VideoCapture(0)
if not camera.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

print("Cámara abierta. Comparando filtros. Presiona 'q' para salir.")

# --- DEFINICIÓN DE KERNELS ---
# Se define un diccionario con solo los tres kernels.
kernels_a_comparar = {
    # 1. Desenfoque (Blur): Promedio simple 3x3
    "1. Desenfoque (Blur)": np.ones((3, 3), np.float32) / 9,

    # 2. Realce (Sharpen): Acentúa los detalles
    "2. Realce (Sharpen)": np.array([[0, -1, 0],
                                     [-1, 5, -1],
                                     [0, -1, 0]]),

    # 3. Bordes Verticales: Resalta las líneas verticales (tipo Sobel vertical)
    "3. Bordes Verticales": np.array([[-1, 0, 1],
                                      [-2, 0, 2],
                                      [-1, 0, 1]])
}

# --- BUCLE PRINCIPAL DE PROCESAMIENTO ---
while True:
    ret, frame = camera.read()

    if not ret:
        print("Advertencia: Error leyendo el flujo de video. Saliendo...")
        break

    # Mostrar la imagen original para referencia
    cv.imshow("0. Imagen Original", frame)

    # Aplicar cada kernel definido y mostrar el resultado en su propia ventana
    # El bucle recorre el diccionario 'kernels_a_comparar'
    for name, kernel in kernels_a_comparar.items():
        # cv.filter2D aplica el kernel a la imagen de entrada (frame).
        # El parámetro -1 mantiene la misma profundidad de bits de la imagen original.
        filtered = cv.filter2D(frame, -1, kernel)

        # Mostrar el resultado filtrado, usando el nombre del filtro como nombre de la ventana.
        cv.imshow(name, filtered)

    # CONTROL DE TECLADO
    # Salir con la tecla 'q'
    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        print("Tecla 'q' presionada. Cerrando la aplicación...")
        break

    # --- LIBERAR RECURSOS ---
if camera.isOpened():
    camera.release()

cv.destroyAllWindows()
print("Proceso finalizado.")