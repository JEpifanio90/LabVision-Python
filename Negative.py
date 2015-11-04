#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'José Epifanio'
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image
class Negative():
    def __init__(self, image):
        self.imag = image
        self.heigth = image.size[0]
        self.width = image.size[1]
        self.newImag = Image.new(self.imag.mode, self.imag.size)

    def convert(self):
        for x in range(self.heigth):
            for y in range(self.width):
                red, green , blue = self.imag.getpixel((x,y))
                red = abs(red-255)
                green= abs(green-255)
                blue= abs(blue-255)
                self.newImag.putpixel((x,y),(red,blue,green))
        self.newImag.save("negative1.png",self.imag.format)
        self.newImag.show()
        print("Done...")

def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    nega=Negative(Image.open(str(usrImag)))
    nega.convert()


if __name__ == '__main__':
    main()