#!/usr/bin/python
#-*- coding: utf-8 -*-
__author__ = 'José Epifanio'
from PIL import Image
import random
class pseudoRandomColors:

	def __init__(self,number):
		half = number/2
		self.width = half
		self.height = half
		self.newImag = Image.new("RGB",(self.width,self.height))
		self.colorMaker()

	def colorMaker(self):
		temp1=0
		temp2=0
		temp3=0
		for x in range(self.width):
			for y in range(self.height):
				red = random.randrange(0,255)
				blue = random.randrange(0,255)
				green= random.randrange(0,255)
				if red==temp1 or blue==temp2 or green==temp3:
					red = random.randrange(0,255)
					blue = random.randrange(0,255)
					green= random.randrange(0,255)
				elif red>=(temp1-20) or blue>=(temp2-20) or green>=(temp3-20):
					red = random.randrange(0,255)
					blue = random.randrange(0,255)
					green= random.randrange(0,255)
				elif red<=(temp1+20) or blue<=(temp2+20) or green<=(temp3+20):
					red = random.randrange(0,255)
					blue = random.randrange(0,255)
					green= random.randrange(0,255)
				self.newImag.putpixel((x,y),(red,blue,green))
				temp1 = red
				temp2 = blue
				temp3= green
		self.newImag.save("PseudoRandom.png","png")
		self.newImag.show()
		print "Done..."


def main():
	op=raw_input("How many colors do you want")
	try:
		op=int(op)
	except:
		print "ERR not a number"
	pseudo = pseudoRandomColors(op)


if __name__=='__main__':
	main()