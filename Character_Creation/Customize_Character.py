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

def click_design(y):
    pyautogui.moveTo(730,y)
    time.sleep(1+randrange(10)/10)
    pyautogui.click(730,y)   

def click_colour(y):
    pyautogui.moveTo(1040,y)
    time.sleep(1+randrange(10)/10)
    pyautogui.click(1040,y) 

def click_confirm():
    pyautogui.moveTo(850,580)
    time.sleep(1+randrange(10)/10)
    pyautogui.click(850,580) 

design = np.array([380,408,440,480,510,550,590])
colour = np.array([380,408,440,480,510])

for i in design:
    j = randrange(6)
    for k in range(j):
        click_design(i)

for i in colour:
    j = randrange(6)
    for k in range(j):
        click_colour(i)

click_confirm()