import cv2 as cv
import numpy as np

# Configuración de la cámara
camera = cv.VideoCapture(0)
if not camera.isOpened():
    print("Error abriendo la cámara")
    exit()

cv.namedWindow("Original", cv.WINDOW_AUTOSIZE)

# Definición de kernels
kernels = {
    "Desenfoque": np.ones((3,3), np.float32) / 9,
    "Realce (Sharpen)": np.array([[0,-1,0],
                                  [-1,5,-1],
                                  [0,-1,0]]),
    "Bordes Verticales": np.array([[-1,0,1],
                                    [-2,0,2],
                                    [-1,0,1]]),
    "Laplace": np.array([[0,-1,0],
                         [-1,4,-1],
                         [0,-1,0]]),
    "Kernel personalizado": np.array([[ 1.0,-2.0, 1.0],
                                    [-1.0,-2.0, 1.0],
                                    [-1.0, 2.0, 1.0]])
}

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error leyendo el video")
        exit()

    # Convertimos a escala de grises para ver mejor los efectos
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Mostrar imagen original
    cv.imshow("Original", frame)
    cv.imshow("OriginalGris", gray)

    # Aplicar cada kernel y mostrar resultado en su ventana
    for name, kernel in kernels.items():
        filtered = cv.filter2D(frame, -1, kernel)
        cv.imshow(name, filtered)

    # Salir con la tecla 'q'
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        camera.release()
        cv.destroyAllWindows()
        exit()

