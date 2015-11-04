#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'José Epifanio'
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image
class RGBManipulator():
     def __init__(self, image):
        self.imag = image
        self.heigth = image.size[0]
        self.width = image.size[1]
        self.newImag = Image.new(self.imag.mode, self.imag.size)

     def changeRGB(self, tag, value):
        for x in range(self.heigth):
            for y in range(self.width):
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
        self.newImag.save("test"+tag+".png",self.imag.format)
        self.newImag.show()
        print("Done...")



def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    manipulator = RGBManipulator(Image.open(str(usrImag)))
    op=0
    while(op!=5):
        print("1.Red")
        print("2.Green")
        print("3.Blue")
        print("4.All of them")
        print("5.Exit")
        op=int(raw_input("¿Which one would you like to modify?"))
        if(op==1):
            print("Red")
            value=[]
            val=int(raw_input("Give the value for the 'red' channel: "))
            while(val<0 or val>255):
                val=int(raw_input("Give the value for the 'red' channel: "))
            value.append(int(val))
            manipulator.changeRGB("red",value)
        elif(op==2):
            print("Green")
            value=[]
            val=int(raw_input("Give the value for the 'green' channel: "))
            while(val<0 or val>255):
                val=int(raw_input("Give the value for the 'green' channel: "))
            value.append(int(val))
            manipulator.changeRGB("green",value)
        elif(op==3):
            print("Blue")
            value=[]
            val=int(raw_input("Give the value for the 'blue' channel: "))
            while(val<0 or val>255):
                val=int(raw_input("Give the value for the 'blue' channel: "))
            value.append(int(val))
            manipulator.changeRGB("blue",value)
        elif(op==4):
            print("all of them")
            value = []
            valR=int(raw_input("Give me the red channel value: "))
            valG=int(raw_input("Give me the green channel value: "))
            valB=int(raw_input("Give me the blue channel value: "))
            if(valR<0 or valR>255):
                print("1 Done")
                while(valR<0 or valR>255):
                    valR=int(raw_input("Give me another red channel value : "))

            elif(valG<0 or valR>255):
                print("2 Done")
                while(valG<0 or valG>255):
                    valG=int(raw_input("Give me another green channel value : "))

            elif(valB<0 or valB>255):
                print("3 Done")
                while(valB<0 or valB>255):
                    valB=int(raw_input("Give me another blue channel value : "))

            value.append(valR)
            value.append(valG)
            value.append(valB)
            manipulator.changeRGB("all",value)
        else:
            print("Good-Bye")




if __name__=='__main__':
    main()