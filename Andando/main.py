import time
import pyautogui 

while True:
    for i in range(0, 17):
        print('Baixo',i)
        pyautogui.click(x=730, y=614, clicks=3)
        time.sleep(2)
        if i == 16:
            pyautogui.press('down')
            for ii in range(0, 19):
                print('Esquerda',ii)
                pyautogui.click(x=636, y=559, clicks=3)
                time.sleep(2)
    i = 0
    pyautogui.press('down')
