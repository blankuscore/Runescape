import pyautogui
import pygetwindow as gw
import time

corewindow = gw.getWindowsWithTitle('Core Keeper')[0]

for k in range(250a):
    corewindow.activate()
    pyautogui.mouseDown(button='right')
    time.sleep(0.15)
    pyautogui.mouseUp(button='right')
    with pyautogui.hold('d'):
        time.sleep(30)
    with pyautogui.hold('a'):
        time.sleep(30)
    