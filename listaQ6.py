# -*- coding: utf-8 -*-
## Questão 6
## Gerar tabuada do número desejado pelo usuário

numero = int(raw_input('Numero: '))

print "Tabuada de ", numero, ": "
# Calcula a tabuada dentro do for, para o intervalo de 1 a 10
for i in range(1, 11):
    print "\t",numero, " X ", i, " = ", numero*i

raw_input('\n\nQualquer tecla para finalizar...')
