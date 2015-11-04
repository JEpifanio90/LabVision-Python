#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Josefoo'
import cv2
import numpy as np

y = raw_input("Ingrese nombre de la imagen: ")
img = cv2.imread(y)
gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
borde = cv2.Canny(gr,50,150,apertureSize = 3)
cv2.imshow('Bordes',borde)
print "Presione cualquier tecla."
cv2.waitKey(0)
cv2.destroyAllWindows()
lines = cv2.HoughLines(borde,1,np.pi/180,200)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('linesDetectionTest.jpg',img)
