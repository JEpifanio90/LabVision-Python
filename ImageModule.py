#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'José Epifanio, Ludim Sanchez'
from PIL import Image
from math import log1p
import math
import numpy # se utiliza en shifting, para obtener la media de cada
             # columna y fila de la matriz

class ImageModule:
    def __init__(self,image):
        self.imag=image
        self.width=image.size[0]
        self.height=image.size[1]
        self.newImag = Image.new(self.imag.mode, self.imag.size)
        self.archivoInput = open("../Images and Files/input.txt", "w") # escala de gris
        self.archivoOutput = open("../Images and Files/output.txt", "w") # matriz cuando se le aplica un operador

    def imprimirMatrizSalida(self):
        matrizImg = self.newImag.load()
        for x in xrange(self.width):
            for y in xrange(self.height):
                r = matrizImg[x,y][0]
                self.archivoOutput.write(str(r)+str(", "))
            self.archivoOutput.write("\n\n")
        self.archivoOutput.close()
        print("Done...")

    def grayScale(self):
        for x in range(self.width):
            for y in range(self.height):
                red, blue, green = self.imag.getpixel((x, y))
                gray = int((max(red,green,blue) + min (red,blue,green))/2)
                self.newImag.putpixel((x, y), (gray, gray, gray))
                self.archivoInput.write(str(gray)+str(", "))# LINEA AGREGADA
            self.archivoInput.write("\n\n") # LINEA AGREGADA
        self.newImag.save("../Images and Files/testGray.png", self.imag.format)
        self.archivoInput.close()
        print("Gray Scale Done...")

    def negative(self):
        for x in range(self.width):
            for y in range(self.height):
                red, green , blue = self.imag.getpixel((x,y))
                red = (255-red) # solo se toma uno, ya que los otros dos colores son iguales, porque la imagen esta en escala de gris
                self.newImag.putpixel((x,y),(red,red,red))
                self.archivoInput.write(str(red)+str(", "))# LINEA AGREGADA
            self.archivoInput.write("\n\n") # LINEA AGREGADA
        self.archivoInput.close()
        self.newImag.save("../Images and Files/negative.png",self.imag.format)
        print("Negative Done...")
        self.imprimirMatrizSalida()

    def changeRGB(self, tag, value):
        for x in range(self.width):
            for y in range(self.height):
                red,green,blue = self.imag.getpixel((x,y))
                if(tag=="red"):
                    red = value[0]
                    self.newImag.putpixel((x,y),(red,green,blue))
                elif(tag=="green"):
                    green=value[0]
                    self.newImag.putpixel((x,y),(red,green,blue))
                elif(tag=="blue"):
                    blue=value[0]
                    self.newImag.putpixel((x,y),(red,green,blue))
                elif(tag=="all"):
                    red=value[0]
                    green=value[1]
                    blue=value[2]
                    self.newImag.putpixel((x,y),(red,green,blue))

        self.newImag.save("../Images and Files/test"+tag+".png",self.imag.format)
        print("Done...")
        self.imprimirMatrizSalida()

    def contrast(self):
        for x in range(self.width):
            for y in range(self.height):
                gray, gray1, gray2 = self.imag.getpixel((x,y))
                maxim=max(gray,gray1,gray2)
                if maxim == 0:
                    maxim = 1
                q=int((maxim*((log1p(maxim+gray))/(log1p(maxim+maxim)))))
                self.newImag.putpixel((x,y),(q,q,q))
                self.archivoInput.write(str(q)+str(", "))# LINEA AGREGADA
            self.archivoInput.write("\n\n") # LINEA AGREGADA
        self.archivoInput.close()
        self.newImag.save("../Images and Files/testContrast1.png",self.imag.format)
        print("Done...")
        self.imprimirMatrizSalida()

    def mirrorHorizontal(self):
        w = self.width * 2
        h = self.height
        self.newImag = Image.new(self.imag.mode, (w,h)) # resize image
        matriz = self.imag.load()
        for x in xrange(self.width):
            for y in xrange(self.height):
                r = matriz[x,y][0]
                self.newImag.putpixel((x,y),(r,r,r))
                self.newImag.putpixel((w-x-1,y),(r,r,r))
                self.archivoOutput.write(str(r)+str(", "))# LINEA AGREGADA
            self.archivoOutput.write("\n\n") # LINEA AGREGADA
        self.archivoOutput.close()
        self.newImag.save("../Images and Files/mirrorHorizontal.png",self.imag.format)
        print("Done...")

    def mirrorVertical(self):
        matriz = self.imag.load()
        for x in xrange(self.width):
            for y in xrange(self.height):
                r = matriz[x,y][0]
                self.newImag.putpixel((self.width-x-1,self.height-y-1),(r,r,r))
                self.archivoInput.write(str(r)+str(", "))# LINEA AGREGADA
            self.archivoInput.write("\n\n") # LINEA AGREGADA
        self.archivoInput.close()
        self.newImag.save("../Images and Files/mirrorVertical.png",self.imag.format)
        print("Done...")
        self.imprimirMatrizSalida()

    def threshold(self,threshol):
        UMBRAL = threshol
        for x in xrange(self.width):
            for y in xrange(self.height):
                r,g,b = self.imag.getpixel((x,y))
                if (r+g+b)/3 > UMBRAL:
                    self.newImag.putpixel((x,y),(255,255,255))
                    self.archivoOutput.write(str(255)+str(", "))# LINEA AGREGADA
                else:
                    self.newImag.putpixel((x,y),(0,0,0))
                    self.archivoOutput.write(str(0)+str(", "))# LINEA AGREGADA
            self.archivoOutput.write("\n\n") # LINEA AGREGADA
        self.archivoOutput.close()
        self.newImag.save("../Images and Files/threshold.png",self.imag.format)
        print("Done...")

    def lightenImagen(self,light):
        for x in range(self.width):
            for y in range(self.height):
                r,g,b = self.imag.getpixel((x,y))
                self.newImag.putpixel((x,y),(r+light,r+light,r+light))
                ns=r,g,b
                self.archivoInput.write(str(ns)+str(", "))# LINEA AGREGADA
            self.archivoInput.write("\n\n") # LINEA AGREGADA
        self.archivoInput.close()
        self.newImag.save("../Images and Files/lightenImage.png",self.imag.format)
        print("Done...")
        self.imprimirMatrizSalida()

    def diagonalShifting(self):
        w = self.imag.size[0]
        h = self.imag.size[1]
        print w,",",h
        matrizImg = self.imag.load()# la imagen debe estar en escala de grises
        matriz = []
        for i in range(h):
            matriz.append([])
            for j in range(w):
                valor = (matrizImg[j,i][0] + matrizImg[j,i][1] + matrizImg[j,i][2]) / 3
                matriz[i].append(valor)
        #print numpy.array(matriz)
        matrixNm = numpy.array(matriz)
        promedioCol = numpy.median(matrixNm,axis=0)
        promedioFil = numpy.median(matrixNm,axis=1)
        print "Promedio columnas ",len(numpy.median(matrixNm,axis=0))
        print "Promedio filas    ",len(numpy.median(matrixNm,axis=1))
        # shift vertical
        mitadIm = int(math.floor(w/2))
        print mitadIm
        newIm = Image.new(self.imag.mode,self.imag.size)
        # se usa el de columnas
        for x in xrange(mitadIm):
            for y in xrange(h): # recorre para abajo
                if y == h-1: # 1 porque toma el pixel de la posicion x +1
                    r,g,b = self.imag.getpixel((0,y))
                    r1,g1,b1 = self.imag.getpixel((0,y))
                else:
                    r,g,b = self.imag.getpixel((x,y+1))
                    r1,g1,b1 = self.imag.getpixel((w-x-1,y+1))
                r = int((promedioCol[x] * r) / promedioCol[len(promedioCol)-x-1])
                #g = int((promedioCol[x] * g) / promedioCol[len(promedioCol)-x-1])
                #b = int((promedioCol[x] * b) / promedioCol[len(promedioCol)-x-1])
                r1 = int(((promedioCol[len(promedioCol)-x-1] * r1) / promedioCol[x]))
                #g1 = int(((promedioCol[len(promedioCol)-x-1] * g1) / promedioCol[x]))
                #b1 = int(((promedioCol[len(promedioCol)-x-1] * b1) / promedioCol[x]))
                self.newImag.putpixel((x,y),(r,r,r))#self.newImag.putpixel((x,y),(r,g,b))
                self.newImag.putpixel((w-x-1,y),(r1,r1,r1))#self.newImag.putpixel((w-x-1,y),(r1,g1,b1))
                ns = r,r1
                self.archivoInput.write(str(ns)+str(", "))# LINEA AGREGADA
            self.archivoInput.write("\n\n") # LINEA AGREGADA
        self.archivoInput.close()
        self.newImag.save("../Images and Files/shiftDiagonal.png",self.imag.format)
        print("Done...")
        self.imprimirMatrizSalida()

    def horizontalShifting(self):
        matrizImg = self.imag.load() # la imagen debe estar en escala de grises
        matriz = []
        for i in range(self.height):
            matriz.append([])
            for j in range(self.width):
                valor = (matrizImg[j,i][0] + matrizImg[j,i][1] + matrizImg[j,i][2]) / 3
                matriz[i].append(valor)
        #print numpy.array(matriz)
        matrixNm = numpy.array(matriz)
        promedioCol = numpy.median(matrixNm,axis=0)
        promedioFil = numpy.median(matrixNm,axis=1)
        print "Promedio columnas ",len(numpy.median(matrixNm,axis=0))
        print "Promedio filas    ",len(numpy.median(matrixNm,axis=1))
        # shift vertical
        mitadIm = int(math.floor(self.height/2))
        print mitadIm
        for y in xrange(self.width):
            for x in xrange(mitadIm):
                r,g,b = self.imag.getpixel((y,x))
                r1,g1,b1 = self.imag.getpixel((y,self.height-x-1))
                r = int((promedioFil[x] * r)/promedioFil[len(promedioFil)-x-1])
                g = int((promedioFil[x] * g)/promedioFil[len(promedioFil)-x-1])
                b = int((promedioFil[x] * b)/promedioFil[len(promedioFil)-x-1])
                r1 = int((promedioFil[len(promedioFil)-x-1] * r1) / promedioFil[x])
                g1 = int((promedioFil[len(promedioFil)-x-1] * g1) / promedioFil[x])
                b1 = int((promedioFil[len(promedioFil)-x-1] * b1) / promedioFil[x])
                self.newImag.putpixel((y,x),(r,g,b))
                self.newImag.putpixel((y,self.height-x-1),(r1,g1,b1))
                ns=r,g,b
                if x == mitadIm - 1:
                    r,g,b = self.imag.getpixel((y,x+1))
                    self.newImag.putpixel((y,x+1),(r,g,b))
                    ns=r,g,b
                self.archivoInput.write(str(ns)+str(", "))# LINEA AGREGADA
            self.archivoInput.write("\n\n") # LINEA AGREGADA
        self.archivoInput.close()
        self.newImag.save("../Images and Files/shiftHorizontal.png",self.imag.format)
        print("Done...")
        self.imprimirMatrizSalida()

    def verticalShifting(self):
        matrizImg = self.imag.load() # la imagen debe estar en escala de grises
        matriz = []
        for i in range(self.height):
            matriz.append([])
            for j in range(self.width):
                valor = (matrizImg[j,i][0] + matrizImg[j,i][1] + matrizImg[j,i][2]) / 3
                matriz[i].append(valor)
        #print numpy.array(matriz)
        matrixNm = numpy.array(matriz)
        promedioCol = numpy.median(matrixNm,axis=0)
        promedioFil = numpy.median(matrixNm,axis=1)
        print "Promedio columnas ",len(numpy.median(matrixNm,axis=0))
        print "Promedio filas    ",len(numpy.median(matrixNm,axis=1))
        # shift vertical
        mitadIm = int(math.floor(self.width/2))
        print mitadIm
        for x in xrange(mitadIm):
            for y in xrange(self.height): # recorre para abajo
                r,g,b = self.imag.getpixel((x,y))
                r1,g1,b1 = self.imag.getpixel((self.width-x-1,y))
                r = int((promedioCol[x] * r) / promedioCol[len(promedioCol)-x-1])
                #g = int((promedioCol[x] * g) / promedioCol[len(promedioCol)-x-1])
                #b = int((promedioCol[x] * b) / promedioCol[len(promedioCol)-x-1])
                r1 = int(((promedioCol[len(promedioCol)-x-1] * r1) / promedioCol[x]))
                #g1 = int(((promedioCol[len(promedioCol)-x-1] * g1) / promedioCol[x]))
                #b1 = int(((promedioCol[len(promedioCol)-x-1] * b1) / promedioCol[x]))
                self.newImag.putpixel((x,y),(r,r,r))#self.newImag.putpixel((x,y),(r,g,b))
                self.newImag.putpixel((self.width-x-1,y),(r1,r1,r1))#self.newImag.putpixel((self.width-x-1,y),(r1,g1,b1))
                ns=r,r1,g,b,b1,g1
                self.archivoInput.write(str(ns)+str(", "))# LINEA AGREGADA
            self.archivoInput.write("\n\n") # LINEA AGREGADA
        self.archivoInput.close()
        self.newImag.save("../Images and Files/shiftVertical.png",self.imag.format)
        print("Done...")
        self.imprimirMatrizSalida()

    def darkenImage(self,dark):
        for x in range(self.width):
            for y in range(self.height):
                r,g,b = self.imag.getpixel((x,y))
                self.newImag.putpixel((x,y),(abs(r-dark),abs(g-dark),abs(b-dark)))
                ns=r,g,b
                self.archivoInput.write(str(ns)+str(", "))# LINEA AGREGADA
            self.archivoInput.write("\n\n") # LINEA AGREGADA
        self.archivoInput.close()
        self.newImag.save("../Images and Files/darkenImage.png",self.imag.format)
        print("Done...")
        self.imprimirMatrizSalida()



def main():
    """
    imageModule = ImageModule(Image.open("testGray"))
    gris = imageModule.grayScale() # se trabaja con escala de grises, cualquier imagen de entrada
    imageModule = ImageModule(Image.open("gray"))
    imageModule.negative()
    """
    op=0
    while(op!=12):
        print("////Image Processing////")
        print("1.Negative")
        print("2.Contrast")
        print("3.RGB Manipulator")
        print("4.Threshold")
        print("5.Horizontal Shifting")
        print("6.Vertical Shifting")
        print("7.Diagonal Shifting")
        print("8.Horizontal mirror")
        print("9.Vertical mirror")
        print("10.Lighten an image")
        print("11.Darken an image")
        print("12.Exit")
        op=int(raw_input("What is thy bidding my master?"))
        imageModule=ImageModule(Image.open("../Images and Files/otter yawn.png"))
        imageModule.grayScale() # se trabaja con escala de grises, cualquier imagen de entrada
        imageModule=ImageModule(Image.open("../images and files/testGray.png"))
        if(op==1):
            imageModule.negative()
        elif(op==2):
            imageModule.contrast()
        elif(op==3):
            print("1.Red")
            print("2.Green")
            print("3.Blue")
            print("4.All of them")
            op=int(raw_input("¿Which one would you like to modify?"))
            if(op==1):
                print("Red")
                value=[]
                value.append(int(raw_input("Give the value for the 'red' channel: ")))
                imageModule.changeRGB("red",value)
            elif(op==2):
                print("Green")
                value=[]
                value.append(int(raw_input("Give the value for the 'green' channel: ")))
                imageModule.changeRGB("green",value)
            elif(op==3):
                print("Blue")
                value=[]
                value.append(int(raw_input("Give the value for the 'blue' channel: ")))
                imageModule.changeRGB("blue",value)
            else:
                print("all of them")
                value = []
                value.append(int(raw_input("Give me the red channel:")))
                value.append(int(raw_input("Give me the green channel:")))
                value.append(int(raw_input("Give me the blue channel:")))
                imageModule.changeRGB("all",value)
        elif(op==4):
            umbr=int(raw_input("Give me the threshold value: "))
            imageModule.threshold(umbr)
        elif(op==5):
            imageModule.horizontalShifting()
        elif(op==6):
            imageModule.verticalShifting()
        elif(op==7):
            imageModule.diagonalShifting()
        elif(op==8):
            imageModule.mirrorHorizontal()
        elif(op==9):
            imageModule.mirrorVertical()
        elif(op==10):
            light = int(raw_input("Give me how many tones you want: "))
            imageModule.lightenImagen(light) # NO ESTA FUNCIONANDO ESTO
        elif(op==11):
            dark = int(raw_input("Give me how many tones you want: "))
            imageModule.darkenImage(dark) # NO ESTA FUNCIONANDO ESTO local variable 'dark' referenced before assignment
        else:
            print("Good Bye, Tschüs, au revoir, até logo, Adios , master")


if __name__ == '__main__':
    main()
