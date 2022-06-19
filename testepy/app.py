### ASSUNTO: Variaveis
 
#nome = "david"				#STRING
#Qualquer coisa entre aspas duplas ou simples é considerado uma string

#idade = 15			    	#INT
#Números sem aspas e sem pontos é considerado int

#saldo = 100.00				#FLOAT
#Números fluatuantes/quebrados são considerados float

#O sinal '=' significa atribuição/recebe 

### ASSUNTO: Entradas e saídas de dados

#Para escrever qualquer coisa no terminal ou em uma aplicação,
#usamos uma função já existente na línguagem python o 'print()'.
#Exemplo:

#print('Olá david')
#->Olá david				#No terminal

#Ou também podemos printar na tela uma váriavel que criamos antes.

#print(f'Olá {nome}') 	    #A variável que criamos lá em cima
#->Olá david				#No terminal

#Percebe que nos dois prints saiu os mesmos dados, pois bem, no exemplo 2,
#usamos uma tecnica para adicionarmos valores de variaveis na função print(),
#o f fora das aspas simples e dentro das {chaves} adicionamos o nome da variavel
#que queremos printar, logo printará o valor dela. Já no exemplo 1 escrevemos
#manualmente, logo o exemplo 2 é mais recomendado em alguns casos.

#O print() é uma função de saída de dados, agora vamos ver uma função de entrada

#input('Qual seu nome?: ')	#input() permite interagirmos com o terminal
#->Qual seu nome?:____		#o programa só fechará quando dermos algum dado

#O input() pode ser guardado em uma variável para usarmos mais tarde, por exemplo:
	
#nomeDois = input('Qual seu nome?')

#Percebe que o nome antes era manual, tinhamos que dar o valor no codigo, agora
#com o input() podemos escrever qualquer nome no terminal e ele irá guardar o dado
#que digitamos.
#Exemplo: 

#nomeDois = input('Qual seu nome?: ')
#->Qual seu nome?: kaua

#print(f'Olá {nomeDois}')
#->Olá kaua
