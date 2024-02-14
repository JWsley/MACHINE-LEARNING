# REQUERIMENTS: pip install opencv-python


import cv2


haarcascades_folder = "OPENCV/haarcascades/haarcascade_frontalface_default.xml"

photo_folder = "OPENCV/img/photo_faces.png"

carregaAlgoritmo = cv2.CascadeClassifier(haarcascades_folder)




imagem = cv2.imread(photo_folder)


#Transforma a cor da imagem para cinza
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) 


faces = carregaAlgoritmo.detectMultiScale(imagemCinza)
print(faces)
for(x,y,l,a) in faces:
    # X = Eixo X | Y = Eixo Y | L = Largura | A = Altura
    #  Cria um retangulo em volta das faces detectadas  ||| (0,255,0) = cor rgb ||| ,2) = espessura da borda.    
    cv2.rectangle(imagem,(x,y),(x+l,y+a),(0,255,0),2)


cv2.imshow("cinza",imagemCinza)

cv2.imshow('Faces', imagem)

cv2.waitKey()