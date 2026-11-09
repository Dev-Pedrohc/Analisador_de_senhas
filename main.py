# Programa que analisa a força de uma senha digitada pelo usuário, utilizando a linguagem Python
senha = input('Digite sua senha: ')
maiuscula = 0
minuscula = 0
numeros = 0
caracteres = 0
pontos = 0

for digitos in senha:
   if digitos.isupper():
       maiuscula+=1
   elif digitos.islower():
       minuscula+=1
   elif digitos.isdigit():
       numeros+=1
   else:
       caracteres+=1
       
       
#Como vai funcionar o sistema de pontuação para verificar se a senha é forte, média ou fraca
#Maiúscula(>=2) = 2 Pontos, Maiúscula(=1) = 1 Ponto, Maiúscula(0) = 0
#Minúscula(>=2) = 2 Pontos, Minúscula(=1) = 1 Ponto, Minúscula(0) = 0
#Números(>=2) = 2 Pontos , Números(=1) = 1 Ponto, Números(0) = 0 Ponto
#Caracteres(>=1) = 1 Ponto, Caracteres(=0) = 0 Pontos
#total de Dígitos >=8 = 1 Ponto

if maiuscula >= 2:
    pontos+=2
elif maiuscula == 1:
    pontos+=1
if minuscula >= 2:
    pontos+=2
elif minuscula == 1:
    pontos+=1
if numeros >= 2:
    pontos+=2
elif numeros >= 1:
    pontos+=1
if caracteres >= 1:
    pontos+=1
if len(senha) >= 8:
    pontos+=1

#Classificação: 0 a 3 é Fraca, 4 a 7 é Média, 8 é Forte.
if pontos >= 8:
    print(f'\033[1;32mSua senha é uma senha considerada forte, tendo {maiuscula} letras maiúsculas, {minuscula} letras minúsculas, {numeros} números e {caracteres} caracteres!')
elif pontos >= 4:
    print(f'\033[1;33mSua senha é uma senha considerada média, tendo {maiuscula} letras maiúsculas, {minuscula} letras minúsculas, {numeros} números e {caracteres} caracteres! ')
else:
    print(f'\033[1;31mSua senha é uma senha considerada fraca, tendo {maiuscula} letras maiúsculas, {minuscula} letras minúsculas, {numeros} números e {caracteres} caracteres!')


    
