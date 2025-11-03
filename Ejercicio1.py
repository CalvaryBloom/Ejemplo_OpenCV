# Ejercicio 1 – Mostrar imagen y agregar texto
#
# Basado en: ej001_holaMundo.py
#   • Carga una imagen cualquiera.
#   • Dibuja un rectángulo, un círculo y un texto con tu nombre.
#   • Muestra la imagen final y guárdala en un archivo nuevo (resultado.jpg).
# Objetivo: aprender dibujo y escritura de texto en imágenes (cv.rectangle, cv.circle, cv.putText, cv.imwrite).

import cv2 as cv
import numpy as np

print(cv.__version__)

# Carga imagen a color
img = cv.imread('chica.png')

# Comprobar que la imagen se cargó correctamente
if img is None:
    raise FileNotFoundError("No se encontró 'chica.png'. Revisa la ruta/nombre del archivo")
else:
    # --- PASO 1: Dibuja un rectángulo ---
    # Coordenadas: (10, 10) esquina superior izquierda, (200, 100) esquina inferior derecha
    # Color: (0, 255, 0) = Verde (BGR)
    # Grosor: 2
    cv.rectangle(img, (10, 10), (200, 100), (0, 255, 0), 2)

    # --- PASO 2: Dibuja un círculo ---
    # Centro: (175, 200)
    # Radio: 50
    # Color: (0, 0, 255) = Rojo (BGR)
    # Grosor: 1
    cv.circle(img, (175, 200), 50, (0, 0, 255), 1)

    # --- PASO 3: Dibuja un texto con mi nombre ---
    cv.putText(img, 'Borja Pardo', (15, 90), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # --- PASO 4: Muestra la imagen  ---
    cv.imshow('Imagen', img)

    # --- PASO 5: Guarda la imagen final ---
    cv.imwrite('resultado.jpg', img)

    # --- PASO 6: Espera y cierra ---
    cv.waitKey(0)  # 0 = Espera indefinida
    cv.destroyAllWindows()  # Cierra la(s) ventana(s)