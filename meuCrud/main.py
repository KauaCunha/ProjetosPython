import mysql.connector
from mysql.connector import Error
import os
import pyfiglet
import editarEstoque
import verEstoque
from tkinter import *

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="db_lojaLoud"
)

if mydb.is_connected():
	print("Conectado ao Banco de dados.")
	#print(mydb)
else:
	print("A conexão com o Banco de Dados não foi realizada.")
	
global RespostaMain
global RespostaEditarEstoque
global RespostaOpcaoEditar

varOpcaoEditar = """

[1] Adicionar
[2] Remover
[3] Atualizar
[9] Voltar
"""

varItens = """

[1] Monitor
[2] CPU
[3] Teclado/Mouse
[9] Voltar
"""


	
def Editar_Estoque():
	os.system("clear") or None
	print(varOpcaoEditar)
	
	RespostaEditarEstoque = input("->")
	
	if(RespostaEditarEstoque == '1'): # ADICIONAR 
		os.system("clear") or None
		#print("\n" * os.get_terminal_size().lines)
		print(varItens)
		RespostaOpcaoEditar = input("->")
		
		if(RespostaOpcaoEditar == '1'): # ADICIONAR MONITOR
			os.system("clear") or None
			print('\nAdicionar Monitor\n')
			editarEstoque.Adicionar_Monitor()
		
		elif(RespostaOpcaoEditar == '2'): # ADICIONAR CPU
			os.system("clear") or None
			print('\nAdicionar CPU\n')
			editarEstoque.Adicionar_CPU()
		
		elif(RespostaOpcaoEditar == '3'): # ADICIONAR TECLADO/MOUSE
			os.system("clear") or None
			print('\nAdicionar Teclado/Mouse\n')
			editarEstoque.Adicionar_TecladoOuMouse()

		elif(RespostaOpcaoEditar == '9'): # VOLTAR
			os.system("clear") or None
			Editar_Estoque()
				
		else:
			print('Insira uma função válida!')
			Editar_Estoque()
				
	elif(RespostaEditarEstoque == '9'):
		editarEstoque.Loop_Main()
		
		
		
def Vender_Iten():
	os.system("clear") or None
	print(varItens)
		
		

def Ler_Tabela():
	os.system("clear") or None
	print(varItens)
	
	respostaLerTabela = input("->")
	
	if(respostaLerTabela == '1'): # MONITOR
		os.system("clear") or None
		verEstoque.Ver_Estoque_Monitor()
		
	elif(respostaLerTabela == '2'):
		os.system("clear") or None
		verEstoque.Ver_Estoque_CPU()
	
	elif(respostaLerTabela == '3'):
		os.system("clear") or None
		verEstoque.Ver_Estoque_Perifericos()
		
	elif(respostaLerTabela == '9'):
		os.system("clear") or None
		verEstoque.Ver_Estoque_Monitor()
			
			

def Main():
	result = pyfiglet.figlet_format("LojaLounge")
	print(result)
	print("""
[1] Editar Estoque
[2] Vender Item
[3] Ver Estoque
[9] Sair

OBS: Informe o NÚMERO de cada função mencionada acima.
	""")
	
	RespostaMain = input("->")

	if(RespostaMain == 1 or RespostaMain == '1'):
		Editar_Estoque()
	elif(RespostaMain == 3 or RespostaMain == '3'):
		Ler_Tabela()
		
		
		
		
		
Main()






























