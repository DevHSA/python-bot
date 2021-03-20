from pyautogui import *
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
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#attack: 

while flag == 0:

    attack = pyautogui.locateOnScreen('attack.png', region=(323,753,670,300), grayscale=True, confidence=0.9)
    cont = pyautogui.locateOnScreen('continue.png', region=(323,753,670,300), grayscale=True, confidence=0.9)
    rebattle = pyautogui.locateOnScreen('rebattle.png', region=(605,405,150,28), grayscale=True, confidence=0.95)
    select = pyautogui.locateOnScreen('select.png', region=(675,327,310,26),grayscale=True, confidence=0.95)

    if attack != None:
        #print(attack)
        #time.sleep(0.01)
        click(attack[0]+10, attack[1]+10)
        

    if cont != None:
        #print(cont)
        #time.sleep(0.01)
        click(cont[0]+10, cont[1]+10)
        

    if rebattle != None:
        print(battles)
        time.sleep(0.2)
        battles = battles + 1
        click(rebattle[0]+5, rebattle[1]+5)
        

    if select !=None:
        #print(select)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA * -3, 10)
        time.sleep(0.1)

    if battles > 130:
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
        

    
    
        
