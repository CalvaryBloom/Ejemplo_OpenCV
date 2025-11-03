# Ejercicio 10 – Mini proyecto: cámara con modos
#
# Basado en: todos los anteriores
# Crea un programa con las siguientes funciones:
#   • Modo 1: mostrar cámara normal.
#   • Modo 2: mostrar escala de grises.
#   • Modo 3: mostrar bordes Canny.
#   • Modo 4: aplicar filtro de realce.
# Cambia de modo con teclas 1–4. Cierra con q.
# Objetivo: integrar lectura de cámara, filtros, control de teclado y visualización.

import cv2 as cv
import numpy as np

# --- DEFINICIÓN DE KERNEL ---
# Kernel para el Modo 4: Filtro de Realce (Sharpen)
KERNEL_SHARPEN = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

# --- CONFIGURACIÓN Y APERTURA DE LA CÁMARA ---
camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("Error: No se pudo abrir la cámara. Asegúrate de que esté disponible.")
    exit()

# Creamos la ventana con la opción WINDOW_NORMAL para que sea redimensionable
cv.namedWindow("Cámara con Modos", cv.WINDOW_NORMAL)
# Establecemos un tamaño fijo más pequeño y manejable para la visualización
cv.resizeWindow("Cámara con Modos", 640, 480)

# --- CONTROL DE ESTADO ---
modo = 1
print("Cámara abierta. Modos disponibles: 1=Normal, 2=Gris, 3=Canny, 4=Realce. Presiona 'q' para salir.")

# --- BUCLE PRINCIPAL DE PROCESAMIENTO ---
while True:
    ret, frame = camera.read()

    if not ret:
        print("Advertencia: Error leyendo el flujo de video. Saliendo...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 1. Definir la cadena de texto base del menú
    texto_menu = "Menu: 1=Normal, 2=Gris, 3=Canny, 4=Realce, q=Salir"

    # 2. PROCESAR SEGÚN EL MODO
    if modo == 1:
        vista = frame.copy()
        texto = f"Modo 1: Normal | {texto_menu}"

    elif modo == 2:
        vista = gray
        texto = f"Modo 2: Escala de Grises | {texto_menu}"

    elif modo == 3:
        vista = cv.Canny(gray, 50, 150)
        texto = f"Modo 3: Bordes Canny | {texto_menu}"

    elif modo == 4:
        vista = cv.filter2D(frame, -1, KERNEL_SHARPEN)
        texto = f"Modo 4: Filtro de Realce | {texto_menu}"

    else:
        vista = frame.copy()
        texto = f"Modo Inválido | {texto_menu}"

    # 3. Preparación de la vista para la visualización (asegura BGR para texto)
    if len(vista.shape) == 2:
        vista_color = cv.cvtColor(vista, cv.COLOR_GRAY2BGR)
    else:
        vista_color = vista.copy()

    # 4. Mostrar texto en pantalla
    # Reducir el 'fontScale' a 0.5 para asegurar que quepa
    cv.putText(vista_color, texto, (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv.LINE_AA)  # Texto verde

    # 5. Mostrar frame
    cv.imshow("Cámara con Modos", vista_color)

    # 6. Control de Teclas 1-4 y 'q'
    key = cv.waitKey(1) & 0xFF

    if key == ord('1'):
        modo = 1
    elif key == ord('2'):
        modo = 2
    elif key == ord('3'):
        modo = 3
    elif key == ord('4'):
        modo = 4
    elif key == ord('q'):
        break

    # --- LIBERAR RECURSOS ---
if camera.isOpened():
    camera.release()
cv.destroyAllWindows()
print("Proceso finalizado. Recursos de la cámara liberados.")