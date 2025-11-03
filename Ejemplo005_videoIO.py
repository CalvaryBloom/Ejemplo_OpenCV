import cv2 as cv

# Ruta del archivo de entrada y salida
video_path = "video.mp4"
output_path = "salida.mp4"

# Abrir el archivo de video
cap = cv.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ Error al abrir el video")
    exit()

# Obtener propiedades del video original
width  = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv.CAP_PROP_FPS)

# Configurar el objeto para guardar video en MP4 (usa códec mp4v)
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

# Crear ventanas con tamaño fijo
cv.namedWindow("Original", cv.WINDOW_NORMAL)
cv.resizeWindow("Original", 400, 300)

cv.namedWindow("Canny", cv.WINDOW_NORMAL)
cv.resizeWindow("Canny", 400, 300)

while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ Fin del video")
        break

    # Convertir a escala de grises
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Aplicar detección de bordes Canny
    edges = cv.Canny(gray, 100, 200)

    # Mostrar resultados
    cv.imshow("Original", frame)
    cv.imshow("Canny", edges)

    # Guardar frame procesado en el archivo de salida
    out.write(edges)

    # Salir con la tecla 'q'
    key = cv.waitKey(25) & 0xFF
    if key == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv.destroyAllWindows()