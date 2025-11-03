# Ejercicio 6 – Detección de bordes Canny
#
# Basado en: Ejemplo005_videoIO.py
#   • Abre un video o cámara.
#   • Aplica cv.Canny() y muestra resultado.
#   • Ajusta los valores de umbral para ver la diferencia.
# Objetivo: aprender uso del detector de bordes Canny.

import cv2 as cv

# --- CONFIGURACIÓN Y APERTURA DE VIDEO ---
# Ruta del archivo de entrada y salida
video_path = "video.mp4"
output_path = "salida_canny.mp4"

# Abrir el archivo de video
cap = cv.VideoCapture(video_path)
if not cap.isOpened():
    print("Error al abrir el video. Asegúrate de que 'video.mp4' existe.")
    exit()

# Obtener propiedades del video original (Necesario para VideoWriter)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

# Configurar el objeto para guardar video en MP4
# isColor=False porque vamos a escribir la imagen de bordes (que es en blanco y negro, 1 canal)
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

# Crear ventanas con tamaño fijo
cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.resizeWindow("Original", 400, 300)

cv.namedWindow("Canny", cv.WINDOW_NORMAL)
cv.resizeWindow("Canny", 400, 300)

print("Aplicando Canny. Presiona 'q' para salir. El video procesado se guardará en 'salida_canny.mp4'.")

# --- BUCLE PRINCIPAL DE PROCESAMIENTO ---
while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ Fin del video")
        break

    # Convertir a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # EJERCICIO: AJUSTAR UMBRALES
    # cv.Canny(imagen_gris, umbral_bajo, umbral_alto)
    # - Los píxeles con gradiente > umbral_alto son definitivamente bordes.
    # - Los píxeles con gradiente < umbral_bajo no son bordes.
    # - Los píxeles entre ambos se deciden por conectividad.
    # Prueba a cambiar los valores (ej: (50, 150), (10, 50), (150, 300)) para ver la diferencia.
    edges = cv.Canny(gray, 50, 150)

    # Mostrar resultados
    cv.imshow("Original", frame)
    cv.imshow("Canny", edges)

    # Guardar frame procesado en el archivo de salida
    out.write(edges)

    # Salir con la tecla 'q'. Espera 25 ms (~40 FPS de reproducción).
    key = cv.waitKey(25) & 0xFF
    if key == ord('q'):
        break

# --- LIBERAR RECURSOS ---
cap.release()
out.release()
cv.destroyAllWindows()
print("Recursos liberados. Archivo de salida guardado.")