# -*- coding: utf-8 -*-
## Questão 3
## Calcular a média alcançada pelo aluno e imprimir "Aprovado", "Reprovado" ou "Aprovado com Distinção"
## de acordo com a média

nota1 = float(raw_input('Nota 1: ').replace(",","."))
nota2 = float(raw_input('Nota 2: ').replace(",","."))

media = (nota1 + nota2)/2

## A mensagem "Aprovado com Distinção", se a média for igual a dez.
if (media == 10):
    print "Aprovado com Distincao"
## A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
elif (media >= 7.0):
    print "Aprovado"
## A mensagem "Reprovado", se a média for menor do que sete;
else:
    print "Reprovado"

raw_input('\n\nQualquer tecla para finalizar...')
