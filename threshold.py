import cv2

img = cv2.imread('img02.jpg')
img = cv2.resize(img,(700,800))
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,this1 = cv2.threshold(imgCinza, 127, 255, cv2.THRESH_BINARY)
#127 LIMITE DO PIXEL, MAIOR QUE 127 = PRETA. MENOR = BRANCA
#... BINARIO.. SO DUAS CORES... facilita para transformar dpps em scaner e tirar so o txto
th2 = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25,16)
th3 = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25,16)

cv2.imshow('Original', img)
cv2.imshow('TH1', this1)
cv2.imshow('TH2', th2)
cv2.imshow('TH3', th3)


#tem sombra = thrhoud adaptativo ...


cv2.waitKey(0)
