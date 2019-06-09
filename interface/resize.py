import cv2
import numpy as np

def Resize(path):
    pic_name = path
    pic = cv2.imread(pic_name)
    height, width = pic.shape[:2]
    size = (250, 250)
    pic = cv2.resize(pic, size, interpolation = cv2.INTER_CUBIC)
    cv2.imwrite(pic_name, pic)

if __name__ == '__main__':
	Resize('enter.jpg')