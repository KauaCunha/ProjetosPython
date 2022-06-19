import mysql.connector
import os
from mysql.connector import Error

#VARIÁVEIS DE CONTROLE
opcao = 0


#FUNÇÃO DE TESTE
def testeLoop():
	mainMenu(opcao)


def cadastroCliente():
	idCliente = input("ID do cliente: ")
	nomeCliente = input("Nome do cliete: ")
	teleCliente = input("Telefone do cliente: ")
	estadoCliente = input("Estado do cliente: ")
	
	#(NULL, NOME, TELEFONE, ESTADO)
	dados = '('+idCliente + ',\"' + nomeCliente + '\",' + teleCliente + ',\"' + estadoCliente + '\"' + ')'
	
	declaracao = """INSERT INTO clientes
	(id, Nome, Telefone, Estado)
	VALUES""" 
	
	sql = declaracao + dados
	print("\n"+sql+"\n")
	
	try: 
		#CONEXÃO COM O BANCO DE DADOS
		con = mysql.connector.connect(host='localhost',database='db_minhaLoja',user='root',password='root')
		
		inserir_clientes = sql
		cursor = con.cursor()
		cursor.execute(inserir_clientes)
		con.commit()
		print(cursor.rowcount, "registros inseridos na tabela!")
		cursor.close()
		
	except Error as erro:
		print(f'Falha ao inserir dados no MySQL, apresenta o seguinte erro.\n{erro}')


def excluirClientes():
	deletarNomeCliente = input("Qual o nome do cliente que irá DELETAR do banco de dados? ")
	
	declaracao = """DELETE FROM clientes WHERE Nome="""
	
	sql = declaracao + '\"' + deletarNomeCliente + '\"' + ';'
	print("Código mysql: "+sql)
#seg 01 nov 2021 19:05:14 
	try: 
		#CONEXÃO COM O BANCO DE DADOS
		con = mysql.connector.connect(host='localhost',database='db_minhaLoja',user='root',password='root')
		
		deletar_clientes = sql
		cursor = con.cursor()
		cursor.execute(deletar_clientes)
		con.commit()
		print(cursor.rowcount, "registros deletados na tabela!")
		cursor.close()
		
	except Error as erro:
		print(f'Falha ao deletar dados no MySQL, apresenta o seguinte erro.\n{erro}')
		

def atualizarCliente():
	perguntaColunas = input("(Nome, Telefone, Estado) \nQual coluna quer atualizar?: ")
	
	if(perguntaColunas == "Nome"):
		varNomeAnterior = input("Qual o nome que será definidio? ")
		varNomePosterior = input("Qual o nome atual?")
		
		ajudaWHERE = '\"' + varNomeAnterior + '\"' + " WHERE Nome="
		
		declaracao = """UPDATE clientes SET Nome="""
	
		sql = declaracao + ajudaWHERE +'\"' + varNomePosterior + '\"' + ';'
		print("Código mysql: "+sql)
		
		try: 
			#CONEXÃO COM O BANCO DE DADOS
			con = mysql.connector.connect(host='localhost',database='db_minhaLoja',user='root',password='root')
		
			atualizar_clientes = sql
			cursor = con.cursor()
			cursor.execute(atualizar_clientes)
			con.commit()
			print(cursor.rowcount, "registros atualizados na tabela!")
			cursor.close()
		
		except Error as erro:
			print(f'Falha ao deletar dados no MySQL, apresenta o seguinte erro.\n{erro}')
		
	elif(perguntaColunas == "Telefone"):
		varTelAnterior = input("Qual o novo número? ")
		varTelPosterior = input("Qual número será atualizado? ")
		
		ajudaWHERE = '\"' + varTelAnterior + '\"' + " WHERE Telefone="
		
		declaracao = """UPDATE clientes SET Telefone="""
	
		sql = declaracao + ajudaWHERE +'\"' + varTelPosterior + '\"' + ';'
		print("Código mysql: "+sql)
		
		try: 
			#CONEXÃO COM O BANCO DE DADOS
			con = mysql.connector.connect(host='localhost',database='db_minhaLoja',user='root',password='root')
		
			atualizar_clientes = sql
			cursor = con.cursor()
			cursor.execute(atualizar_clientes)
			con.commit()
			print(cursor.rowcount, "registros atualizados na tabela!")
			cursor.close()
		
		except Error as erro:
			print(f'Falha ao deletar dados no MySQL, apresenta o seguinte erro.\n{erro}')
		
	elif(perguntaColunas == "Estado"):
		varEstadoAnterior = input("Qual o novo Estado? ")
		varEstadoPosterior = input("Qual Estado que será atualizado? ")
		
		ajudaWHERE = '\"' + varEstadoAnterior + '\"' + " WHERE Telefone="
		
		declaracao = """UPDATE clientes SET Telefone="""
	
		sql = declaracao + ajudaWHERE +'\"' + varTelPosterior + '\"' + ';'
		print("Código mysql: "+sql)
		
		try: 
			#CONEXÃO COM O BANCO DE DADOS
			con = mysql.connector.connect(host='localhost',database='db_minhaLoja',user='root',password='root')
		
			atualizar_clientes = sql
			cursor = con.cursor()
			cursor.execute(atualizar_clientes)
			con.commit()
			print(cursor.rowcount, "registros atualizados na tabela!")
			cursor.close()
		
		except Error as erro:
			print(f'Falha ao deletar dados no MySQL, apresenta o seguinte erro.\n{erro}')

















#FUNÇÃO DO MENU DA SELEÇÃO DE FUNÇÃO
def mainMenu(opcao):
	print(
	'\n1 - Cadastrar cliente'
	'\n2 - Excluir cliente'
	'\n3 - Atualizar dados do cliente'
	'\n9 - Sair'
		)
	
	opcao = input('\nOpção: ')
	
	if(opcao == '1'):
		print("\nCadastro de cliente.\n")
		cadastroCliente()
		
	elif(opcao == '2'):
		print("\nExcluir cliente.\n")
		excluirClientes()
		
	elif(opcao == '3'):
		print("\nAtualizar dados do cliente.\n")
		atualizarCliente()

	elif(opcao == '9'):
		print("\nEncerrando o programa...\n")
		quit()

		
	else:
		print("\nDigite uma opção válida.")
		testeLoop()
	
	return opcao
	
while True == True:
	mainMenu(opcao) 
	
	 
