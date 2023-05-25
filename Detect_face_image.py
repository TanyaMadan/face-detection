import cv2

#import the cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#taking the image
image = cv2.imread('multiface.jpg')

#convert the image into grayscale image

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#detect the faces from the complete image
faces = face_cascade.detectMultiScale(gray_image,1.2,4)

#put rectangle around the faces
# x,y coordinates and w is weight and h is height
for(x,y,w,h) in faces:
     #input,point1,point2,color=green,thickness=3
    cv2.rectangle(image, (x, y), (x+w ,y+h), (0,128,0), 3)

#display the image
cv2.imshow('image',image)

cv2.waitKey()