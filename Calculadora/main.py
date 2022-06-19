import tkinter
from tkinter import *
from tkinter import ttk


# Variáveis
cor1 = "#3b3b3b" #preta
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#eceff1" #cinza
cor5 = "#ff9233" #laranja


# Janela
janela = Tk() 
janela.title("Calculadora")
janela.geometry("284x311")
janela.config(bg=cor1)


# Criando Frames
janela_tela = Frame(janela, width=284, height=55, bg=cor3)
janela_tela.grid(row=0, column=0)

janela_corpo = Frame(janela, width=284, height=261)
janela_corpo.grid(row=1, column=0)

# Variáveis
valor_texto = StringVar()
todos_valores = ''


# Função Exibi na Tela
def entrar_valores(event):
	global todos_valores
	todos_valores = todos_valores + str(event)
	
	# Passanddo o valor na Tela
	valor_texto.set(todos_valores)
	
	
def calcular():
	global todos_valores
	resultado = eval(todos_valores)
	valor_texto.set(str(resultado))
	todos_valores = str(resultado)
	
	
def limpar_tela():
	global todos_valores
	todos_valores = ""
	valor_texto.set("")


# Criando Label
app_label = Label(janela_tela, textvariable=valor_texto, text="123456789", width=16, height=2, padx=35, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 16 bold'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# Ciando Botões
b_1 = Button(janela_corpo, command= limpar_tela,text="C", width=14, height=2, bg=cor5, fg=cor2)
b_1.place(x=0, y=0)
b_2 = Button(janela_corpo, command= lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor5, fg=cor2)
b_2.place(x=144, y=0)
b_3 = Button(janela_corpo, command= lambda: entrar_valores('/'),text="/", width=5, height=2, bg=cor5, fg=cor2)
b_3.place(x=216, y=0)

b_4 = Button(janela_corpo, command= lambda: entrar_valores('7'),text="7", width=5, height=2, bg=cor4)
b_4.place(x=0, y=52)
b_5 = Button(janela_corpo, command= lambda: entrar_valores('8'),text="8", width=5, height=2, bg=cor4)
b_5.place(x=72, y=52) 
b_6 = Button(janela_corpo, command= lambda: entrar_valores('9'),text="9", width=5, height=2, bg=cor4)
b_6.place(x=144, y=52)
b_7 = Button(janela_corpo, command= lambda: entrar_valores('*'),text="x", width=5, height=2, bg=cor5, fg=cor2)
b_7.place(x=216, y=52)

b_8 = Button(janela_corpo, command= lambda: entrar_valores('4'),text="4", width=5, height=2, bg=cor4)
b_8.place(x=0, y=104)
b_9 = Button(janela_corpo, command= lambda: entrar_valores('5'),text="5", width=5, height=2, bg=cor4)
b_9.place(x=72, y=104) 
b_10 = Button(janela_corpo, command= lambda: entrar_valores('6'),text="6", width=5, height=2, bg=cor4)
b_10.place(x=144, y=104)
b_11 = Button(janela_corpo, command= lambda: entrar_valores('-'),text="-", width=5, height=2, bg=cor5, fg=cor2)
b_11.place(x=216, y=104)

b_12 = Button(janela_corpo, command= lambda: entrar_valores('1'),text="1", width=5, height=2, bg=cor4)
b_12.place(x=0, y=156)
b_13 = Button(janela_corpo, command= lambda: entrar_valores('2'),text="2", width=5, height=2, bg=cor4)
b_13.place(x=72, y=156) 
b_14 = Button(janela_corpo, command= lambda: entrar_valores('3'),text="3", width=5, height=2, bg=cor4)
b_14.place(x=144, y=156)
b_14 = Button(janela_corpo, command= lambda: entrar_valores('+'),text="+", width=5, height=2, bg=cor5, fg=cor2)
b_14.place(x=216, y=156)


b_15 = Button(janela_corpo, command= lambda: entrar_valores('0'),text="0", width=14, height=2, bg=cor4)
b_15.place(x=0, y=208) 
b_16 = Button(janela_corpo, command= lambda: entrar_valores('.'),text=".", width=5, height=2, bg=cor4)
b_16.place(x=144, y=208)
b_17 = Button(janela_corpo, command=calcular,text="=", width=5, height=2, bg=cor5, fg=cor2)
b_17.place(x=216, y=208)





janela.mainloop()

















