from turtle import up
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
from PIL import ImageGrab

from pytesseract import pytesseract
from pytesseract import Output

pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#cow_rgb = [(74,54,43), (76,62,56), (56,41,33)]
#cow_hsl = [(13,39,64), (14,64,55), (14,41,33)]
#928 511
low = np.array([10,30,10])
up = np.array([255,50,255])

locations = [(1015, 580), (425,250), (425,580), (1015,250)]

def inventory_count(): # determine how many items are in the inventory
    pyautogui.screenshot('inventory.jpg',region=(1687,746,(1878-1688),(1007-746)))
    img = Image.open('inventory.jpg') # width: 191, height: 261
    inventory_count = 0
    for k in range(0,7,1):                          # vertical 0, 1, 2, 3, 4, 5, 6
        for i in range(0,4,1):                      # horizontal 0, 1, 2, 3
            coordinate = x, y = 30+45*i, 25+35*k    # check each inventory slot
            color = img.getpixel(coordinate)        # pull the pixel color of the inventory location
            #print(color)
            if(color[0] > 60 and color[0] < 64):    # if the b value is between 38 and 42 (typically 40) it is an empty slot
                inventory_count = inventory_count + 1   #count the empty slots
    return (28 - inventory_count)                   # the inventory is 28 full minus the empty slots

def is_cow():  # update this function to check for color and not for text
    pyautogui.screenshot('cowstatus.png',region=(0,21,140,25))
    img = Image.open('cowstatus.png')
    #print(pytesseract.image_to_string(img)[0:2])
    #img.show()
    if(pytesseract.image_to_string(img)[0:2] == "At"): return True
    return False

def cowfind(startx,starty):
    pyautogui.screenshot('cattle_find.jpg', region = (startx,starty,300,300))
    img = Image.open('cattle_find.jpg')
    for k in range(300):
        for j in range(300):
            coordinate = k, j
            color = img.getpixel(coordinate)
            if(color[1] > 30 and color[1] < 50):
                coordinate = k+startx,j+starty
                return(coordinate)
                break


for k in locations:
    coord = cowfind(k[0],k[1])
    pyautogui.moveTo(coord)
    print(is_cow())
    time.sleep(2)