# import os 
# import cv2
# import numpy as np
# import math


# cap = cv2.VideoCapture(0)


# while(1):
#     try #verifica o objeto "mão" na camera;
    
#     ret , frame = cap.read()
#     frame=cv2.flip(frame,1)
    
#     #Filtro de suavização
#     kernel=np.ones((3,3),np.unit8)
    
#     #região de interesse ROI
#     roi=frame[100:300,100:300]
    
#     #marcando area de interesse ROI
#     cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)
    
    
#     #Converte  cores RGB da imagem para HSV
#     hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
#     lower_skin = np.array([0,20,70], dtype=np.uint8)
    
#     upper_skin = np.array([20,255,255], dtype=np.uint8)
    
    
#     mask= cv2.dilate(mask,lower_skin,upper_skin)
#     mask = cv2.GaussianBlur(mask,(5,5),100)
    
#     contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
#     epsilon = 0.0005*cv2.arcLength(cnt,True)
#     approx = cv2.approxPolyDP(cnt,epsilon,True)
    
#     hull = cv2.convexHull(cnt)
#     arehull = cv2.contourArea(hull)
#     areacnt = cv2.contourArea(cnt)
#     arearatio=((areahull-areacnt)/areacnt)*100
    
#     #Definindo região de interesse
#         for i in range(defects.shape[0]):
#             s,e,f,d = detects[i,0]
#             start = tuple(approx[s][0])
#             end = tuple(approx[e][0])
#             far = tuple(approx[f][0])
#             pt = (100,180)-
            
#         L += 1
        
        
#         font =cv2.FONT_HERSHEY_SIMPLEX
#         if L==1:
#             if areacnt<2000:
#                 cv2.putText(frame,"Esperando Dados",(0,50))
    
    
    