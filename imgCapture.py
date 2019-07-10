import pytesseract
from PIL import Image
import cv2
'''
the below commented code! > is used to check which port the camera is to access
'''
# cams_test = 10
# for i in range(0,cams_test):
#     cap = cv2.VideoCapture(i)
#     test,frame = cap.read()
#     print("i :" + str(i)+"//result :" + str(test))


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
imagenames = []


def imgtotext():
    for i in imagenames:
        img = Image.open(i).convert('L')
        img = img.convert('RGBA')

        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        '''
        in above line provide the path of tesseract-ocr exe file path
        '''
        result = pytesseract.image_to_string(img)
        # print(result)
        img.save('three{}.png'.format(i))
        with open('magic_{}.txt'.format(i), mode='w') as file:
            file.write(result)


while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        imgtotext()
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        imagenames.append(img_name)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
print(imagenames)

