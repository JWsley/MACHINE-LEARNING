# REQUERIMENTS: pip install opencv-python


# Eyes

import cv2




photo_folder = "OPENCV/img/photo_faces2.png"

carregaFace = cv2.CascadeClassifier("OPENCV/haarcascades/haarcascade_frontalface_default.xml")
carregaOlho = cv2.CascadeClassifier("OPENCV/haarcascades/haarcascade_eye.xml")


imagem = cv2.imread(photo_folder)


imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) 

faces = carregaFace.detectMultiScale(imagemCinza)
print(faces)
for(x,y,l,a) in faces:    
   marcador =  cv2.rectangle(imagem,(x,y),(x+l,y+a),(0,255,0),2)
   
   # Calcula as proporsoêes do olho dentro da face ja reconhecida
   localOlho = imagem[y:y + a,x:x + l]
   localOlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
   detectado = carregaOlho.detectMultiScale(localOlhoCinza,scaleFactor=1.08,minNeighbors=9)
   
   
   #Desenha um retangulo nos olhos seguindo a mesma lógica dos Rostos
   for(Ox,Oy,Ol,Oa) in detectado:
       marcador_olho = cv2.rectangle(localOlho,(Ox,Oy),(Ox+Ol,Oy+Oa),(255,0,0),2)



cv2.imshow('Faces_Eyes', imagem)

cv2.waitKey()