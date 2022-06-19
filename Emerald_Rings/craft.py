import numpy as np
import numpy
import cv2

from pyautogui import *
import pyautogui
import time
import keyboard
from random import randrange
import win32api, win32con

#updates:   add a feature to catch when materials are out and stop the bot
#           add a feature to 'misclick' on occassion
#           add a feature to 'take breaks'

def randcoords(coords_in):
    coords_out = list(coords_in)
    coords_out[0] = coords_in[0] + randrange(-5,5,1)
    coords_out[1] = coords_in[1] + randrange(-5,5,1)
    return tuple(coords_out)

def craft_rings():
    # click on furnace
    print("looking for furance")
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/furnace2.png', confidence = 0.55)
    if (coords) != None: 
        print("found furnace")
        print(pyautogui.center(coords))
        pyautogui.moveTo(coords)
        time.sleep(0.25)
        pyautogui.click(pyautogui.center(randcoords(coords)))   # Click on the furnace
        time.sleep(10+randrange(10)/10)


    # craft some rings
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/ring.png', confidence = 0.95)
    if (coords) != None: 
        print(pyautogui.center(coords))
        pyautogui.moveTo(coords)
        time.sleep(0.25)
        pyautogui.click(pyautogui.center(randcoords(coords)))   # Click on the ring
        time.sleep(20+randrange(10)/10)

def deposit_rings():
    # find the bank and click on it
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/banks.png', confidence = 0.5)
    if (coords) != None: 
        print(pyautogui.center(coords))
        pyautogui.moveTo(coords)
        time.sleep(0.25)
        pyautogui.click(pyautogui.center(randcoords(coords)))   # Click on the bank
        time.sleep(14+randrange(10)/10)
    if (pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/wrench.png', confidence = 0.5) == None): # check if the bank screen is open
        coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/bank.png', confidence = 0.65)
        if (coords) != None: 
            print(pyautogui.center(coords))
            pyautogui.moveTo(coords)
            time.sleep(0.25)
            pyautogui.click(pyautogui.center(randcoords(coords)))   # Click on the bank
            time.sleep(2+randrange(10)/10)
    print("looking to deposit rings")
    # deposit the rings in my inventory
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/ring_inv.png', region=(1677,744,200,300), confidence = 0.95)
    if (coords) != None: 
        print(pyautogui.center(coords))
        pyautogui.click(pyautogui.center(randcoords(coords)))   # Click on the ring
        time.sleep(1+randrange(10)/10)

def withdraw_gold():
    # withdraw gold bars from bank
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/goldbar.png', confidence = 0.65)
    if (coords) != None: 
        print(pyautogui.center(coords))
        pyautogui.moveTo(coords)
        time.sleep(0.15)
        pyautogui.click(pyautogui.center(randcoords(coords)))   # Click on the bank
        time.sleep(1+randrange(10)/10)

def withdraw_emeralds():
    # withdraw emeralds from bank
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/emerald.png', confidence = 0.65)
    if (coords) != None: 
        #print(pyautogui.center(coords))
        print("withdrawing emeralds")
        pyautogui.moveTo(coords)
        time.sleep(0.25)
        pyautogui.click(pyautogui.center(randcoords(coords)))   # Click on the bank
        time.sleep(1+randrange(10)/10)

def deposit_gold():
    # deposit any gold bars into bank
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/goldbar.png', region=(1677,744,200,300), confidence = 0.95)
    if (coords) != None: 
            #print(pyautogui.center(coords))
            pyautogui.moveTo(coords)
            time.sleep(0.25)
            pyautogui.click(pyautogui.center(randcoords(coords)))   # Click on the goldbars
            time.sleep(1+randrange(10)/10)
            print("Deposited goldbars")

def deposit_emeralds():
    # deposit emeralds into bank
    coords = pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/emerald.png', region=(1677,744,200,300), confidence = 0.95)
    if (coords) != None: 
            #print(pyautogui.center(coords))
            pyautogui.moveTo(coords)
            time.sleep(0.25)
            pyautogui.click(pyautogui.center(randcoords(coords)))   # Click on the emeralds
            time.sleep(1+randrange(10)/10)
            print("Deposited emeralds")

def check_inventory():
    if(pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/emerald.png', region=(1677,744,200,300), confidence = 0.95) != None):
        deposit_emeralds()
        print("depositing emeralds")
    if(pyautogui.locateOnScreen('C:/Users/GregM/Documents/VSCode/Python/Runescape/Emerald_Rings/goldbar.png', region=(1677,744,200,300), confidence = 0.95) != None):
        deposit_gold()
        print("depositing gold")

while(1):
    deposit_rings()
    check_inventory()
    withdraw_gold()
    withdraw_emeralds()
    craft_rings()