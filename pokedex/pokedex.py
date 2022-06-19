import os

POKEMON = {
    'bulbasaur':{ #001
        'numero':'001',
        'nome':'Bulbasaur',
        'tipos':['Grass','Poison'],
        'habilidades':['Overgrow','Chlorophill'],
        'fraquezas':['Flying','Fire','Psychic','Ice'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Fighting','Water','Grass','Eletric','Fairy'],
        'basestatus':['45','49','49','65','65','45']},
    'ivysaur':{ #002
        'numero':'002',
        'nome':'Ivysaur',
        'tipos':['Grass','Poison'],
        'habilidades':['Overgrow','Chlorophill'],
        'fraquezas':['Flying','Fire','Psychic','Ice'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Fighting','Water','Grass','Eletric','Fairy'],
        'basestatus':['60','62','63','80','80','60']},
    'venusaur':{ #003
        'numero':'003',
        'nome':'Venusaur',
        'tipos':['Grass','Poison'],
        'habilidades':['Overgrow','Chlorophill'],
        'fraquezas':['Flying','Fire','Psychic','Ice'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Fighting','Water','Grass','Eletric','Fairy'],
        'basestatus':['80','82','83','100','100','80']},
    'charmander':{ #004
        'numero':'004',
        'nome':'Charmander',
        'tipos':['Fire'],
        'habilidades':['Blaze','Solar Power'],
        'fraquezas':['Ground','Rock','Water'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Bug','Steel','Fire','Grass','Ice','Fairy'],
        'basestatus':['39','52','43','60','50','65']},
    'charmeleon':{ #005
        'numero':'005',
        'nome':'Charmeleon',
        'tipos':['Fire'],
        'habilidades':['Blaze','Solar Power'],
        'fraquezas':['Ground','Rock','Water'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Bug','Steel','Fire','Grass','Ice','Fairy'],
        'basestatus':['58','64','58','80','65','80']},
    'charizard':{ #006
        'numero':'006',
        'nome':'Charizard',
        'tipos':['Fire','Flying'],
        'habilidades':['Blaze','Solar Power'],
        'fraquezas':['Ground','Rock','Water'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Bug','Steel','Fire','Grass','Ice','Fairy'],
        'basestatus':['78','84','78','109','85','100']},
    'squirtle':{ #007
        'numero':'007',
        'nome':'Squirtle',
        'tipos':['Water'],
        'habilidades':['Torrent','Rain Dish'],
        'fraquezas':['Grass','Eletric'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Stell','Fire','Water','Ice'],
        'basestatus':['44','48','65','50','64','43']},
    'wartortle':{ #008
        'numero':'008',
        'nome':'Sartortle',
        'tipos':['Water'],
        'habilidades':['Torrent','Rain Dish'],
        'fraquezas':['Grass','Eletric'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Stell','Fire','Water','Ice'],
        'basestatus':['59','63','80','65','80','58']},
    'blastoise':{ #09
        'numero':'009',
        'nome':'Blastoise',
        'tipos':['Water'],
        'habilidades':['Torrent','Rain Dish'],
        'fraquezas':['Grass','Eletric'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Stell','Fire','Water','Ice'],
        'basestatus':['79','83','100','85','105','78']},
    'cartepie':{ #010
        'numero':'010',
        'nome':'Cartepie',
        'tipos':['Bug'],
        'habilidades':['Shield Dust','Run Away'],
        'fraquezas':['Flying','Rock','Fire'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Fighting','Ground','Grass'],
        'basestatus':['45','30','35','20','20','45']},
    'metapod':{ #011
        'numero':'011',
        'nome':'Metapod',
        'tipos':['Bug'],
        'habilidades':['Shield Skin'],
        'fraquezas':['Flying','Rock','Fire'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Fighting','Ground','Grass'],
        'basestatus':['50','20','55','25','25','30']},
    'butterfree':{ #012
        'numero':'012',
        'nome':'Butterfree',
        'tipos':['Bug','Flying'],
        'habilidades':['Compound Eyes','Tinted Lens'],
        'fraquezas':['Flying','Rock','Fire','Eletric','Ice','Ground'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Fighting','Ground','Grass'],
        'basestatus':['60','45','50','80','80','70']},
    'weedle':{ #013
        'numero':'013',
        'nome':'Weedle',
        'tipos':['Bug','Poison'],
        'habilidades':['Shield Dust'],
        'fraquezas':['Flying','Rock','Fire','Psychic'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Fighting','Poison','Bug','Grass','Fairy'],
        'basestatus':['40','35','30','20','20','50']},
    'kakuna':{ #014
        'numero':'014',
        'nome':'Kakuna',
        'tipos':['Bug','Poison'],
        'habilidades':['Shield Skin'],
        'fraquezas':['Flying','Rock','Fire','Psychic'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Fighting','Poison','Bug','Grass','Fairy'],
        'basestatus':['45','25','50','25','25','35']},
    'beedrill':{ #0015
        'numero':'015',
        'nome':'Beedrill',
        'tipos':['Bug','Poison'],
        'habilidades':['Swarm','Sniper'],
        'fraquezas':['Flying','Rock','Fire','Psychic'],
        'imunidade':['Sem Imunidade'],
        'resistente':['Fighting','Poison','Bug','Grass','Fairy'],
        'basestatus':['65','80','40','45','80','75']},
    'pidgey':{ #016
        'numero':'016',
        'nome':'Pidgey',
        'tipos':['Normal','Flying'],
        'habilidades':['Keen Eye','Big Pecks'],
        'fraquezas':['Rock','Eletric','Ice'],
        'imunidade':['Ground','Ghost'],
        'resistente':['Bug','Grass',],
        'basestatus':['40','45','40','35','35','56']},
    'pidgeotto':{ #017
        'numero':'017',
        'nome':'Pidgeotto',
        'tipos':['Normal','Flying'],
        'habilidades':['Keen Eye','Big Pecks'],
        'fraquezas':['Rock','Eletric','Ice'],
        'imunidade':['Ground','Ghost'],
        'resistente':['Bug','Grass',],
        'basestatus':['63','60','55','50','50','71']},
    'pidgeot':{ #018
        'numero':'018',
        'nome':'Pidgeot',
        'tipos':['Normal','Flying'],
        'habilidades':['Keen Eye','Big Pecks'],
        'fraquezas':['Rock','Eletric','Ice'],
        'imunidade':['Ground','Ghost'],
        'resistente':['Bug','Grass',],
        'basestatus':['83','80','75','70','70','91']},
    'rattata':{ #019
        'numero':'019',
        'nome':'Rattata',
        'tipos':['Normal'],
        'habilidades':['Run Away','Guts','Hustle'],
        'fraquezas':['Fighting'],
        'imunidade':['Ghost'],
        'resistente':['Sem Imunidade',],
        'basestatus':['30','56','35','25','35','72']},
    'raticate':{ #020
        'numero':'020',
        'nome':'Raticate',
        'tipos':['Normal'],
        'habilidades':['Run Away','Guts','Hustle'],
        'fraquezas':['Fighting'],
        'imunidade':['Ghost'],
        'resistente':['Sem Imunidade',],
        'basestatus':['55','81','60','50','70','97']},


}
var = ['HP:   ','ATK:  ','DEF:  ','SPATK:','SPDEF:','SPEED:']

def get_pokemon_by_name(nome):
    os.system('clear')
    #print(POKEMON[nome])
    print('ID:',POKEMON[nome]['numero'])
    print('Nome:',POKEMON[nome]['nome'])
    print('Tipos:',*POKEMON[nome]['tipos'])
    print('Fraquezas:',*POKEMON[nome]['fraquezas'])
    print('Imunidade:',*POKEMON[nome]['imunidade'])
    print('Resistencias:',*POKEMON[nome]['resistente'],'\n')

    for i, ii in zip(var, POKEMON[nome]['basestatus']):
        print(i, ii)
    
    basetotal = [int(string) for string in POKEMON[nome]['basestatus']]
    print('TOTAL:',sum(basetotal))



nome = input('Nome do Pokemon: ')

if nome in POKEMON:
    get_pokemon_by_name(nome)
else:
    print('Digite corretamente o nome do Pokémon.')