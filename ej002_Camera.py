import cv2 as cv
import numpy as np
import argparse

#CAMERA SETUP
camera = cv.VideoCapture(0)
if not camera.isOpened():
    print("Error opening video stream or file")
    exit()

cv.namedWindow("Camara",cv.WINDOW_AUTOSIZE) #crea la ventana
print("hola desde la camara")

#BUCLE PRINCIPAL
while True:
    ret, frame = camera.read()

    if not ret:
        print("Error reading video stream or file")
        exit()

    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)    #convertir imagen a escala de grises


    cv.imshow("Ventana", frame)                   #dibuja los frames
    cv.imshow("Ventana2", gray_image)

    key = cv.pollKey()                                     #activa el gestor de eventos para poder salir del bucle while
    if key == ord('q'):                                    #cierra la ventana al pulsar "q"
        cv.destroyAllWindows()
        if camera.isOpened():
            camera.release()
        exit()