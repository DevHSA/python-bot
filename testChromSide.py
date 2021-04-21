from pyautogui import *
from random import randint, choice, uniform
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

battles = 1
flag = 0




def click(x,y):
    win32api.SetCursorPos((x,y))
    randNum = uniform(0.1,0.2)
    #pyautogui.moveTo(x, y, randNum, pyautogui.easeInQuad, False, False)
   
    
    #time.sleep(randNum)
    #real_click()
    pyautogui.click()
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # time.sleep(0.08)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#attack: 

x = 9999
y = 9999
w = 0
h = 0

while battles < 1000:
 attack = pyautogui.locateOnScreen('./attackchromeside.png', region=(285,775,258,259), grayscale=True, confidence=0.85)
 cont = pyautogui.locateOnScreen('./continuechromeside.png', region=(285,775,258,259), grayscale=True, confidence=0.85)

 #print(attack,cont,rebattle,select)

 if attack!= None or cont!=None:
     
     if attack != None:
        #print("attack")
        #print(attack)
        if attack[0] < x:
            x = attack[0]
        if attack[1] < y:
            y = attack[1]
        if attack[2] + attack[0] > w:
            w = attack[2] + attack[0]
        if attack[3] + attack[1] > h:
            h = attack[3] + attack[1]
        
        #print(attack)
        #time.sleep(0.01)
        #print(attack)       
        click(attack[0]+randint(2,5), attack[1]+randint(5,10))
        
     if cont != None:
        #print("cont")
        #print(cont)
        if cont[0] < x:
            x = cont[0]
        if cont[1] < y:
            y = cont[1]
        if cont[2] + cont[0]> w:
            w = cont[2] + cont[0]
        if cont[3] + cont[1] > h:
            h = cont[3] + cont[1]
        
        #print(cont)
        #time.sleep(0.01)
        click(cont[0]+10, cont[1]+10)
 else:
    
    rebattle = pyautogui.locateOnScreen('./rebattlechromeside.png', region=(311,405,125,21), grayscale=True, confidence=0.95)
    select = pyautogui.locateOnScreen('./selectchromeside.png', region=(421,326,84,24),grayscale=True, confidence=0.8)

    if rebattle != None:
        #print("rebattle")
        #print(rebattle)
        print(battles)
        #time.sleep(0.1)
        battles = battles + 1
        print(x,y,w,h)
        click(rebattle[0]+5, rebattle[1]+5)
        
        
    if select !=None:
        #print("select")
        #print(select)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA * -3, 10)
        time.sleep(0.1)



        

    
    
        
