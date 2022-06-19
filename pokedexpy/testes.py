import os
import tkinter as tk
from tkinter import *
import mysql.connector
from mysql.connector import Error


def adicionarPokemon():
    # criando janela
    janela = Tk()
    janela.title('Adicionar Pokémon')
    janela.geometry('300x300')
    janela.configure(background='gray')
    janela.resizable(width=False, height=False)

def janelaMain():

    # criando janela
    janela = Tk()
    janela.title('POKEDEX')
    #janela.geometry('300x300')
    janela.configure(background='gray')
    janela.resizable(width=False, height=False)

    botao_adicionar_pokemon = tk.Button(text='Adicionar Pokémon', command=adicionarPokemon)
    botao_adicionar_pokemon.grid(row=0, column=2,  sticky='nswe', columnspan=4)

    botao_remover_pokemon = tk.Button(text='Remover Pokémon', command=adicionarPokemon)
    botao_remover_pokemon.grid(row=1, column=2, padx=10, pady=10, sticky='nswe', columnspan=4)

    botao_atualizar_pokemon = tk.Button(text='Atualizar Pokémon', command=adicionarPokemon)
    botao_atualizar_pokemon.grid(row=2, column=2, padx=10, pady=10, sticky='nswe', columnspan=4)

    botao_ver_pokedex = tk.Button(text='Ver Pokédex', command=adicionarPokemon)
    botao_ver_pokedex.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=4)

    
    janela.mainloop()

janelaMain()