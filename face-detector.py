import cv2 #python computer vision library
import sys
from google.colab.patches import cv2_imshow #Colab patch for the incompatible cv2 photo rendering function

#filepaths from colab filesystem (not OS)
imagePath = "/content/filename.png"
cascPath = "/content/haarcascade_frontal_default.xml"

#Creating necessary classifier, image, and color objects.
faceCascade = cv2.CascadeClassifier(cascPath)
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,#gray converts image to grayscale
    scaleFactor=1.1,                        #scaleFactor scales all faces to the same size
    minNeighbors=14,                        #minNeighbor is minimum amount of patterns (classifiers) that the ai needs to find to call something a face. 
                                            #decreasing it will allow it to pick up more but it will be less accurate
    minSize=(19,19),                        #minSize is the minimum size a face has to be
    flags = cv2.CASCADE_SCALE_IMAGE)#flags scales the image

for (x,y,w,h) in faces:                     # the for loop draws a green square around each face found in the image
  cv2.rectangle(image, (x,y),(x+w, y+h), (0, 255, 0),2)

cv2_imshow(image)                          #this shows the image (this is the Colab patch for im.show() from cv2)
cv2.waitKey(0)                             #waits a second before the program terminates

print("found {0} faces!".format(len(faces)))  #print how many faces
