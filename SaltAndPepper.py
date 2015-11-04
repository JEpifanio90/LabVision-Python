#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'José Epifanio'
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image
import random

class SaltAndPepper:

    def __init__(self,image):
        self.imag = image
        self.width= image.size[0]
        self.height= image.size[1]
        self.newImage = Image.new(self.imag.mode, self.imag.size)

    def saltAndPepper(self):
        flag = True
        tone = 0
        for x in range(self.width):
            for y in range(self.height):
                r,g,b = self.imag.getpixel((x,y))
                ran=random.randrange(0,(self.height*self.width))
                if (ran%2==0):
                    if flag:
                        tone=0
                        flag=False
                    else:
                        tone=255
                        flag=True
                    self.newImage.putpixel((x,y),(tone,tone,tone))
                else:
                    self.newImage.putpixel((x,y),(r,g,b))
        self.newImage.save("SaltAndPepper.png",self.imag.format)
        #self.newImage.show()
        print 'Done...'




def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    saltIt = SaltAndPepper(Image.open(str(usrImag)))
    saltIt.saltAndPepper()


if __name__=='__main__':
    main()