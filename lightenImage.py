#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Josefoo'
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image

class lightenImage():
    def __init__(self,image):
        self.imag=image
        self.width=image.size[0]
        self.height=image.size[1]
        self.newImag= Image.new(self.imag.mode,self.imag.size)

    def lighten(self,light):
        for x in range(self.width):
                for y in range(self.height):
                    r,g,b = self.imag.getpixel((x,y))
                    self.newImag.putpixel((x,y),(r+light,r+light,r+light))
                    ns=r,g,b
        self.newImag.save("ightenImage.png",self.imag.format)
        print("Done...")

def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    light=lightenImage(Image.open(str(usrImag)))
    value =int(raw_input("Give me the lighten value"))
    light.lighten(value)

if __name__=="__main__":
    main()