import cv2
#necessário criar a pasta objetos para colocar os itens antes de rodar o codigo .

img = cv2.imread('objetos.jpg')

img = cv2.resize(img,(600, 500)) #muda o tamanho
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) #passa p cinza
imgCanny = cv2.Canny(imgCinza,30,200)
imgClose = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE,(7,7))

countours,hierarchy = cv2.findContours(imgClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

numero_objetos = 1

for i in countours:
    x, y,w,h = cv2.boundingRect(i)
    objeto = img[y:y+h, x:x+w]
    cv2.imwrite(f'objetos/objeto{numero_objetos}.jpg',objeto)
    cv2.rectangle(img,(x,y),(x+w, y+h), (255,0,0),2)
    numero_objetos += 1

#prints
cv2.imshow('Imagem', img)
cv2.imshow('Imagem Cinza', imgCinza)

cv2.waitKey(0)
