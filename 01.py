import cv2 # Import cv2

img = cv2.imread('F:\Images\Aminul_islam.jpg')
img = cv2.resize(img,(700,700))
cv2.imshow('Orginal', img)

cv2.waitKey()
cv2.destroyAllWindows()