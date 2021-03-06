import cv2
img = cv2.imread('doc_shadow.png',0)
ret,thresh1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imwrite("normalThresh.jpg",thresh1)
cv2.imwrite("Mblock11c2.jpg",th2)
cv2.imwrite("Gblock11c2.jpg",th3)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)
cv2.imwrite("Mblock5c2.jpg",th2)
cv2.imwrite("Gblock5c2.jpg",th3)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,20)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,20)
cv2.imwrite("Mblock11c20.jpg",th2)
cv2.imwrite("Gblock11c20.jpg",th3)