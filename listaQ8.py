# -*- coding: utf-8 -*-
## Questão 8
## Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

## MAIN
string = raw_input('Entre com a cadeia de caracteres desejada: ') 
print "Cadeia lida: ", string

# retirando espaços e sinais de pontuação da cadeia lida (para casos mais complexos)
string =(((((string.replace(" ","")).replace(".","")).replace(",","")).replace(";","")).replace("!","")).replace("?","")

# quantidade de caracteres na string final
index = len(string) - 1

# variável utilizada para sinalizar se é verdadeiro ou falso para ser palidroma
r = True

# Para verificar se é palidroma, analisa o primeiro caractere com o ultimo, o segundo com o penultimo e
# assim sucessivamente
for i in range (len(string)/2):
    if (string[i] != string[index - i]):
            r = False   # se forem diferentes, então não é palidroma
            break       # encerra o loop
        
if (r == True):
    print "\nEssa sequencia de caracteres e palidroma."
else:
    print "\nEssa sequencia de caracteres nao e palidroma."

raw_input('\n\nQualquer tecla para finalizar...')
