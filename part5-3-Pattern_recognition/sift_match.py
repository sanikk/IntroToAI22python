# match SIFT features between two images
# Teemu Roos 6.10.2022

import cv2 
import sys

if len(sys.argv) > 2:
    img1 = cv2.imread(sys.argv[1])
    img2 = cv2.imread(sys.argv[2])
else:
# read two images
    img1 = cv2.imread('img1.jpg')  
    img2 = cv2.imread('img2.jpg') 

# convert to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# create an instance of the SIFT feature extractor
sift = cv2.SIFT_create()

# extract keypoints and descriptors
keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

# match descriptors between the two sets
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(descriptors_1,descriptors_2)

# sort the matches so that the best matches (shortest distance) are first
matches = sorted(matches, key = lambda x:x.distance)

# draw the keypoints and descriptors on top of the two images
img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2,
                       matches[:30], img2, flags=2)

# save the output to a file
cv2.imwrite('sift_keypoints.jpg', img3)
