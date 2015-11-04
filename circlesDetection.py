__author__ = 'Josefoo'
import cv2
import numpy as np

class circlesDetection:

	def detectThem(self):
		img = cv2.imread('Images/opencv_logo.png',0)
		img = cv2.medianBlur(img,5)
		cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
		circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:# draw the outer circle
    	 	 cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    		 # draw the center of the circle
    		 cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
		#cv2.imshow('detected circles.png',cimg)
		cv2.imwrite("Images/detected circles.png",cimg)
		cv2.waitKey(0)
		cv2.destroyAllWindows()



def main():

	circles = circlesDetection()
	circles.detectThem()


if __name__ == "__main__":
	main()

	import cv2
import numpy as np

