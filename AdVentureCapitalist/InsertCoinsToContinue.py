import numpy as np
import numpy
import cv2

from pyautogui import *
import pyautogui
import time
import keyboard
from random import randrange
import win32api, win32con

import pygetwindow as gw

from PIL import Image
# from PIL import ImageGrab

from pytesseract import pytesseract
from pytesseract import Output


pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#MASH   550,350
#START  970,380
#GOAL   1750,350

upgrade = (238, 141, 72)
y = [975, 830, 670, 525, 385]
x = [1300, 750]

x_g = [870]
y_g = [400, 600, 800, 1000]

count = 0

def goal_click():
    pyautogui.click(1750,350)
    time.sleep(0.35)
    for l in y_g:
        pyautogui.click(870,l)
    pyautogui.click(1675,135)
    return 0

while keyboard.is_pressed('g') == False:
    count = count + 1
    if(count > 25):
        count = goal_click()
    for i in range(1,40):
        pyautogui.click(565,350)
        time.sleep(0.025)
    pyautogui.screenshot('ACbuttons.png')
    img = Image.open('ACbuttons.png')
    pyautogui.click(970,380)
    for k in x:
        for j in y:
            if(img.getpixel((k,j)) == upgrade):
                pyautogui.click(k,j)