import pyautogui
import time
time.sleep(0.5)
pyautogui.hotkey('win', 'q')
time.sleep(0.5)

if pyautogui.locateOnScreen('.\\arena\\chinese.png') is not None: #切英文
    pyautogui.hotkey('shift')

time.sleep(0.5)    

pyautogui.typewrite('nox')
pyautogui.hotkey('enter')

i = 0
while i < 60: 
    if pyautogui.locateOnScreen('.\\arena\\big.png') is not None:  #放大
        pyautogui.click(pyautogui.locateCenterOnScreen(".\\arena\\big.png"))
        break
    time.sleep(1)
    i += 1
time.sleep(1)

i = 0
while i < 60: 
    if pyautogui.locateOnScreen('.\\arena\\icon.png') is not None: #點遊戲
        pyautogui.click(pyautogui.locateCenterOnScreen(".\\arena\\icon.png"))
        break
    time.sleep(1)
    i += 1
time.sleep(5)

while i < 60:
    check = pyautogui.locateOnScreen('.\\arena\\x.png') or pyautogui.locateOnScreen('.\\arena\\x2.png') or pyautogui.locateOnScreen('.\\arena\\x3.png')
    if check is not None: 
        for i in range(2):
            pyautogui.hotkey('c')
            time.sleep(1)
        break
        i += 1
time.sleep(1)

pyautogui.click(x=1133, y=900, duration=1) #模式選擇
pyautogui.click(x=1133, y=900, duration=1) #模式選擇
pyautogui.click(x=152, y=778, duration=1) #娛樂模式
pyautogui.click(x=1329, y=915, duration=1) #開始遊戲
pyautogui.click(x=1659, y=652, duration=1.5) #排位賽
pyautogui.click(x=1547, y=948, duration=1) #開始配對

i = 0
while i<99:
    pyautogui.click(x=939, y=900, duration=1) #開始配對
    check = pyautogui.locateOnScreen('.\\arena\\stop.png') or pyautogui.locateOnScreen('.\\arena\\stop2.png') or pyautogui.locateOnScreen('.\\arena\\stop3.png') 
    if check is not None:
        break
    time.sleep(10)
    i += 1