import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="db_lojaLoud"
)


	
def Adicionar_Monitor():
	varMarca = input('Nome da Marca: ')
	varPolegada = input('Informe as Polegadas: ')
	varPreco = input('Informe o valor do Produto: ')
	
	mycursor = mydb.cursor()
	
	declaracao = """INSERT INTO Monitores
	(Marca, Polegadas, Preco)
	VALUES""" 
	
	dados = '(\"'+varMarca + '\",\"' + varPolegada + '\",\"' + varPreco + '\"' + ')' + ';'
	
	sqlval = declaracao + dados
	mycursor.execute(sqlval)
	mydb.commit()
	
	print(mycursor.rowcount, "produto inserido.")



def Adicionar_CPU():
	print('Função adiconar CPU')
	varProcessador = input('Processador: ')
	varVideo = input('Placa Gráfica: ')
	varRAM = input('Quantidade de RAM: ')
	varSSD = input('Quantidade de SSD: ')
	varHD = input('Espaço no HD: ')
	varFonte = input('Fonte: ')
	varPreco = input('Preço: ')
	
	mycursor = mydb.cursor()
	
	declaracao = """INSERT INTO CPU
	(Processador, Video, RAM, HD, SSD, Fonte, Preco)
	VALUES""" 
	
	dados = '(\"'+varProcessador+'\",\"'+varVideo+'\",\"'+varRAM+'\",\"'+varHD+'\",\"'+varSSD+'\",\"'+varFonte+'\",\"'+varPreco+'\"'+')'+';'
	
	sqlval = declaracao + dados
	mycursor.execute(sqlval)
	mydb.commit()
	
	print(mycursor.rowcount, "produto inserido.")
	
	
def Adicionar_TecladoOuMouse():
	print('Função adiconar TecladoOuMouse')
	varTipo = input('Teclado ou Mouse?: ')
	varMarca = input('Marca: ')
	varRGB = input('Possui RGB?: ')
	varDPI = input('Quantidade de DPI: ')
	varPreco = input('Preco: ')
	
	mycursor = mydb.cursor()
	
	declaracao = """INSERT INTO Perifericos
	(Tipo, Marca, RGB, DPI, Preco)
	VALUES""" 
	
	dados = '(\"'+varTipo+'\",\"'+varMarca+'\",\"'+varRGB+'\",\"'+varDPI+'\",\"'+varPreco+'\"'+')'+';'
	
	sqlval = declaracao + dados
	mycursor.execute(sqlval)
	mydb.commit()
	
	print(mycursor.rowcount, "produto inserido.")
	
	
	
	
	
	
	
	
	
	
	
