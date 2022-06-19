from matplotlib.pyplot import box
import names
from pyautogui import *
import pyautogui
import time
import keyboard
from random import randrange
import win32api, win32con

import cv2
import numpy as np
from PIL import Image

from pytesseract import pytesseract
from pytesseract import Output

from PIL import ImageGrab

pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def setname():
    name = names.get_full_name()

    pyautogui.moveTo(825,475)
    time.sleep(0.5)
    pyautogui.click(825,475)   # Click on Display Name box
    for i in range(0,10):
        pyautogui.press('backspace')
        time.sleep(0.2)
    pyautogui.write(name)
    time.sleep(2+randrange(10)/10)

    pyautogui.moveTo(854,571)
    time.sleep(0.5)
    pyautogui.click(854,571) 

def check_available():
    pyautogui.screenshot('available.png',region=(909,500,70,20))
    img = Image.open('available.png')
    available_data = pytesseract.image_to_string(img)
    if "available" in available_data:
        return True

def click_setname():
    pyautogui.moveTo(854,571)
    time.sleep(0.5)
    pyautogui.click(854,571) 

while(check_available() != True):
    setname()
    time.sleep(3)

click_setname()

