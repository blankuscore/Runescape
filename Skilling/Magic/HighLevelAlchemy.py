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

runewindow = gw.getWindowsWithTitle('Old School RuneScape')[0]

def randcoords(coords_in): # randomize click locations
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(-6,6,1)
    coords_out[1] = coords_in[1] + randrange(-6,6,1)
    return tuple(coords_out) 

def HA_spell():
    coords = pyautogui.locateOnScreen('Skilling\Magic\HA_Spell.png', confidence = 0.95)
    if (coords) != None: 
        coords = randcoords(pyautogui.center(coords))
        pyautogui.moveTo(coords[0], coords[1], 0.15)
        time.sleep(1+randrange(5,20)/10)
        pyautogui.click()   #click on high alch spell
    else:
        pyautogui.press("F6")
        time.sleep(randrange(5,10)/10)
        coords = pyautogui.locateOnScreen('Skilling\Magic\HA_Spell.png', confidence = 0.95)
        if (coords) != None: 
            coords = randcoords(pyautogui.center(coords))
            pyautogui.moveTo(coords[0], coords[1], 0.15)
            time.sleep(1+randrange(5,20)/10)
            pyautogui.click()   #click on high alch spell

def HA_item():
    coords = pyautogui.locateOnScreen('Skilling\Magic\HA_Item.png', confidence = 0.5)
    if coords != None:
        coords = randcoords(pyautogui.center(coords))
        pyautogui.moveTo(coords[0], coords[1], 0.15)
        time.sleep(randrange(5)/10)
        pyautogui.click()   #click on high alch spell
    else: return Exception

runewindow.activate()
count = 0
while 1:
    HA_spell()
    try: 
        HA_item()
        time.sleep(1+randrange(10,15)/10)
    except:
        quit()

    count = count + 1
    print("{} items submitted to High Alchemy".format(count))