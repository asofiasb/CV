import cv2

#carrega nossa img principal
img = cv2.imread('piramide.jpg')

#redmencionar nossa img principal
img = cv2.resize(img, (500, 400))

#aplica o cinza
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#aplica o blur
imgBlur = cv2.GaussianBlur(imgCinza,(7,7), 0)
#pq o blur? pq facilita o algortimo .. suavizando os detalhes e facilitando

#achar os contornos na imagem //tharrold = limite de seguranca
imgCanny = cv2.Canny(img, 50, 100)

#dilatacao .. expande todos os pontos
imgDilat = cv2.dilate(imgCanny, (5,5), iterations= 5)

# erode - contrario a dilatacao . diminui os pontos .. desfragmenta
imgErode = cv2.erode(imgCanny, (5,5), iterations= 2)

#imprime a imagem:

#cv2.imshow('Img original', img)
#cv2.imshow('Img CINZA', imgCinza)
#cv2.imshow('Img blur', imgBlur)
cv2.imshow('Img Canny', imgCanny)
#cv2.imshow('Img dilatada', imgDilat)
#cv2.imshow('Img com Erode', imgErode)

#open = erosao> dilatacao . retirar ruidos e limpar a imagem
#closing =  dilatacao > erosao .. limpar O OBJETO e focar nele e nao na imagem como um todo

# pode usar na tora usando uma funcao dps a outra mas tem funcao q enchuta isso no open cv

imgOpening = cv2.morphologyEx(imgCanny, cv2.MORPH_OPEN,(5,5))
imgClosing = cv2.morphologyEx(imgCanny, cv2.MORPH_CLOSE,(5,5))

cv2.imshow('Img ABERTA', imgOpening)
cv2.imshow('Img FECHADA', imgClosing)

cv2.waitKey(0)

