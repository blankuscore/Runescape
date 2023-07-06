import numpy as np
import numpy
import cv2

from pyautogui import *
import pyautogui
import time
import keyboard
from random import randrange
import win32api, win32con

#1677 744
#1869 1004

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.5+randrange(10)/10)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while(1):
    coords = pyautogui.locateOnScreen('rslla.png', confidence = 0.85)
    
    if (coords) != None:
        print(pyautogui.center(coords))
        pyautogui.click(pyautogui.center(coords))
        time.sleep(1.5+randrange(10)/10)

    coords2 = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/ra.png', confidence = 0.85)
    if (coords2) != None:
        print(pyautogui.center(coords2))
        pyautogui.click(pyautogui.center(coords2))
        time.sleep(1.5+randrange(10)/10)
    

    time.sleep(2)

    # click(1706+randrange(10),764+randrange(15)) # click on tinderbox
    # time.sleep(0.5+randrange(10)/10)
    # coords = pyautogui.locateOnScreen('wood.png', region=(1677,744,200,300), confidence = 0.85)
    # if (coords) != None:
    #     print(pyautogui.center(coords))
    #     pyautogui.click(pyautogui.center(coords))
    #     time.sleep(1.5+randrange(10)/10)

