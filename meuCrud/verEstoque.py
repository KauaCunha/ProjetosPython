import mysql.connector
from mysql.connector import Error
import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="db_lojaLoud"
)


def Ver_Estoque_Monitor():
	try:
			mycursor = mydb.cursor()
			declaracao = """SELECT * FROM Monitores""" 
			mycursor.execute(declaracao)
			linhas = mycursor.fetchall()
			print(mycursor.rowcount, "Número total de registros retornados.")
			
			print("\nMostrando a tabela Monitores\n")
			for linha in linhas:
				#print("ProdutoId:",linha[0],"| Marca:",linha[1],"| Polegadas:",linha[2],"| Preço:",linha[3],"\n")
				print("ProdutoId:",linha[0])
				print("Marca:", linha[1])
				print("Polegadas:", linha[2])
				print("Preço:", linha[3],"\n")
				#print("ProdutoId |","Marca |","Polegada |","Preço")
				#print(linha[0],"         ",linha[1], "  " ,linha[2] ,"       " ,linha[3],"\n")
	except Error as e:
		print("Erro ao acessar tabela mysql", e)
	finally:
		if(mydb.is_connected()):
			mydb.close()
			mycursor.close()
			print("Conexão ao MySQL encerrada")

def Ver_Estoque_CPU():
	try:
			mycursor = mydb.cursor()
			declaracao = """SELECT * FROM CPU""" 
			mycursor.execute(declaracao)
			linhas = mycursor.fetchall()
			print(mycursor.rowcount, "Número total de registros retornados.")
			
			print("\nMostrando a tabela CPU\n")
			for linha in linhas:
				#print("ProdutoId:",linha[0],"| Marca:",linha[1],"| Polegadas:",linha[2],"| Preço:",linha[3],"\n")
				print("ProdutoId:",linha[0])
				print("Processador:", linha[1])
				print("Vídeo:", linha[2])
				print("RAM:", linha[3])
				print("HD:",linha[4])
				print("SSD:", linha[5])
				print("Fonte:", linha[6])
				print("Preço:", linha[7],"\n")
				#print("ProdutoId |","Marca |","Polegada |","Preço")
				#print(linha[0],"         ",linha[1], "  " ,linha[2] ,"       " ,linha[3],"\n")
	except Error as e:
		print("Erro ao acessar tabela mysql", e)
	finally:
		if(mydb.is_connected()):
			mydb.close()
			mycursor.close()
			print("Conexão ao MySQL encerrada")
			
def Ver_Estoque_Perifericos():
	try:
			mycursor = mydb.cursor()
			declaracao = """SELECT * FROM Perifericos""" 
			mycursor.execute(declaracao)
			linhas = mycursor.fetchall()
			print(mycursor.rowcount, "Número total de registros retornados.")
			
			print("\nMostrando a tabela Monitores\n")
			for linha in linhas:
				#print("ProdutoId:",linha[0],"| Marca:",linha[1],"| Polegadas:",linha[2],"| Preço:",linha[3],"\n")
				print("ProdutoId:",linha[0])
				print("Tipo:", linha[1])
				print("Marca:", linha[2])
				print("RGB:", linha[3])
				print("DPI:", linha[4])
				print("Preço:", linha[5],"\n")
				#print("ProdutoId |","Marca |","Polegada |","Preço")
				#print(linha[0],"         ",linha[1], "  " ,linha[2] ,"       " ,linha[3],"\n")
	except Error as e:
		print("Erro ao acessar tabela mysql", e)
	finally:
		if(mydb.is_connected()):
			mydb.close()
			mycursor.close()
			print("Conexão ao MySQL encerrada")
