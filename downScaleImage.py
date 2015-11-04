__author__ = 'Josefoo'
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
from PIL import Image
import os

class downScaleImage():

	def downScale(self,image,size):
		im = Image.open(image)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save("thumbnailTest.png", "PNG")
		im.show()
		print "Done..."


def main():
    Tk().withdraw()
    tkMessageBox.showinfo( "Image", "Select an Image")
    usrImag = askopenfilename()
    size =128,128
    downSc = downScaleImage()
    downSc.downScale(usrImag,size)


if __name__=="__main__":
	main()