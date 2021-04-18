from pyautogui import *
from random import randint, choice, uniform
import pyautogui
import time
import random


time.sleep(2)

battles = 1

def click(x,y):
    pyautogui.moveTo(x, y)
    #randNum = uniform(0.1,0.2)
    #pyautogui.moveTo(x, y, randNum, pyautogui.easeInQuad, False, False)
    #time.sleep(randNum)
    #real_click()
    pyautogui.click()

#attack: 

while battles < 1000:

    attack = pyautogui.locateOnScreen('attack.png',region=(237,540,244,134), grayscale=True, confidence=0.7)
    cont = pyautogui.locateOnScreen('continue.png',region=(237,540,244,134), grayscale=True, confidence=0.7)
    rebattle = pyautogui.locateOnScreen('rebattle.png', region=(305,323,80,14), grayscale=True)
    select = pyautogui.locateOnScreen('select.png', region=(346,270,181,14), grayscale=True)

    if rebattle != None:
        print(battles)
       	#time.sleep(0.1)
        battles = battles + 1
        click(rebattle[0]+5, rebattle[1]+5)

    if cont != None:
        click(cont[0]+5, cont[1]+5)

    if attack != None:
        click(attack[0]+5, attack[1]+5)

    if select != None:
       	pyautogui.scroll(-10)
	#time.sleep(0.1)






