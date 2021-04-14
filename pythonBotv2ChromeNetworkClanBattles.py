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

losscount = 0

while battles < 1000:

    attack = pyautogui.locateOnScreen('./attackchromeside.png', region=(195,560,680,530), grayscale=True, confidence=0.85)
    cont = pyautogui.locateOnScreen('./continuechromeside.png', region=(195,560,680,530), grayscale=True, confidence=0.85)
    rebattle = pyautogui.locateOnScreen('./backtoclanchromeside.png', region=(200,200,300,300), grayscale=True, confidence=0.95)
    select = pyautogui.locateOnScreen('./selectchromeside.png', region=(250,250,400,100),grayscale=True, confidence=0.8)
    start = pyautogui.locateOnScreen('./startbattle.png', region=(710,526,107,27),grayscale=True, confidence=0.8)
    
    #print(attack,cont,rebattle,select)

    if attack != None:
        #print(attack)
        #time.sleep(0.01)
        #print(attack)       
        click(attack[0]+randint(2,5), attack[1]+randint(5,10))
        
    if cont != None:
        #print(cont)
        #time.sleep(0.01)
        click(cont[0]+10, cont[1]+10)
        
    if rebattle != None:
        print(battles)
        #time.sleep(0.1)
        battles = battles + 1
        click(rebattle[0]+10, rebattle[1]+10)
        time.sleep(6)

    if start != None:
        print(start)
        #time.sleep(0.1)
        battles = battles + 1
        click(start[0]+10, start[1]+10)
        time.sleep(6)
        
    if select !=None:
        #print(select)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA * -3, 10)
        time.sleep(0.1)

    if battles > 5550:
        time.sleep(5)
        flag = 1
        logout = pyautogui.locateOnScreen('logout.png', confidence=0.95)
        time.sleep(2)
        click(logout[0]+5, logout[1]+5)
        time.sleep(6)
        browserclose = pyautogui.locateOnScreen('browserclose.png', confidence=0.95)
        time.sleep(2)
        click(browserclose[0]+5, browserclose[1]+5)
        time.sleep(6)

        

    
    
        
