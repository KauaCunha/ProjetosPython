from tkinter import *
from tkcalendar import Calendar, DateEntry

# cores
cor0 = "#038cfc" # azul
cor1 = "#f0f3f5" # preta
cor2 = "#feffff" # branca
cor3 = "#4fa882" # verde
cor4 = "#38576b" # valor
cor5 = "#403d3d" # letra
cor6 = "#e06636" # profit
cor7 = "#ef5350" # vermelha
cor8 = "#263238" # verde
cor9 = "#e9edf5" # ceu


# criando janela
janela = Tk()
janela.title('')
janela.geometry('1043x453')
janela.configure(background=cor9)
janela.resizable(width=False, height=False)


# dividindo janelas
frame_cima = Frame(janela, width=350, height=50, bg=cor3, relief=FLAT)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=350, height=403, bg=cor2, relief=FLAT)
frame_baixo.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)

frame_direita = Frame(janela, width=588, height=403, bg=cor2, relief=FLAT)
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


# label cima
app_nome = Label(frame_cima, text='Formulário', anchor=NW, font=('Ivy 13 bold'), bg=cor3, fg=cor2, relief=FLAT)
app_nome.place(x=10,y=13)


# conf frame baixo
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=cor2, fg=cor3, relief=FLAT)
l_nome.place(x=10,y=10)
e_nome = Entry(frame_baixo, width=40, justify='left', relief=SOLID)
e_nome.place(x=15,y=30)

l_email = Label(frame_baixo, text='E-mail *', anchor=NW, font=('Ivy 10 bold'), bg=cor2, fg=cor3, relief=FLAT)
l_email.place(x=10,y=70)
e_email = Entry(frame_baixo, width=40, justify='left', relief=SOLID)
e_email.place(x=15,y=90)

l_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=cor2, fg=cor3, relief=FLAT)
l_telefone.place(x=10,y=130)
e_telefone = Entry(frame_baixo, width=40, justify='left', relief=SOLID)
e_telefone.place(x=15,y=150)

l_data = Label(frame_baixo, text='Data da Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=cor2, fg=cor3, relief=FLAT)
l_data.place(x=10,y=190)
e_data = DateEntry(frame_baixo, width=10, bg='darkblue', fg='white', bw=2)
e_data.place(x=15,y=210)

l_estado = Label(frame_baixo, text='Estado da Consulta *', anchor=NW, font=('Ivy 10 bold'), bg=cor2, fg=cor3, relief=FLAT)
l_estado.place(x=165,y=190)
e_estado = Entry(frame_baixo, width=21, justify='left', relief=SOLID)
e_estado.place(x=165,y=210)

l_sobre = Label(frame_baixo, text='Informação Extra *', anchor=NW, font=('Ivy 10 bold'), bg=cor2, fg=cor3, relief=FLAT)
l_sobre.place(x=10,y=250)
e_sobre = Entry(frame_baixo, width=40, justify='left', relief=SOLID)
e_sobre.place(x=15,y=270)


# botão inserir
b_inserir = Button(frame_baixo, text='Inserir', width=9, font=('Ivy 9 bold'), bg='green', fg=cor1, relief='raised', overrelief='ridge')
b_inserir.place(x=15,y=320)

# botão atualizar
b_att = Button(frame_baixo, text='Atualizar', width=9, font=('Ivy 9 bold'), bg='blue', fg=cor1, relief='raised', overrelief='ridge')
b_att.place(x=128,y=320)

# botão apagar
b_apagar = Button(frame_baixo, text='Apagar', width=9, font=('Ivy 9 bold'), bg='red', fg=cor1, relief='raised', overrelief='ridge')
b_apagar.place(x=240,y=320)







janela.mainloop()