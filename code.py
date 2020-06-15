import sys
import cv2
import imutils

c = 0
def extractImages(pathIn, pathOut,c):
    count = 0
    
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    while success:
        success,image = vidcap.read()
        if count%10==0:
            #image = imutils.rotate_bound(image, 90)
            cv2.imwrite( pathOut + "%06d.jpg" % c, image)
            c = c + 1
        count = count + 1
    return c

s = "your-video.mp4"
pathIn = "/your/folder/input/%s" % s
pathOut = "/your/folder/output/"

c=extractImages(pathIn, pathOut,c)
