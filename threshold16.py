#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'José Epifanio'
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image
class threshold16:

    def __init__(self,image):
        self.imag=image
        self.width=image.size[0]
        self.height=image.size[1]
        self.newImag = Image.new(self.imag.mode,self.imag.size)

    def threshold(self):
        ran = 255/16 # saltos de 16
        for x in range(self.width):
            for y in range(self.height):
                gray = self.imag.getpixel((x,y)) # esta tomando los tres
                gray = gray[0]
                #print "gris ",gray
                if gray>=0 and gray <= ran:
                    if (ran/2)>gray:
                        gray=0
                    else:
                        gray=ran
                elif gray > ran and gray <= (ran*2):
                    if ((ran*2)/2)>=gray:
                        gray= (ran*2)
                    else:
                        gray= (ran*3)
                elif gray > (ran*2) and gray<= (ran*3):
                    if ((ran*3)/2)>=gray:
                        gray= (ran*3)
                    else:
                        gray= (ran*4)
                elif gray > (ran*3) and gray<= (ran*4):
                    if ((ran*4)/2)>=gray:
                        gray= (ran*4)
                    else:
                        gray= (ran*5)
                elif gray > (ran*4) and gray<= (ran*5):
                    if ((ran*5)/2)>=gray:
                        gray= (ran*5)
                    else:
                        gray= (ran*6)
                elif gray > (ran*5) and gray<= (ran*6):
                    if ((ran*6)/2)>=gray:
                        gray= (ran*6)
                    else:
                        gray= (ran*7)
                elif gray > (ran*6) and gray<= (ran*7):
                    if ((ran*7)/2)>=gray:
                        gray= (ran*7)
                    else:
                        gray= (ran*8)
                elif gray > (ran*7) and gray<= (ran*8):
                    if ((ran*8)/2)>=gray:
                        gray= (ran*8)
                    else:
                        gray= (ran*9)
                elif gray > (ran*8) and gray<= (ran*9):
                    if ((ran*9)/2)>=gray:
                        gray= (ran*9)
                    else:
                        gray= (ran*10)
                elif gray > (ran*9) and gray<= (ran*10):
                    if ((ran*10)/2)>=gray:
                        gray= (ran*10)
                    else:
                        gray= (ran*11)
                elif gray > (ran*10) and gray<= (ran*11):
                    if ((ran*11)/2)>=gray:
                        gray= (ran*11)
                    else:
                        gray= (ran*12)
                elif gray > (ran*11) and gray<= (ran*12):
                    if ((ran*12)/2)>=gray:
                        gray= (ran*12)
                    else:
                        gray= (ran*13)
                elif gray > (ran*12) and gray<= (ran*13):
                    if ((ran*13)/2)>=gray:
                        gray= (ran*13)
                    else:
                        gray= (ran*14)
                elif gray > (ran*13) and gray<= (ran*14):
                    if ((ran*14)/2)>=gray:
                        gray= (ran*14)
                    else:
                        gray= (ran*15)
                elif gray > (ran*14) and gray<= (ran*15):
                    if ((ran*15)/2)>=gray:
                        gray= (ran*15)
                    else:
                        gray= (ran*16)
                elif gray > (ran*15) and gray<= (ran*16):
                    if ((ran*16)/2)>=gray:
                        gray= (ran*16)
                    else:
                        gray= (ran*17)
                else:
                    gray = 255 # revisar esta ultima condicion bien
                self.newImag.putpixel((x,y),(gray,gray,gray))
        self.newImag.save("Threshold16Tones.png",self.imag.format)
#        self.newImag.show()
        print "Done.."




def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    thres = threshold16(Image.open(str(usrImag)))
    thres.threshold()


if __name__=='__main__':
    main()
