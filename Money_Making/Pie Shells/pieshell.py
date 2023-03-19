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
runewindow = gw.getWindowsWithTitle('RuneLite - Gwen Washing')[0]

def randcoords(coords_in): # randomize click locations
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(5,10,1)
    coords_out[1] = coords_in[1] + randrange(5,10,1)
    return tuple(coords_out)  

def bank_coords():
    pyautogui.moveTo(940,528,0.15)
    temp = []
    for x in range(940,970,2):
        pyautogui.moveTo(x,528,0.025)
        if is_bank():
            temp.append(x)
    return(min(temp))

def is_bank():
    pyautogui.screenshot('bank.png', region=(1,25,85,40))
    img = Image.open('bank.png')
    #print(pytesseract.image_to_string(img)[0:2])
    if(pytesseract.image_to_string(img)[0:2] == "Ba" or pytesseract.image_to_string(img)[0:2] == "8a"): return True
    return False

def is_pshell():
    pyautogui.screenshot('pshell.png', region=(1,25,85,40))
    img = Image.open('pshell.png')
    #print(pytesseract.image_to_string(img)[0:2])
    if(pytesseract.image_to_string(img)[0:2] == "De"): return True
    return False

def is_pastry():
    pyautogui.screenshot('pshell.png', region=(30,25,85,40))
    img = Image.open('pshell.png')
    #print(pytesseract.image_to_string(img)[0:2])
    if(pytesseract.image_to_string(img)[0:2] == "Pa"): return True
    return False

def is_piedish():
    pyautogui.screenshot('pshell.png', region=(146,25,85,40))
    img = Image.open('pshell.png')
    print(pytesseract.image_to_string(img)[0:2])
    if(pytesseract.image_to_string(img)[0:2] == "Pi"): return True
    return False

def open_bank(x, y):    # opens the bank screen, looks to deposit chocolate
    print('looking to deposit pie shells')
    coords = x, y
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0], coords[1], randrange(10,15)/100)
    if(is_bank()):
        pyautogui.click()
    else: return Exception
    
def deposit_pieshells():
    coords = pyautogui.locateOnScreen('Money_Making\Pie Shells\pieshell.png', confidence = 0.75)
    print(coords == None)
    if(coords == None):
        raise
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0]+10, coords[1]+10, randrange(5,10)/10)
    if(is_pshell()):
        pyautogui.click()
    else: raise
    time.sleep(1)

def retreive_dough_dish():    # finds dough, finds shells, withdraws both, closes bank
    print('finding dough')
    coords = pyautogui.locateOnScreen('Money_Making\Pie Shells\pastrydough.png', confidence = 0.85)
    if(coords == None):
        raise
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0]+10, coords[1], 0.3)
    time.sleep(randrange(5,15)/10)
    pyautogui.click()
    time.sleep(randrange(5,15)/10)
    print('finding pie dish')
    coords = pyautogui.locateOnScreen('Money_Making\Pie Shells\piedish.png', confidence = 0.85)
    if(coords == None):
        raise
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0]+10, coords[1], 0.3)
    time.sleep(randrange(5,15)/10)
    pyautogui.click()
    time.sleep(randrange(5,15)/10)
    pyautogui.press('esc')

def create_dishes():
    # uses the knife on the chocolate, waits
    knife = (1750, 846)
    chocolate_bar = (1750, 885)
    coords = knife
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0]+5, coords[1]+5, randrange(10,45)/100)
    #if(not is_pastry()):
    #   raise
    pyautogui.click()
    time.sleep(randrange(50,75)/100)

    coords = chocolate_bar
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0]+5, coords[1]+5, randrange(10,25)/100)
    #if(not is_piedish()):
    #    raise
    pyautogui.click()
    time.sleep(randrange(75,125)/100)
    pyautogui.press('space')


    print("making those pie dishes!")
    time.sleep(randrange(18,22))

# Create check: is inventory open
# Create check: is bank set to 14x withdraw
runewindow.activate()
bank_x = bank_coords()
# START:
start_time = time.time()
time_stop = randrange(120,180,1)
print("Going pie shellin for ", time_stop, " minutes!")
while 1:
    if (time.time() - start_time > (time_stop*60)):
        quit()
    try: 
        open_bank(bank_x, 528)
    except:
        print("Could not open bank!")
        time.sleep(30)
        quit()    
    time.sleep(1.5)
    try: 
        deposit_pieshells()
    except:
        print("No pieshells to deposit")
        time.sleep(1)
    try:
        retreive_dough_dish() 
    except:
        print("Could not retreive dough or dishes!")
        time.sleep(30)    
        quit()

    time.sleep(2)
    try:
        create_dishes() # ADD CHECK TO DETERMINE IF THERE'S BOTH PIE DISH AND DOUGH
    except:
        quit()
