import cv2

algoritmo = cv2.CascadeClassifier("OPENCV/haarcascades/haarcascade_frontalface_default.xml")

imagem = cv2.imread("OPENCV/img/photo_faces.png")

imagemCinza = cv2.cvtColor(imagem,  cv2.COLOR_BGR2GRAY)


faces = algoritmo.detectMultiScale(imagemCinza,scaleFactor=1.02,minNeighbors=3,minSize=(35,35))

print(faces)


for(x,y,a,l) in faces:
    cv2.rectangle(imagem,(x,y),(x+l,x+a),(255,0,255),2)
    
cv2.imshow("faces",imagem)
cv2.waitKey()
    
