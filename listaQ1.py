# -*- coding: utf-8 -*-
## Questão 2
## Calcula o peso ideal de acordo com o sexo e a altura e verifica se está acima, abaixo ou no peso ideal

# Lê altura
h = float(raw_input('Altura (cm):').replace(",","."))

# Calculo do peso ideal de acordo com as fórmulas
fim = False # Garante que sexo seja F/f ou M/m
while (fim == False):
    sexo = raw_input('Sexo (M - masculino ou F - feminino):')
    ## Peso ideal - Homem
    if (sexo == "M" or sexo == "m"):
        pesoIdeal = 72.7*h - 58
        fim = True
    ## Peso ideal - Mulher
    elif (sexo == "F" or sexo == "f"):
        pesoIdeal = 62.1*h - 44.7
        fim = True
    else:
        print "Sexo Desconhecido"

# Lê o peso atual
peso = float(raw_input('Qual seu peso?').replace(",","."))

## Verificar peso
if (peso < pesoIdeal):
    print "Voce esta abaixo do peso ideal"
elif (peso == pesoIdeal):
    print "Voce esta no seu peso ideal"
else:
    print "Voce esta acima do peso ideal"

raw_input('\n\nQualquer tecla para finalizar...')
