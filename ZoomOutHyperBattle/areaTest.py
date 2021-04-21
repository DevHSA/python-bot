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
x = 9999
y = 9999
w = 0
h = 0

def click(x,y):
    win32api.SetCursorPos((x,y))
    #pyautogui.moveTo(x,y)
    #randNum = uniform(0.1,0.2)
    #pyautogui.moveTo(x, y, randNum, pyautogui.easeInQuad, False, False)
   
    
    #time.sleep(randNum)
    #real_click()
    pyautogui.click()
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # time.sleep(0.08)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while battles < 2000:

 counter = counter + 1
 attack = pyautogui.locateOnScreen('./attack.png', region=(194,545,366,1009), grayscale=True, confidence=0.85)
 cont = pyautogui.locateOnScreen('./continue.png', region=(194,545,366,1009), grayscale=True, confidence=0.85)

 #print(attack,cont)

 if attack!= None or cont!=None:
     
     if attack != None:
        #print("attack")
        #print(attack)
        #time.sleep(0.01)
        #print(attack)

        if attack[0] < x:
            x = attack[0]
        if attack[1] < y:
            y = attack[1]
        if attack[2] + attack[0] > w:
            w = attack[2] + attack[0]
        if attack[3] + attack[1] > h:
            h = attack[3] + attack[1]
        counter = 0
        click(attack[0]+3, attack[1]+3)
        
     if cont != None:
        #print("cont")
        #print(cont)
        #print(cont)
        #time.sleep(0.01)
        if cont[0] < x:
            x = cont[0]
        if cont[1] < y:
            y = cont[1]
        if cont[2] + cont[0]> w:
            w = cont[2] + cont[0]
        if cont[3] + cont[1] > h:
            h = cont[3] + cont[1] 
        counter = 0
        click(cont[0]+3, cont[1]+3)
 else:
    
    rebattle = pyautogui.locateOnScreen('./rebattle.png', region=(207,300,83,14), grayscale=True, confidence=0.85)
    
    if rebattle != None:
        #print("rebattle")
        #print(rebattle)
        print(battles)
        #time.sleep(0.1)
        battles = battles + 1
        print(x,y,w,h)
        counter = 0
        click(rebattle[0]+5, rebattle[1]+5)


 if counter > 20:
     time.sleep(0.5)
     pyautogui.click()
     time.sleep(0.5)
