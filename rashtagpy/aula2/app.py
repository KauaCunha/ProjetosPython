#Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

#Passo 2: Visualizar a base de dados
#	- Entender quais as informações estão disponíveis
#	- Descobrir as cagadas da base de dados
tabela = tabela.drop("Unnamed: 0", axis=1) #0 =coluna #1 = linha
print(tabela)

#Passo 3: Tratamento de dados
#	- Valores que estão sendo reconhecido de forma errada
tabela["TotalGasto"]
#	- Valores vazios
print(tabela.info())

#Passo 4: Análise Inicial

#Passo 5: Análise Mais completa
