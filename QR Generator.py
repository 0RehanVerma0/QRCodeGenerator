import pyqrcode
import png
import cv2

s="www.youtube.com"
url=pyqrcode.create(s)
url.png('Mypng.png',scale = 8)

img=cv2.imread("C:/Users/91981/Desktop/Python Projects/Mypng.png")
detect=cv2.QRCodeDetector()
val,pts,st_code=detect.detectAndDecode(img)
print(val)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
