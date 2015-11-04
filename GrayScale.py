#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'José Epifanio'
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image
class GrayScale():
    def __init__(self, image):
        self.imag = image
        self.heigth = image.size[0]
        self.width = image.size[1]
        self.newImag = Image.new(self.imag.mode, self.imag.size)

    def grayScale(self):
        for x in range(self.heigth):
            for y in range(self.width):
                red, blue, green = self.imag.getpixel((x,y))
                gray = int(0.21 * red + 0.72 * green + 0.07 * blue)
                self.newImag.putpixel((x,y), (gray, gray, gray))
        self.newImag.save("testGray.png", self.imag.format)
        self.newImag.show()
        print("Done...")

def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    grayScale = GrayScale(Image.open(str(usrImag)))
    grayScale.grayScale()



if __name__ == '__main__':
    main()

