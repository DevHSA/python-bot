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
 attack = pyautogui.locateOnScreen('./attackchromeside.png', region=(285,775,265,259), grayscale=True, confidence=0.85)
 cont = pyautogui.locateOnScreen('./continuechromeside.png', region=(285,775,265,259), grayscale=True, confidence=0.85)

 #print(attack,cont,rebattle,select)

 if attack!= None or cont!=None:
     
     if attack != None:
        #print("attack")
        #print(attack)
        #time.sleep(0.01)
        #print(attack)
        counter = 0
        click(attack[0]+randint(2,5), attack[1]+randint(5,10))
        
     if cont != None:
        #print("cont")
        #print(cont)
        #print(cont)
        #time.sleep(0.01)
        counter = 0
        click(cont[0]+10, cont[1]+10)
 else:
    
    rebattle = pyautogui.locateOnScreen('./rebattlechromeside.png', region=(311,405,125,21), grayscale=True, confidence=0.85)
    select = pyautogui.locateOnScreen('./selectchromeside.png', region=(421,326,84,24),grayscale=True, confidence=0.8)

    if rebattle != None:
        #print("rebattle")
        #print(rebattle)
        print(battles)
        #time.sleep(0.1)
        battles = battles + 1
        #print(x,y,w,h)
        counter = 0
        click(rebattle[0]+5, rebattle[1]+5)
        
        
    if select !=None:
        #print("select")
        #print(select)
        counter = 0
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA * -3, 10)
        time.sleep(0.1)


 if counter > 20:
     time.sleep(0.5)
     pyautogui.click()
     time.sleep(0.5)
#    if rebattle == None and select == None and attack==None and cont==None:

        #print("Entered")
 #       rebattleside = pyautogui.locateOnScreen('./rebattleselected.png', region=(310,395,140,35), grayscale=True, confidence=0.95)

  #      if(rebattleside!=None):   
   #      time.sleep(0.5)
    #     pyautogui.click()  
         #time.sleep(0.5)
         #pyautogui.moveTo(rebattleside[0]+5,rebattleside[0]+3)
         #time.sleep(0.5)
         #pyautogui.click() 
        

    
    
        
