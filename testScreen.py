import pyautogui


img = pyautogui.screenshot(region=(285,775,258,259))
img.save(r"D:\GIT\python-bot\testimage.png")

img = pyautogui.locateOnScreen('chrome.png')
 
print(img)
