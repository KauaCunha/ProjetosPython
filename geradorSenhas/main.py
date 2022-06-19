import random

letras = [
    'A','B','C','Ç','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    'a','b','c','ç','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    '!','.',',','#','"',':',';','<','>',"'",'@',
    1,2,3,4,5,6,7,8,9,0
    ]

loop = 1

userDigitos = int(input('Qunatos caracteres você deseja na sua senha?: '))

print('Sua nova senha: ',end='')

while loop <= userDigitos:
    print(random.choice(letras),end='')
    loop+=1
    
print('')