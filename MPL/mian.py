from tkinter import Y
import pandas as pd
arquivo = pd.read_csv('/home/kauacunha/projetospy/MPL/wine_dataset.csv')

arquivo['style'] = arquivo['style'].replace('red',0)
arquivo['style'] = arquivo['style'].replace('white',1)

# Separando as variáveis entre PREDITORAS e ALVO
y = arquivo['style']
x = arquivo.drop('style', axis = 1)

print(arquivo.head())
print(y.head())