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
inv = [ (1720,750), (1760,750), (1800,750), (1840,750),
        (1720,790), (1760,790), (1800,790), (1840,790),
        (1720,820), (1760,820), (1800,820), (1840,820),
        (1720,860), (1760,860), (1800,860), (1840,860),
        (1720,900), (1760,900), (1800,900), (1840,900),
        (1720,940), (1760,940), (1800,940), (1840,940),
        (1720,970), (1760,970), (1800,970), (1840,970), (1840,970)]
runewindow = gw.getWindowsWithTitle('RuneLite')[0]

def randcoords(coords_in): # randomize click locations
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(-5,5,1)
    coords_out[1] = coords_in[1] + randrange(-5,5,1)
    return tuple(coords_out)  

def inventory_count(): # determine how many items are in the inventory
    pyautogui.screenshot('inventory.jpg',region=(1686,729,(1878-1688),(986-746)))
    img = Image.open('inventory.jpg') # width: 191, height: 261
    inventory_count = 0
    for k in range(0,7,1):                          # vertical 0, 1, 2, 3, 4, 5, 6
        for i in range(0,4,1):                      # horizontal 0, 1, 2, 3
            coordinate = 30+45*i, 25+35*k    # check each inventory slot
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
    if(pytesseract.image_to_string(img)[0:2] == "NO" or pytesseract.image_to_string(img)[0:2] == "" or pytesseract.image_to_string(img)[1] == "0" or pytesseract.image_to_string(img)[0:2] == "HO" or pytesseract.image_to_string(img)[0:2] == "No"): return False
    return True

def is_rock():
    pyautogui.screenshot('rock.png', region=(1,25,85,40))
    img = Image.open('rock.png')
    print(pytesseract.image_to_string(img)[0:2])
    if(pytesseract.image_to_string(img)[0:2] == "Mi" or pytesseract.image_to_string(img)[0:2] == "Hi"): return True
    return False

def is_cd(x_min, x_max, y_min, y_max):
    pyautogui.screenshot('cd.png', region=(x_min, y_min, x_max-x_min, y_max-y_min))
    img = Image.open('cd.png')
    #img.show()
    coordinate = round((x_max - x_min)/2), round((y_max - y_min)/2)
    color_array = []
    for x in range(1, coordinate[0],1):
        for y in range(1, coordinate[1],1):
            coord = x, y
            color = img.getpixel(coord)
            color_array.append(color[0])
    return(sum(color_array))

def find_rocks():
    # 945 528 = player location
    pyautogui.moveTo(845,528,0.15)

    # ROCK LEFT
    temp = []
    for x in range(845,945,5):
        pyautogui.moveTo(x,528,0.05)
        if is_rock():
            temp.append(x)
    rock_left = [min(temp), max(temp)]
    temp = []

    for y in range(500,550,5):
        pyautogui.moveTo((rock_left[0] + ((rock_left[1] - rock_left[0])/2)),y,0.05)
        if is_rock():
            temp.append(y)
    
    rock_left.append(min(temp))
    rock_left.append(max(temp))
    # Rock left = min_x, max_x, min_y, max_y

    # ROCK RIGHT
    """
    temp = []
    for x in range(945,1045,5):
        pyautogui.moveTo(x,528,0.05)
        if is_rock():
            temp.append(x)
    if(temp != []):
        rock_right = [min(temp), max(temp)]
        temp = []
        for y in range(500,550,5):
            pyautogui.moveTo((rock_right[0] + ((rock_right[1] - rock_right[0])/2)),y,0.05)
        if is_rock():
            temp.append(y)
        rock_right.append(min(temp))
        rock_right.append(max(temp))
        # Rock right = min_x, max_x, min_y, max_y
    """

    # ROCK TOP
    temp = []
    for y in range(428,528,5):
        pyautogui.moveTo(945,y,0.05)
        if is_rock():
            temp.append(y)
    rock_top = []
    rock_top_temp = [min(temp), max(temp)]
    temp = []

    for x in range(900,1000,5):
        pyautogui.moveTo(x,(rock_top_temp[0] + ((rock_top_temp[1] - rock_top_temp[0])/2)),0.05)
        if is_rock():
            temp.append(x)
    
    rock_top.append(min(temp))
    rock_top.append(max(temp))
    rock_top.append(rock_top_temp[0])
    rock_top.append(rock_top_temp[1])
    # Rock top = min_x, max_x, min_y, max_y
    
    return(rock_left, rock_top)

def mine(x, y):
    coords = x, y
    coords = randcoords(coords)
    pyautogui.moveTo(coords[0], coords[1], 0.15)
    pyautogui.mouseDown()
    time.sleep(randrange(1,3)/60)
    pyautogui.mouseUp()
    

start_time = time.time()
time_stop = randrange(105,135,1)
print("Going minin for ", time_stop, " minutes!")
runewindow.activate()
rock_left, rock_top = find_rocks() # min_x, max_x, min_y, max_y
rock_left_center = (rock_left[1] - rock_left[0]) / 2 + rock_left[0], (rock_left[3] - rock_left[2]) / 2 + rock_left[2]
rock_top_center = (rock_top[1] - rock_top[0]) / 2 + rock_top[0], (rock_top[3] - rock_top[2]) / 2 + rock_top[2]
cd_left = is_cd(rock_left[0], rock_left[1], rock_left[2], rock_left[3])
cd_top = is_cd(rock_top[0], rock_top[1], rock_top[2], rock_top[3])
while(1):
    #[930, 965, 478, 513]
    #print(rock_top)
    #print(is_cd(rock_top[0], rock_top[1], rock_top[2], rock_top[3]))
    #print(cd_top)
    if(is_cd(rock_top[0], rock_top[1], rock_top[2], rock_top[3]) < cd_top * 1.20):
        mine(rock_top_center[0], rock_top_center[1])
        time.sleep(3)
    if(is_cd(rock_left[0], rock_left[1], rock_left[2], rock_left[3]) < cd_left * 1.05):
        mine(rock_left_center[0], rock_left_center[1])
        time.sleep(3)
    print(inventory_count())
    if (inventory_count()+1 > 26):
        clear_inv(1,inventory_count())
    if (time.time() - start_time > (time_stop*60)):
        quit()
    time.sleep(1)
    """
    while(is_mining()):
        time.sleep(0.5)
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/Mining/iron1.png', confidence = 0.75)
    if coords != None: 
        pyautogui.moveTo(coords[0]+randrange(100,140),coords[1]+randrange(30,60), 0.15)
        pyautogui.click()
    else:
        coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Skilling/Mining/iron1.png', confidence = 0.75)
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
    """
    