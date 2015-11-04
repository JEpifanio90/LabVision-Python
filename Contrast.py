#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'José Epifanio'
from math import log1p
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image
class Contrast():

    def __init__(self,image):
        self.imag=image
        self.width=image.size[0]
        self.height=image.size[1]
        self.newImag= Image.new(self.imag.mode,self.imag.size)

    def contrast(self,beta):
        for x in range(self.width):
            for y in range(self.height):
                gray, gray1, gray2 = self.imag.getpixel((x,y))
                maxim=max(gray,gray1,gray2)
                #minim=min(gray,gray1,gray2)
                q=int((maxim*((log1p(maxim+gray))/(log1p(maxim+maxim)))))
                #q=q*gray+beta
                self.newImag.putpixel((x,y),(q,q,q))
        self.newImag.save("testContrast1.jpg",self.imag.format)
        self.newImag.show()
        print("Done...")


def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    contra=Contrast(Image.open(str(usrImag)))
    beta =int(raw_input("Give me the beta value"))
    contra.contrast(beta)

if __name__=="__main__":
    main()
