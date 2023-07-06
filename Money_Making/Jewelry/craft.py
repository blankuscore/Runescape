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

import PySimpleGUI as sg

from PIL import Image

from pytesseract import pytesseract
from pytesseract import Output

pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#updates:   add a feature to catch when materials are out and stop the bot
#           add a feature to 'misclick' on occassion
#           add a feature to 'take breaks'

material = []
jewelry = []

layout = [
    [   
        sg.Button(button_text = "", key = "sapphire_bracelet", tooltip = "Sapphire Bracelet", image_source="Money_Making\Jewelry\images\sapphire_bracelet_100px.png"),
        sg.Button(button_text = "", key = "sapphire_necklace", tooltip = "Sapphire Necklace", image_source="Money_Making\Jewelry\images\sapphire_necklace_100px.png"),
        sg.Button(button_text = "", key = "sapphire_ring", tooltip = "Sapphire Ring", image_source="Money_Making\Jewelry\images\sapphire_ring_100px.png"),
        sg.Button(button_text = "", key = "emerald_bracelet", tooltip = "Emerald Bracelet", image_source="Money_Making\Jewelry\images\emerald_bracelet_100px.png"),
        sg.Button(button_text = "", key = "emerald_necklace", tooltip = "Emerald Necklace", image_source="Money_Making\Jewelry\images\emerald_necklace_100px.png"),
        sg.Button(button_text = "", key = "emerald_ring", tooltip = "Emerald Ring", image_source="Money_Making\Jewelry\images\emerald_ring_100px.png"),
        sg.Button(button_text = "", key = "ruby_bracelet", tooltip = "Ruby Bracelet", image_source="Money_Making/Jewelry/images/ruby_bracelet_100px.png"),
        sg.Button(button_text = "", key = "ruby_necklace", tooltip = "Ruby Necklace", image_source="Money_Making/Jewelry/images/ruby_necklace_100px.png"),
        sg.Button(button_text = "", key = "ruby_ring", tooltip = "Ruby Ring", image_source="Money_Making/Jewelry/images/ruby_ring_100px.png")
    ]
]

window = sg.Window("Jewelry Crafting - Edgeville", layout)

def randcoords(coords_in):
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(10,20,1)
    coords_out[1] = coords_in[1] + randrange(10,20,1)
    return tuple(coords_out)

def craft(material, jewelry):
    print("looking for furance")     # click on furnace
    coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/furnace2.png', confidence = 0.55)
    if (coords) != None: 
        print(pyautogui.center(coords))
        pyautogui.moveTo(coords[0], coords[1], 0.35)

    elif (pyautogui.locateOnScreen('./Money_Making/Jewelry/furnace1.png', confidence = 0.55) != None):
        coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/furnace1.png', confidence = 0.55)
        if (coords == None):
            quit()

    i = 10
    while is_furnace() == False:
        pyautogui.moveTo(coords[0], coords[1]+i, 0.1)
        i = i + 4
        time.sleep(0.05)

    print("found furnace")    
    pyautogui.click(duration=randrange(25,40)/1000)
    time.sleep(12+randrange(10)/10)

    coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/' + material + '_' + jewelry + '_1.png', confidence = 0.95)     # craft jewelry
    if (coords) != None: 
        coords = randcoords(coords)
        pyautogui.moveTo(coords[0], coords[1], 0.35) # click on the jewelry to craft
        pyautogui.click(duration=randrange(25,40)/1000)
        time.sleep(24+randrange(10)/10)
    else:
        coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/' + material + '_' + jewelry + '_2.png', confidence = 0.95)     # craft jewelry
        coords = randcoords(coords)
        pyautogui.moveTo(coords[0], coords[1], 0.35) # click on the jewelry to craft
        pyautogui.click(duration=randrange(25,40)/1000)
        time.sleep(24+randrange(10)/10)

def deposit_jewelry(material, jewelry):    
    coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/banks.png', confidence = 0.5) # find the bank and click on it
    if (coords) != None: 
        print('Found bank 1')
        coords = randcoords(coords)
        pyautogui.moveTo(coords[0]+15, coords[1], 0.35)
        if is_bank() == True:
            pyautogui.click(duration=randrange(25,40)/1000)   # Click on the bank
            time.sleep(14+randrange(10)/10)
        else:
            i = 1
            while is_bank() == False:
                pyautogui.moveTo(coords[0]+(4*i), coords[1]+i, 0.1)
                i = i + 1
                time.sleep(0.05)
                if(int(coords[0]+(4*i)) > 600 or int(coords[1]+i) > 800):
                    print('Missed bank and resetting coordinates now')
                    coords_out = list(coords)
                    coords_out[0] = 404
                    coords_out[1] = 727
                    coords = tuple(coords_out)

        pyautogui.click(duration=randrange(25,40)/1000)   # Click on the bank
        time.sleep(13+randrange(10)/10)

    else:
        coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/bank2.png', region = [300, 600, 550-300, 850-600], confidence = 0.5)
        print('Bank 2')
        coords = randcoords(coords)
        pyautogui.moveTo(coords[0],coords[1],0.35)
        if is_bank() == True:   
                pyautogui.click(duration=randrange(25,40)/1000)   # Click on the bank
                time.sleep(14+randrange(10)/10)
        else:
            i = 1
            while is_bank() == False:
                pyautogui.moveTo(coords[0], coords[1]+i, 0.1)
                i = i + 1
                time.sleep(0.05)
    
    if (pyautogui.locateOnScreen('./Money_Making/Jewelry/wrench.png', confidence = 0.5) == None): # check if the bank screen isn't open
        coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/bank.png', confidence = 0.35)
        if (coords) != None: 
            coords = randcoords(coords)
            pyautogui.moveTo(coords[0], coords[1], 0.15) # click on the bank
            time.sleep(2+randrange(10)/10)
    print("looking to deposit jewelry")
    # deposit the jewelry in my inventory
    coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/' + material + '_' + jewelry + '.png', region=(1685,745,300,400), confidence = 0.75)
    if (coords) != None: 
        coords = randcoords(coords)
        pyautogui.moveTo(coords[0],coords[1], 0.45)
        pyautogui.click(duration=randrange(25,40)/1000)   # Click on the jewelry
        time.sleep(1+randrange(10)/10)

def is_furnace():  # update this function to check for color and not for text
    pyautogui.screenshot('./Money_Making/Jewelry/furnace.png',region=(0,21,140,25))
    img = Image.open('./Money_Making/Jewelry/furnace.png')
    #print(pytesseract.image_to_string(img)[0:2])
    #img.show()
    if(pytesseract.image_to_string(img)[0:2] == "Sm" or pytesseract.image_to_string(img)[0:2] == "sm"): return True
    return False

def is_bank():
    pyautogui.screenshot('./Money_Making/Jewelry/bnk_check.png',region=(0,21,140,25))
    img = Image.open('./Money_Making/Jewelry/bnk_check.png')
    if(pytesseract.image_to_string(img)[0:2] == "Ba" or pytesseract.image_to_string(img)[0:2] == "ba"): return True
    return False

def withdraw_gold():    # withdraw gold bars from bank
    coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/goldbar.png', confidence = 0.65)
    if (coords) != None: 
        coords = randcoords(coords)
        pyautogui.moveTo(coords[0], coords[1], 0.35)
        pyautogui.click(duration=randrange(25,40)/1000)   # Click on the bank
        time.sleep(1+randrange(10)/10)
    else:
        quit()

def deposit_gold():    # deposit any gold bars into bank
    coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/goldbar.png', region=(1677,744,200,300), confidence = 0.95)
    if (coords) != None: 
            #print(pyautogui.center(coords))
            coords = randcoords(coords)
            pyautogui.moveTo(coords[0], coords[1], 0.35)
            pyautogui.click(duration=randrange(25,40)/1000)   # Click on the goldbars
            time.sleep(1+randrange(20)/10)
            print("Deposited goldbars")

def deposit_gems(material):    # deposit raw materials into bank
    coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/' + material + '.png', region=(1677,744,200,300), confidence = 0.95)
    if (coords) != None: 
            coords = randcoords(coords)
            pyautogui.moveTo(coords[0], coords[1], 0.15)
            pyautogui.click(duration=randrange(25,40)/1000)
            time.sleep(1+randrange(10)/10)
            print("Deposited gems")
            
def withdraw_gems(material):    # withdraw rubies from bank
    coords = pyautogui.locateOnScreen('./Money_Making/Jewelry/' + material + '.png', confidence = 0.85)
    if (coords) != None: 
        coords = randcoords(coords)
        pyautogui.moveTo(coords[0], coords[1] ,0.15)
        pyautogui.click(duration=randrange(25,40)/1000)   # Click on the bank
        time.sleep(1+randrange(10)/10)
    else: 
        quit()

def check_inventory(material):
    if(pyautogui.locateOnScreen('./Money_Making/Jewelry/' + material + '.png', region=(1677,744,200,300), confidence = 0.95) != None):
        deposit_gems(material)
        print("depositing gems")
    if(pyautogui.locateOnScreen('./Money_Making/Jewelry/goldbar.png', region=(1677,744,200,300), confidence = 0.95) != None):
        deposit_gold()
        print("depositing gold bars")

click()
"""
while True: # UI to select jewelry and material type
    event, values = window.read()

    if event == "sapphire_bracelet":
        material = "sapphire"
        jewelry = "bracelet"
        window.close()
        break
    if event == "sapphire_necklace":
        material = "sapphire"
        jewelry = "necklace"
        window.close()
        break
    if event == "sapphire_ring":
        material = "sapphire"
        jewelry = "ring"
        window.close()
        break

    if event == "emerald_bracelet":
        material = "emerald"
        jewelry = "bracelet"
        window.close()
        break
    if event == "emerald_necklace":
        material = "emerald"
        jewelry = "necklace"
        window.close()
        break
    if event == "emerald_ring":
        material = "emerald"
        jewelry = "ring"
        window.close()
        break

    if event == "ruby_bracelet":
        material = "ruby"
        jewelry = "bracelet"
        window.close()
        break
    if event == "ruby_necklace":
        material = "ruby"
        jewelry = "necklace"
        window.close()
        break
    if event == "ruby_ring":
        material = "ruby"
        jewelry = "ring"
        window.close()
        break

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

time.sleep(2)
start_time = time.time()
time_stop = randrange(60,100,1)
print("Crafting for a maximum of ", time_stop, " minutes!")
while 1:
    withdraw_gold()
    withdraw_gems(material)
    craft(material, jewelry)
    deposit_jewelry(material, jewelry)
    deposit_gold()
    deposit_gems(material)
    if (time.time() - start_time > (time_stop*60)):
        quit()
        """