#from types import NoneType
import numpy as np
import numpy
import cv2

from pyautogui import *
import pyautogui
import time
import keyboard
from random import randrange
import win32api, win32con

from PIL import Image
# from PIL import ImageGrab

from pytesseract import pytesseract
from pytesseract import Output

pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

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

#todo:
# fix first item not being dropped
# increase speed of drops
# add randomness in the click locations and timing
# general effeciency improvements

def clear_inventory():
    pyautogui.moveTo(800,9)
    time.sleep(0.25)
    pyautogui.click()
    pyautogui.moveTo(1720,770,0.25)
    pyautogui.mouseUp()
    time.sleep(0.5)
    with pyautogui.hold('shift'):
        for k in range(0,7,1):                          # vertical 0, 1, 2, 3, 4, 5, 6
            for i in range(0,4,1):                      # horizontal 0, 1, 2, 3
                coordinate = x, y = 30+45*i, 25+35*k    # check each inventory slot
                pyautogui.dragTo(1720-30+coordinate[0],770-25+coordinate[1],0.5)
                pyautogui.leftClick()
                time.sleep(0.5)
    pyautogui.keyUp('shift')

def is_tree():
    pyautogui.screenshot('treecheck.png',region=(2,24,240,40))
    img = Image.open('treecheck.png')
    tree_check = pytesseract.image_to_string(img)
    if(tree_check[0:14] != "Chop down Tree"):
            return False
    return True


def randcoords(coords_in):
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(-25,25,1)
    coords_out[1] = coords_in[1] + randrange(-25,25,1)
    return tuple(coords_out)

def move_mouse_left(coords_in):
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] - 50 + randrange(-15,15,1)
    coords_out[1] = coords_in[1] + randrange(-15,15,1)
    return tuple(coords_out)

def move_mouse_right(coords_in):
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + 50 + randrange(-15,15,1)
    coords_out[1] = coords_in[1] + randrange(-15,15,1)
    return tuple(coords_out)

def move_mouse_up(coords_in):
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(-15,15,1)
    coords_out[1] = coords_in[1] - 50 + randrange(-15,15,1)
    return tuple(coords_out)

def move_mouse_down(coords_in):
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(-15,15,1)
    coords_out[1] = coords_in[1] + 50 + randrange(-15,15,1)
    return tuple(coords_out)

def tree_search():
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/start.png', confidence = 0.45)
    pyautogui.moveTo(coords[0],coords[1],0.25) # center of screen: 938 547
    while(1):
        i = randrange(0,4,1)
        if (i == 0):
            coords = move_mouse_left(coords)
        if (i == 1):
            coords = move_mouse_right(coords)
        if (i == 2):
            coords = move_mouse_up(coords)
        if (i == 3):
            coords = move_mouse_down(coords)
        pyautogui.moveTo(coords[0],coords[1],0.10) 
        if(is_tree()): 
            return(coords)

def trunk_search():
    x = 600
    y = 300
    while(not(is_tree())):
        x = x + 50
        y = y = 50
        coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/treetrunk.png', region=(x,y,400,400), confidence = 0.25)
        if(coords != None):
            coords = randcoords(coords)
            pyautogui.moveTo(coords[0],coords[1],0.15)
            print(is_tree())


#print(inventory_count())
#clear_inventory()
print(tree_search())
#trunk_search()