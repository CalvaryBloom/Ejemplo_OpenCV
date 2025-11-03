# Ejercicio 8 – Control de filtros con teclado
#
# Basado en: ejemplo003_kernels.py
#   • Usa teclas 1, 2, 3 para cambiar entre filtros:
#       - 1: desenfoque
#       - 2: realce
#       - 3: bordes
#   • Cambia dinámicamente el kernel aplicado en el bucle.
# Objetivo: manejar eventos de teclado y cambiar parámetros en tiempo real.

import cv2 as cv
import numpy as np

# --- DEFINICIÓN DE KERNELS DE CONVOLUCIÓN ---
# Kernels de convolución para cv.filter2D
KERNEL_BLUR = np.ones((3, 3), np.float32) / 9  # Desenfoque (Promedio Simple)
KERNEL_SHARPEN = np.array([[0, -1, 0],  # Realce
                           [-1, 5, -1],
                           [0, -1, 0]])
KERNEL_BORDERS = np.array([[-1, 0, 1],  # Bordes Verticales
                           [-2, 0, 2],
                           [-1, 0, 1]])

# --- CONFIGURACIÓN Y APERTURA DE VIDEO ---
# Cargar video desde archivo
video_path = "video.mp4"
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error abriendo el video:", video_path)
    exit()

cv.namedWindow("Video", cv.WINDOW_AUTOSIZE)

# --- CONTROL DE ESTADO ---
# 1 = Desenfoque, 2 = Realce, 3 = Bordes
modo = 1  # Inicializamos en Desenfoque

# --- BUCLE PRINCIPAL DE PROCESAMIENTO ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("Fin del video o error de lectura.")
        break

    # 1. Definir la cadena de texto base del menú
    texto_menu = "Menu: 1=Desenfoque, 2=Realce, 3=Bordes, q=Salir"

    # 2. Procesar según el modo
    if modo == 1:
        # Modo Desenfoque (1)
        kernel_aplicar = KERNEL_BLUR
        vista = cv.filter2D(frame, -1, kernel_aplicar)
        texto = f"Modo: Desenfoque | {texto_menu}"

    elif modo == 2:
        # Modo Realce (2)
        kernel_aplicar = KERNEL_SHARPEN
        vista = cv.filter2D(frame, -1, kernel_aplicar)
        texto = f"Modo: Realce | {texto_menu}"

    elif modo == 3:
        # Modo Bordes (3)
        kernel_aplicar = KERNEL_BORDERS
        vista = cv.filter2D(frame, -1, kernel_aplicar)
        texto = f"Modo: Bordes Verticales | {texto_menu}"

    else:
        # Modo por defecto (si se presiona una tecla no mapeada que cambia el modo)
        vista = frame.copy()
        texto = f"Modo: Sin Filtro (Opción no válida) | {texto_menu}"

    # 3. Asegurar que la imagen sea en color para escribir texto
    # (Necesario porque los filtros podrían producir resultados de 1 canal si se aplicaran a 'gray')
    if len(vista.shape) == 2:
        vista_color = cv.cvtColor(vista, cv.COLOR_GRAY2BGR)
    else:
        vista_color = vista.copy()

    # 4. Mostrar texto en pantalla
    cv.putText(vista_color, texto, (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2, cv.LINE_AA)

    # 5. Mostrar frame
    cv.imshow("Video", vista_color)

    # 6. Teclas de control
    key = cv.waitKey(25) & 0xFF

    # Cambio dinámico de modo con las teclas 1, 2 y 3
    if key == ord('1'):
        modo = 1
    elif key == ord('2'):
        modo = 2
    elif key == ord('3'):
        modo = 3
    elif key == ord('q'):
        break

# --- LIBERAR RECURSOS ---
cap.release()
cv.destroyAllWindows()
print("Proceso finalizado.")