import cv2 #foto

img = cv2.imread('farol.jpg')  #carregar a imagem .. coloca o path

print(img.shape) #printar o tamanho

cv2.imshow('Image', img) #exibir a imagem . parametros: nome da janela e a img carregada
cv2.waitKey(0) #tempo de frame (nesse caso so tem 1 frame)


----------------------------------------------------------
import cv2 # carregar - video

myvideo = cv2.VideoCapture('runners.mp4')  #carregar meu video .. coloca o path

#atencao o que ta dentro do loop
while True:
    check,img = myvideo.read()
    imgRedim = cv2.resize(img, (420, 640))
    print(imgRedim.shape) #fica em loop printando as dimensoes
    cv2.imshow('myvideo',imgRedim)
    cv2.waitKey(1) #acelerado. 10 fica melhor

____________________________________________________________

import cv2

#-- modo bracal --
##cortar uma imagem com as dimensoes selecionadas pelo paint

img = cv2.imread('farol.jpg')
print(img.shape) #printar no terminal as dimensoes

#y 310-520
#x 120-420
recorte = img[310:520, 120:420]
cv2.imshow('Imagem Normal', img)
cv2.imshow('Recorte', recorte)

cv2.waitKey(0)

------------------------------------------------------------------------------------

import cv2

##cortar uma imagem com as dimensoes selecionadas pelo paint

img = cv2.imread('farol.jpg')

dim =cv2.selectROI('Selecione a area de recorte!', img, False)
print(dim)

v1 = int(dim[0]) #salva em uma variavel .. pois
#dim == é um array com 4 dimencoes
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])

recorte = img[v2:v2+v4, v1:v1+v3]

cv2.imshow('Recorte', recorte)

cv2.waitKey(0)

----------------------------------------------------
# salvando recorte da imagem que eu mesma faço 
import cv2

img = cv2.imread('farol.jpg')

dim =cv2.selectROI('Selecione a area de recorte!', img, False)
cv2.destroyWindow('Selecione a area de recorte!')

v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])

recorte = img[v2:v2+v4, v1:v1+v3]
caminho = 'recortes/'
nome_arquivo = input('Digite o nome do arquivo: ')

cv2.imwrite( '{caminho}{nome_arquivo}.jpg, recorte)
print('Imagem salva com sucesso')

cv2.waitKey(0)

------------------------------------------

            











