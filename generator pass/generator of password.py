import random
import string


print('Gerador de senhas')

lista = string.ascii_uppercase
lista += string.digits
lista += string.ascii_lowercase



numeros = input('quantas senhas? ')
numeros = int(numeros)

letras = input('quantas letras quer? ')
letras = int(letras)

print('Senha gerada')

for senha in range(numeros):
    senha = ''
    for c in range(letras):
        senha += random.choice(lista)
    print(senha)

    