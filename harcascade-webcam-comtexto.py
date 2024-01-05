import cv2

camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier(r'/home/assb/Downloads/VC/pythonProject1/cascade/arquivos/cascades/haarcascade_smile.xml')

while True:
    check, img = camera.read()

    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    objetos = classificador.detectMultiScale(imgCinza, minSize=(50, 50), scaleFactor=1.5)

    texto = "SORRISINHOOOO"  # Corrigido: Movido para dentro do loop

    for x, y, l, a in objetos:
        cv2.rectangle(img, (x, y), (x + l, y + a), (255, 0, 0), 2)
        cv2.putText(img, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # Corrigido: Coordenadas ajustadas

    cv2.imshow('Imagem', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
