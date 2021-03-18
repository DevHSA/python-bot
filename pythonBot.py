from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



while 1:

    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA * -1, 10)
    time.sleep(0.1)
    attack = pyautogui.locateOnScreen('attack.png', confidence=0.9)
    cont = pyautogui.locateOnScreen('continue.png', confidence=0.9)
    rebattle = pyautogui.locateOnScreen('rebattle.png', confidence=0.95)

    if attack != None:
        print(attack)
        click(attack[0]+10, attack[1]+10)
        time.sleep(0.1)

    if cont != None:
        print(cont)
        click(cont[0]+10, cont[1]+10)
        time.sleep(0.2)

    if rebattle != None:
        print(rebattle)
        click(rebattle[0]+5, rebattle[1]+5)
        time.sleep(0.2)
