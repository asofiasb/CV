import cv2

camera = cv2.VideoCapture(0)

while True:
    check, img = camera.read()

    cv2.imshow('Web can', img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #cria uma condicional p reproduzir
        #1fps infinitamente ou ate input = q(teclado
        break


