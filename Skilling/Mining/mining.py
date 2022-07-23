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

inv_x = [1720, 1760, 1800, 1840]
inv_y = [770, 805, 840, 875, 910, 945, 980]
inv = [ (1720,770), (1760,770), (1800,770), (1840,770),
        (1720,805), (1760,805), (1800,805), (1840,805),
        (1720,840), (1760,840), (1800,840), (1840,840),
        (1720,875), (1760,875), (1800,875), (1840,875),
        (1720,910), (1760,910), (1800,910), (1840,910),
        (1720,945), (1760,945), (1800,945), (1840,945),
        (1720,980), (1760,980), (1800,980), (1840,980), (1840,980)]
runewindow = gw.getWindowsWithTitle('RuneLite')[0]

def randcoords(coords_in): # randomize click locations
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(-5,5,1)
    coords_out[1] = coords_in[1] + randrange(-5,5,1)
    return tuple(coords_out)  

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

def clear_inv(start,end): # clear a set of inventory items
    runewindow.activate()
    if(end > 28): return Exception
    with pyautogui.hold('shift'):
        for i in range(start-1,end+1):
            coords = inv[i]
            rcoords = randcoords(coords); time.sleep(0.05)
            time.sleep(0.05); pyautogui.moveTo(rcoords[0], rcoords[1], 0.125)
            time.sleep(0.05); pyautogui.click(rcoords[0], rcoords[1]) 

def is_mining():  # update this function to check for color and not for text
    pyautogui.screenshot('miningstatus.png',region=(30,45,80,20))
    img = Image.open('miningstatus.png')
    #print(pytesseract.image_to_string(img)[0:2])
    #img.show()
    if(pytesseract.image_to_string(img)[0:2] == "NO" or pytesseract.image_to_string(img)[0:2] == "" or pytesseract.image_to_string(img)[1] == "0" or pytesseract.image_to_string(img)[0:2] == "HO" or pytesseract.image_to_string(img)[0:2] == "No"): return False
    return True


start_time = time.time()
time_stop = randrange(105,135,1)
print("Going minin for ", time_stop, " minutes!")
runewindow.activate()
while(1):
    if (inventory_count() > 26):
        clear_inv(1,inventory_count())
    if (time.time() - start_time > (time_stop*60)):
        quit()
    while(is_mining()):
        time.sleep(0.5)
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/Mining/iron1.png', confidence = 0.75)
    if coords != None: 
        pyautogui.moveTo(coords[0]+randrange(100,140),coords[1]+randrange(30,60), 0.15)
        pyautogui.click()
    else:
        coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/Mining/iron1.1.png', confidence = 0.75)
        if coords != None: 
            pyautogui.moveTo(coords[0]+randrange(40,60),coords[1]+randrange(15,30), 0.15)
            pyautogui.click()
    time.sleep(2)
    if (inventory_count() > 26):
        clear_inv(1,inventory_count())
    while(is_mining()):
        time.sleep(0.5)
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/Mining/iron2.png', confidence = 0.9)
    if coords != None: 
        pyautogui.moveTo(coords[0]+randrange(40,60),coords[1]+randrange(15,30), 0.15)
        pyautogui.click()
    time.sleep(2)
    if (inventory_count() > 26):
        clear_inv(1,inventory_count())
    while(is_mining()):
        time.sleep(0.5)
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/Mining/iron3.png', confidence = 0.75)
    if coords != None: 
        pyautogui.moveTo(coords[0]+randrange(40,60),coords[1]+randrange(15,30), 0.15)
        pyautogui.click()
    #else:
    #    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/Mining/iron3.1.png', confidence = 0.75)
    #    if coords != None: 
    #        pyautogui.moveTo(coords[0]+randrange(40,60),coords[1]+randrange(15,30), 0.15)
    #        pyautogui.click()
    time.sleep(2)

    