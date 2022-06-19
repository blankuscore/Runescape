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

def take_break():
    t = randrange(0,100,1)
    print("Taking a break for ", 300 * t / 100) 
    time.sleep(round(300 * t / 100)) # take a break for up to 5 minutes (300s)
   
def remove_inv(location): # removes a specific inventory item in a specific location
    runewindow.activate()
    if(location < 5): x = inv_x[location - 1]; y = inv_y[0]
    if(4 < location < 9): x = inv_x[location - 5]; y = inv_y[1]
    if(8 < location < 13): x = inv_x[location - 9]; y = inv_y[2]
    if(12 < location < 17): x = inv_x[location - 13]; y = inv_y[3]
    if(16 < location < 21): x = inv_x[location - 17]; y = inv_y[4]
    if(20 < location < 25): x = inv_x[location - 21]; y = inv_y[5]
    if(24 < location < 29): x = inv_x[location - 25]; y = inv_y[6]
    if(28 < location): return None
    coords = (x,y)
    rcoords = randcoords(coords); time.sleep(0.05)
    with pyautogui.hold('shift'):
        time.sleep(0.05); pyautogui.moveTo(rcoords[0], rcoords[1], 0.15)
        time.sleep(0.05); pyautogui.click(rcoords[0], rcoords[1])    
    
def randcoords(coords_in): # randomize click locations
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(-5,5,1)
    coords_out[1] = coords_in[1] + randrange(-5,5,1)
    return tuple(coords_out)  

def inv_open():
    runewindow.activate()
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Runescape/Skilling/inventory.png') #check if inventory is open or not
    if (coords != None): 
        time.sleep(0.05); pyautogui.moveTo(coords[0], coords[1], 0.15)
        pyautogui.click()

def clear_inv(start,end): # clear a set of inventory items
    runewindow.activate()
    inv_open()
    if(end > 28): return Exception
    with pyautogui.hold('shift'):
        for i in range(start-1,end+1):
            coords = inv[i]
            rcoords = randcoords(coords); time.sleep(0.05)
            time.sleep(0.05); pyautogui.moveTo(rcoords[0], rcoords[1], 0.125)
            time.sleep(0.05); pyautogui.click(rcoords[0], rcoords[1])  

def findshrimp():
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/shrimp.png', confidence = 0.85)
    if(coords != None): return coords
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/shrimp2.png', confidence = 0.85)
    if(coords != None): return coords
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/shrimp2.png', confidence = 0.45)
    if(coords != None): return coords

def use_net():
    runewindow.activate()
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/Fishnet.png',confidence = 0.95)
    pyautogui.moveTo(coords[0],coords[1],0.15)
    time.sleep(0.25)
    pyautogui.click()

def is_fishing():
    pyautogui.screenshot('fishingstatus.png',region=(30,45,80,25))
    img = Image.open('fishingstatus.png')
    if(pytesseract.image_to_string(img)[0:2] == "NO" or pytesseract.image_to_string(img)[0:2] == ""): return False
    return True

while(1):
    if (inventory_count() > 24):
        clear_inv(2,24)
    if (is_fishing() == False):
        coords = findshrimp()
        pyautogui.moveTo(coords[0]+20,coords[1]+20, 0.15)
        pyautogui.click()
        time.sleep(8)  
