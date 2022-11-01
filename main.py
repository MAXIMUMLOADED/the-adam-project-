import time
from tkinter import Image
import uuid
import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from matplotlib import pyplot as plt

def take_photo():
    time.sleep(3)
    cap = cv2.VideoCapture(0)
    text=""
    id = str(uuid.uuid1())
    fileName = 'adam1_'+id+'.jpg'
    try:          
        ret, frame = cap.read()
        #print(ret)
        #print(frame)
        #plt.imshow(frame)
        cv2.imwrite(fileName,frame)  
        #img = Image.open(frame)
        text = tess.image_to_string(fileName)
        #print(text) 
    finally:
        cap.release() 
        cv2.destroyAllWindows()
        time.sleep(3)
        return text
        


# print('process started')
take_photo()
# print('process completed!')    
     