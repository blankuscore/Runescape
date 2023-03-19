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

knife = (1700, 730)
chocolate_dust = (1740, 730)

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

def is_cdust():
    pyautogui.screenshot('cdust.png', region=(1,25,85,40))
    img = Image.open('cdust.png')
    #print(pytesseract.image_to_string(img)[0:2])
    if(pytesseract.image_to_string(img)[0:2] == "De"): return True
    return False

def is_cbar():
    pyautogui.screenshot('cdust.png', region=(1,25,85,40))
    img = Image.open('cdust.png')
    #print(pytesseract.image_to_string(img)[0:2])
    if(pytesseract.image_to_string(img)[0:2] == "Wi" or pytesseract.image_to_string(img)[0:2] == "it" or pytesseract.image_to_string(img)[0:2] == "Vi" or pytesseract.image_to_string(img)[0:2] == "Ui"): return True
    return False

def open_bank(x, y):
    # opens the bank screen, looks to deposit chocolate
    print('looking to deposit chocolate dust')
    coords = x, y
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0], coords[1], randrange(10,15)/100)
    if(is_bank()):
        pyautogui.click()
    else: return Exception
    
def deposit_chocolate():
    coords = pyautogui.locateOnScreen('Money_Making\GE\Chocolate\chocolate_dust.png', confidence = 0.75)
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0]+10, coords[1]+10, randrange(5,10)/10)
    if(is_cdust()):
        pyautogui.click()
    else: return Exception
    time.sleep(1)

def retreive_chocolate():
    # finds chocolate, checks chocolate exists, withdraws chocolate, closes bank
    print('finding chocolate')
    coords = pyautogui.locateOnScreen('Money_Making\GE\Chocolate\chocolate_bar.png', confidence = 0.7)
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0]+10, coords[1], 0.3)
    time.sleep(randrange(10,20)/10)
    if(is_cbar()):
        pyautogui.click()
    else: return Exception
    """
    close = (1050, 50)
    coords = randcoords(close)
    pyautogui.moveTo(coords[0], coords[1], 0.65)
    time.sleep(randrange(10,20)/10)
    pyautogui.mouseDown()
    time.sleep(randrange(1,3)/60)
    pyautogui.mouseUp()
    """
    time.sleep(randrange(10,20)/10)
    pyautogui.press('esc')

def cut_chocolate():
    # uses the knife on the chocolate, waits
    knife = (1700, 730)
    chocolate_bar = (1740, 730)
    coords = knife
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0]+10, coords[1]+10, randrange(10,45)/100)
    pyautogui.mouseDown()
    time.sleep(randrange(1,3)/60)
    pyautogui.mouseUp()
    time.sleep(randrange(50,75)/100)

    coords = chocolate_bar
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0]+10, coords[1]+10, randrange(10,45)/100)
    pyautogui.mouseDown()
    time.sleep(randrange(1,3)/60)
    pyautogui.mouseUp()

    print("Cutting that chocolate! (est. 45s)")
    time.sleep(randrange(45,52))

bank_x = bank_coords()
# START:
try: 
    open_bank(bank_x, 528)
except:
    print("Could not open bank!")
    time.sleep(30)
    quit()    
time.sleep(1.5)
try:
    retreive_chocolate()
except:
    print("Could not retreive chocolate!")
    time.sleep(30)    
    quit()

time.sleep(randrange(1,7)/10)
cut_chocolate()
start_time = time.time()
time_stop = randrange(120,180,1)
print("Going minin for ", time_stop, " minutes!")
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
        deposit_chocolate()
    except:
        print("Could not deposit chocolate!")
        time.sleep(30)    
        quit()
    time.sleep(1.5)
    try:
        retreive_chocolate()
    except:
        print("Could not retreive chocolate!")
        time.sleep(30)    
        quit()

    time.sleep(2)
    cut_chocolate()