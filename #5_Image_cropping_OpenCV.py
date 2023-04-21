#import packages
import cv2
import numpy as np

img = cv2.imread('image.jpg')
print(img.shape) # Print image shape
cv2.imshow("Original:", img)
 
# Cropping an image it works like this: img[height, width]
cropped_image = img[100:400, 50:330]
 
# Display cropped image
cv2.imshow("Cropped", cropped_image)
print(cropped_image.shape)
 
# Save the cropped image
cv2.imwrite("test_cropped.jpg", cropped_image)
 
cv2.waitKey(0)
cv2.destroyAllWindows()


