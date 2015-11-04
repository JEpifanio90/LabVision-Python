#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Josefoo'
from math import log1p
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image

class Threshold():

    def __init__(self,image):
        self.imag=image
        self.width=image.size[0]
        self.height=image.size[1]
        self.newImag= Image.new(self.imag.mode,self.imag.size)

    def threshold(self,threshold):
        UMBRAL = threshold
        for x in xrange(self.width):
            for y in xrange(self.height):
                r,g,b = self.imag.getpixel((x,y))
                if (r+g+b)/3 > UMBRAL:
                    self.newImag.putpixel((x,y),(255,255,255))
                else:
                    self.newImag.putpixel((x,y),(0,0,0))
        self.newImag.save("threshold.png",self.imag.format)
        self.newImag.show()
        print("Done...")




def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    thres=Threshold(Image.open(str(usrImag)))
    value =int(raw_input("Give me the threshold value"))
    thres.threshold(value)

if __name__=="__main__":
    main()