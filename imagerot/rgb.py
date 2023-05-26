import cv2
import numpy as np

# Load an image from file
img = cv2.imread('images.jpg')

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale', gray)
cv2.waitKey(0)

# Apply a Gaussian blur to the image
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Display the blurred image
cv2.imshow('Blurred', blur)
cv2.waitKey(0)

# Apply edge detection to the image
edges = cv2.Canny(img, 100, 200)

# Display the edges image
cv2.imshow('Edges', edges)
cv2.waitKey(0)

# Apply a threshold to the image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display the thresholded image
cv2.imshow('Threshold', thresh)
cv2.waitKey(0)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

# Display the image with contours
cv2.imshow('Contours', img)
cv2.waitKey(0)

# Resize the image
resized = cv2.resize(img, (500, 500))

# Display the resized image
cv2.imshow('Resized', resized)
cv2.waitKey(0)

# Rotate the image
(rows, cols) = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))

# Display the rotated image
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)

# Flip the image horizontally
flipped = cv2.flip(img, 1)

# Display the flipped image
cv2.imshow('Flipped', flipped)
cv2.waitKey(0)