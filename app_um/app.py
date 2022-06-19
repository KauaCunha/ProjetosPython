import os
import urllib.request
from twilio.rest import Client

opcao = 0

def testeLoop():
	mainMenu(opcao)
	
def enviarSMS(suaMensagem, numDestino):
	from twilio.rest import Client 
 
	account_sid = 'AC89df70cecd72dc1606f307b6829855d4' 
	auth_token = '7b0d1af6ea415bf37d2ecac449af1d00' 
	client = Client(account_sid, auth_token) 
	 
	message = client.messages.create(  
      #messaging_service_sid='MG5b4487a0b3063e4ec11dde025d35d9a4', 
      body=suaMensagem,
      from_='+12182755900',
      to=numDestino 
	) 
	#print(message.sid)
	print('\nMensagem enviada com sucesso!\n')
	mainMenu(opcao)

def getCEP(varCep):
	cep = varCep
	url = 'https://viacep.com.br/ws/%s/json/' % cep
	headers = {'User-Agent': 'Autociencia/1.0'}
	requisicao = urllib.request.Request(url, headers=headers, method='GET')
	cliente = urllib.request.urlopen(requisicao)
	conteudo = cliente.read().decode('utf-8')
	cliente.close()
	print(conteudo)
	mainMenu(opcao)

def mainMenu(opcao):
	print(
	'\n###############################################\n'
	'\n1 - Solicitar CEP'
	'\n2 - Enviar SMS'
	'\n3 - Enviar E-mail'
	'\n9 - Sair'
		)
	
	opcao = int(input('\nOpção: '))
	
	if(opcao == 1):
		#PARA DEBUG
		#print("Escolhi a opção 1")
		#print(opcao)
		#testeLoop()
	
		varCep = int(input('Insira seu CEP: '))
		getCEP(varCep)
	
	elif(opcao == 2):
		print("\nEscolhi a opção 2\n")
		
		suaMensagem = str(input('Mensagem: '))
		numDestino = input('Para o número: ')
		enviarSMS(suaMensagem, numDestino)
		
	elif(opcao == 3):
		print("\nEscolhi a opção 3\n")
		print(opcao)
		testeLoop()
		
	elif(opcao == 9):
		print("\nEncerrando o programa...\n")
		#sys.exit()
		quit()
		
	else:
		print("\nDigite uma opção válida.")
		#print(opcao)
		mainMenu(opcao)
	
	return opcao
	
mainMenu(opcao)














