from pyautogui import *
from random import randint, choice, uniform
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

battles = 1
counter = 0
refreshCounter = 0
battleFlag = 0
clickMutex = 0

def click(x,y):
    win32api.SetCursorPos((x,y))
    #pyautogui.moveTo(x,y)
    #randNum = uniform(0.1,0.2)
    #pyautogui.moveTo(x, y, randNum, pyautogui.easeInQuad, False, False)
   
    
    #time.sleep(randNum)
    #real_click()
    #pyautogui.click()
    #clickMutex = 1
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #time.sleep(0.08)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #clickMutex = 0

while battles < 3000:

 counter = counter + 1
 refreshCounter = refreshCounter + 1
 attack = pyautogui.locateOnScreen('./attack.png', region=(194,545,366,1009), grayscale=True, confidence=0.85)
 cont = pyautogui.locateOnScreen('./continue.png', region=(194,545,366,1009), grayscale=True, confidence=0.85)

 #print(attack,cont)

 if attack!= None or cont!=None :
     
     if attack != None:
        #print("attack")
        #print(attack)
        #time.sleep(0.01)
        #print(attack)
        counter = 0
        refreshCounter = 0
        battleFlag = 0
        click(attack[0]+randint(15,20), attack[1]+randint(14,17))
        #win32api.SetCursorPos((attack[0]+20,attack[1]+17))
        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        #time.sleep(0.08)
        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        
     if cont != None:
        #print("cont")
        #print(cont)
        #print(cont)
        #time.sleep(0.01)
        counter = 0
        refreshCounter = 0
        battleFlag = 0
        click(cont[0]+10, cont[1]+14)
 else:
    
    rebattle = pyautogui.locateOnScreen('./rebattle.png', region=(207,300,83,14), grayscale=True, confidence=0.95)
    
    if rebattle != None:
        #print("rebattle")
        #print(rebattle)
        #time.sleep(0.1)
        if battleFlag == 0:
            battles = battles + 1
            print(battles)
            battleFlag = 1
        counter = 0
        refreshCounter = 0
        click(rebattle[0]+5, rebattle[1]+5)


 if counter > 6:
     print("counter", counter)
     time.sleep(0.5)
     pyautogui.click()
     time.sleep(0.5)
     counter = 0
 if refreshCounter > 30:
     print("refresh", refreshCounter)
     time.sleep(0.5)
     pyautogui.press('f5')
     time.sleep(5)
     refreshCounter = 0
