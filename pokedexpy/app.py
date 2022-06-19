from cgitb import text
import os
import datetime as dt
import tkinter as tk
from tkinter import *
from turtle import width
import mysql.connector
from mysql.connector import Error

	

def cadastro_Pokemon():
	pass


def janela_Adicionar_Pokemon():
	janelaAdiconar = tk.Toplevel()
	janelaAdiconar.title('Cadastro de pokemon') 
	janelaAdiconar.geometry("500x300")
	janelaAdiconar.resizable(width=False, height=False)
	

	lb_adicionar_nome = tk.Label(janelaAdiconar, text='Nome:')
	lb_adicionar_nome.grid(row=0, column=0, 
	padx=10, pady=10, sticky='nswe')

	en_adicionar_nome = tk.Entry(janelaAdiconar)
	en_adicionar_nome.grid(row=0, column=1,
	padx=10, pady=10, sticky='nswe')

	lb_adicionar_id = tk.Label(janelaAdiconar, text='ID:')
	lb_adicionar_id.grid(row=0, column=2, 
	padx=10, pady=10, sticky='nswe')

	en_adicionar_id = tk.Entry(janelaAdiconar, width=5)
	en_adicionar_id.grid(row=0, column=3,
	padx=10, pady=10,
	sticky='nswe')

	lb_fraquezas = tk.Label(janelaAdiconar, text='Fraquezas:')
	lb_fraquezas.grid(row=1, column=0, 
	padx=10, pady=10, sticky='nswe')

	cb_adicionar_fraqueza_fogo = tk.Checkbutton(janelaAdiconar, text='Fogo', bg='red')
	cb_adicionar_fraqueza_fogo.place(x=0, y=80)

	cb_adicionar_fraqueza_agua = tk.Checkbutton(janelaAdiconar, text='Água', bg='blue')
	cb_adicionar_fraqueza_agua.place(x=70, y=80)

	cb_adicionar_fraqueza_grama = tk.Checkbutton(janelaAdiconar, text='Grama', bg='green')
	cb_adicionar_fraqueza_grama.place(x=130, y=80)

 

	janelaAdiconar.mainloop()


#FUNÇÃO DO MENU DA SELEÇÃO DE FUNÇÃO


# criando janela
janelaMain = tk.Tk()
janelaMain.title('POKEDEX')
#janela.geometry('300x300')
janelaMain.configure(background='gray')
janelaMain.resizable(width=False, height=False)

botao_adicionar_pokemon = tk.Button(janelaMain, text='Adicionar Pokémon',
command=janela_Adicionar_Pokemon)
botao_adicionar_pokemon.grid(row=0, column=2,
padx=10, pady=10, sticky='nswe', columnspan=4)

botao_remover_pokemon = tk.Button(janelaMain, text='Remover Pokémon',
command=janela_Adicionar_Pokemon)
botao_remover_pokemon.grid(row=1,column=2,
padx=10, pady=10,sticky='nswe', columnspan=4)

botao_atualizar_pokemon = tk.Button(janelaMain, text='Atualizar Pokémon',
command=janela_Adicionar_Pokemon)
botao_atualizar_pokemon.grid(row=2, column=2,
padx=10, pady=10, sticky='nswe', columnspan=4)

botao_ver_pokedex = tk.Button(janelaMain, text='Ver Pokédex',
command=janela_Adicionar_Pokemon)
botao_ver_pokedex.grid(row=3, column=2,
padx=10, pady=10, sticky='nswe', columnspan=4)


janelaMain.mainloop()