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

pyautogui.MINIMUM_DURATION = 0.01

def real_click():
    '''This function clicks the mouse with realistic errors:
        occasional accidental right click
        occasional double click
        occasional no click
    '''
    if randint(1, 19) != 1:
        sleep(93 / randint(83,201))
        pyautogui.click()
    else:
        tmp_rand = randint(1, 3)
        if tmp_rand == 1:
            #double click
            pyautogui.click()
            sleep(randint(43, 113) / 1000)
            pyautogui.click()
        elif tmp_rand == 2:
            pyautogui.click(button = 'right')


def click(x,y):
    #win32api.SetCursorPos((x,y))
    randNum = uniform(0.1,0.2)
    pyautogui.moveTo(x, y, randNum, pyautogui.easeInQuad, False, False)
    #time.sleep(randNum)
    #real_click()
    pyautogui.click()
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # time.sleep(0.08)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#attack: 

while battles < 35:

    attack = pyautogui.locateOnScreen('./attack.png', region=(323,703,670,300), grayscale=True, confidence=0.85)
    cont = pyautogui.locateOnScreen('./continue.png', region=(323,753,670,300), grayscale=True, confidence=0.85)
    rebattle = pyautogui.locateOnScreen('./rebattle.png', region=(605,405,150,28), grayscale=True, confidence=0.9)
    select = pyautogui.locateOnScreen('./select.png', region=(675,327,310,26),grayscale=True, confidence=0.9)

    if attack != None:
        #print(attack)
        #time.sleep(0.01)
        print(attack)       
        click(attack[0]+uniform(2,5), attack[1]+uniform(5,10))
        

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

    if battles > 50:
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

    #if select == None and rebattle == None and cont == None and attack == None and battles <= 100:
        #print(select)
        #sleep(5)
        #win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, win32con.WHEEL_DELTA * -3, 10)
        #time.sleep(0.1)
        

    
    
        
