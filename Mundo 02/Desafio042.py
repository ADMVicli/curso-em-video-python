#Desafio042

n1 = float(input('Insira o primeiro seguimento: '))
n2 = float(input('Insira o segundo seguimento: '))
n3 = float(input('Insira o terceiro seguimento: '))

if n1 < n2 + n3 and n2 < n2 + n3 and n3 < n1 + n2:
    print('Ok! Esses três seguimentos podem formar um triângulo ', end='')
    if n1 == n2 == n3:
        print('equilátero!')
    elif n1 != n2 != n3 != n1:
        print('escaleno!')
    else:
        print('isóceles!')
else:
    print('Esses três seguimentos não podem formar um triângulo!')  