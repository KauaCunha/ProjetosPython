import pyautogui 
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 3

#Passo 1: Entrar no link/sistema
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
pyautogui.hotkey("ctrl","t")
pyautogui.write("https://drive.google.com/drive/folders/1skMbKVXsu_vCiiEUmKfLCz_VufA4ViHu")
#pyperclip.copy("https://drive.google.com/drive/folders/1skMbKVXsu_vCiiEUmKfLCz_VufA4ViHu")
#pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(5)

#Passo 2: Navegar até o local do relatório
#pyautogui.click(x=1753, y=280, clicks=2)#entra na pasta TV
pyautogui.click(x=425, y=356, clicks=2)#entra na pasta Notebook
time.sleep(3)

#Passo 3: Fazer o download do relatório
#pyautogui.click(x=1757, y=368)#clica no arquivo TV
pyautogui.click(x=450, y=420)#clica no arquivo Notebook
pyautogui.click(x=3080, y=164)#clica nos 3pts TV
pyautogui.click(x=1162, y=245)#clica nos 3pts Notebook
pyautogui.click(x=2933, y=572)#clica em download TV
pyautogui.click(x=982, y=654)#clica em donwload Notebook
time.sleep(5)

#Passo 4: Calcular os indicadores #pandas
tabela = pd.read_excel(r"/home/kauacunha/Downloads/Vendas - Dez.xlsx")
print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum() 
time.sleep(10)

#Passo 5: Entrar no e-mail
pyautogui.hotkey("ctrl","t")
pyautogui.write("https://mail.google.com/mail/u/0")
pyautogui.press("enter")
time.sleep(5)

#Passo 6: Enviar por e-mail o resultado
pyautogui.click(x=1440, y=190)#clica em escrever
pyautogui.write("ixaba.cla89+diretoria@gmail.com")#escreve o email
pyautogui.press("tab")#seleciona o email
pyautogui.press("tab")#pula pro campo de assunto
#pyperclip.copy("Relatório e vendas)
#pyautogui.hotkey("ctrl","v")#escreve o relatorio
pyautogui.write("Relatory")
pyautogui.press("tab")#pular pro corpo do email
pyautogui.write(f"Valor de faturamento: {faturamento}")
pyautogui.press("enter")
pyautogui.write(f"Quantidade de itend ventidos: {quantidade}")

#TODO: FAZER O EMAIL SER ENVIADO E CONCERTAR O PYPERCLIP









