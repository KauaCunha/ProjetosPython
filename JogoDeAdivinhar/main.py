import random

min = int(input("Insira o mínimo número: "))
max = int(input("Insira o máximo número: "))

tentativas_restantes = 0

valor = random.randint(min,max)

while tentativas_restantes <= 4:
    tentativa_valor = int(input(f'\nChute um número entre {min} e {max}: '))
    tentativas_restantes += 1
    print(f'Tentativas restantes: {tentativas_restantes}')

    if tentativa_valor > valor:
        print('Valor muito alto!')

    if tentativa_valor < valor:
        print('Valor muito baixo!')

    if tentativa_valor == valor:
        print('\nParabéns você ganhou!!!\n')
    
    if tentativas_restantes > 4:
        print(f'\nA resposta era {valor}, tente novamente\n')
