import pyautogui 
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 3


#Passo 1: Entrar no link/sistema
while True:
    for i in range(0,32):
        pyautogui.click(x=492, y=728)
        time.sleep(1)
        if i == 30:
            for ii in range(0,32):
                pyautogui.click(x=371, y=610)
                time.sleep(1)


