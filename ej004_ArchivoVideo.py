import cv2 as cv
import numpy as np

# Ruta del archivo de video (cambia esto por tu archivo)
video_path = "video.mp4"

# Abrir el archivo de video
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error al abrir el video")
    exit()

# Kernel para detección de bordes (Laplace)
kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])



# Crear ventanas con tamaño fijo
cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.resizeWindow("Original", 854, 480)

cv.namedWindow("Bordes", cv.WINDOW_NORMAL)
cv.resizeWindow("Bordes", 854, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ Fin del video o error al leer el archivo")
        break

    # Convertir a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Aplicar filtro de detección de bordes
    edges = cv.filter2D(gray, -1, kernel)

    # Mostrar resultados en ventanas
    cv.imshow("Original", frame)
    cv.imshow("Bordes", edges)

    # Esperar tecla (25 ms) y salir si presionamos 'q'
    key = cv.waitKey(25) & 0xFF
    if key == ord('q'):
        break

# Liberar recursos
cap.release()
cv.destroyAllWindows()