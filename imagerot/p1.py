import cv2

# Load the image file
image = cv2.imread('img2.jpg')

# Get the dimensions of the image
height, width = image.shape[:2]

# Split the image into 4 quadrants
quadrant1 = image[0:height//2, 0:width//2]
quadrant2 = image[0:height//2, width//2:width]
quadrant3 = image[height//2:height, 0:width//2]
quadrant4 = image[height//2:height, width//2:width]

# Display the quadrants
cv2.imshow('Quadrant 1', quadrant1)
cv2.imshow('Quadrant 2', quadrant2)
cv2.imshow('Quadrant 3', quadrant3)
cv2.imshow('Quadrant 4', quadrant4)
cv2.waitKey(0)
cv2.destroyAllWindows()


