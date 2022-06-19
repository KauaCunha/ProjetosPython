import json
import os
import os.path
import GoblinInimigo
import Player

new_goblin = GoblinInimigo.Goblin
new_player = Player.Player

rounds = '1234567'

save = []
#inimigos = [new_goblin.]

def Subir_De_Level():
    if new_player.EXPs >= 100 and new_player.EXPs < 200:
        print('Você subiu de Level!')
        new_player.Level += 1



def Salvar():
    save.append(new_player.EXPs)
    save.append(new_player.Level)
    save.append(new_player.player_HP)
    save.append(new_player.player_ATK)
    save.append(new_player.inimigos_mortos)
    with open('JogoRPG/data.json','w') as data:
        json.dump(save,data)



def Carregar_Save():
    # Verifica se há algum save pré escrito
    f_existe = os.path.exists('JogoRPG/data.json')
    if f_existe == True:
        # Faz com que o arquivo data.json seja manipulável 
        with open('JogoRPG/data.json') as data_save:
            jogador=json.load(data_save) # Atribuo os valores json à jogador
        # Atribuo os valores já salvos aos novos atributos    
        new_player.EXPs = jogador[0]
        new_player.Level = jogador[1]
        new_player.player_HP = jogador[2]
        new_player.player_ATK = jogador[3]
        new_player.inimigos_mortos = jogador[4]



def Atacar():
    os.system('clear') or None
    for i in rounds:
        new_goblin.goblin_HP -= new_player.player_ATK
        new_player.player_HP -= new_goblin.goblin_ATK
        print('\nROUND:',i)
        print('Goblin HP:', new_goblin.goblin_HP)
        print('Player HP:', new_player.player_HP)
        if new_goblin.goblin_HP <=0:
            print('\nVocê venceu! HP restaurado.')
            print(new_goblin.EXPs_oferecida,' XP ganha')
            new_player.EXPs += new_goblin.EXPs_oferecida
            new_player.inimigos_mortos += 1
            new_goblin.goblin_HP = 20
            #new_player.player_HP = 100
            Subir_De_Level()
            break


def Lista_Inimigo():
    while True:
        opcao_de_inimigo = input('Qula irá atacar?')


def Menu_Jogo():
    while True:
        
        print('\nXP:', new_player.EXPs, '- Level:',new_player.Level) 
        print('Player HP:', new_player.player_HP)
        print('Player ATK:', new_player.player_ATK)
        print('Inimigos Mortos:', new_player.inimigos_mortos)
        opcao_de_acao = input('\nAtacar[A] | Correr[C] | Sair e Salvar[S]-> ')

        if opcao_de_acao == 'A':
            Atacar()

        elif opcao_de_acao == 'C':
            print('Você fugiu com segurança')
        
        elif opcao_de_acao == 'S':
            Salvar()
            print('Jogo salvo com sucesso')
            break

        else:
            print('Escolha uma das opções ditas!')



def Menu_Principal():
    print('''
[1] Novo Jogo
[2] Carregar Jogo
[3] Sair
    ''')
    opcao_jogador = input('Insira sua ação: -> ')

    if opcao_jogador == '1':
        new_f_existe = os.path.exists('JogoRPG/data.json')
        #print(new_f_existe)
        if new_f_existe == False:
            Menu_Jogo()

        if new_f_existe == True:
            print('Você já tem um save, deseja apagar todos os dados?')
            opcao_apagar = input('S/s ou N/n -> ')
            if opcao_apagar == 'S':
                os.remove("JogoRPG/data.json")
                print('Dados apagados.')
                Menu_Jogo()

            if opcao_apagar == 'N':
                Menu_Principal()

    if opcao_jogador == '2':
        f_existe = os.path.exists('JogoRPG/data.json')
        if f_existe == True:
            Carregar_Save()
            Menu_Jogo()
        if f_existe == False:
            print('Criando Novo Jogo..\n')
            Menu_Jogo()

    if opcao_jogador == '3':
        os.system('exit')

    else:
        pass


Menu_Principal()