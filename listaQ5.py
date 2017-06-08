# -*- coding: utf-8 -*-
## Questão 5
## Validar as seguintes condições
##  a. Nome: maior que 3 caracteres;
##  b. Idade: entre 0 e 150;
##  c. Salário: maior que zero;
##  d. Sexo: 'f' ou 'm';
##  e. Estado Civil: 's', 'c', 'v', 'd';

validacao = False
while (validacao == False):
    nome = raw_input('Nome: ')
    #  a. Nome: maior que 3 caracteres;
    if (len(nome) <= 3):
        print "Nome precisar ter mais que 3 caracteres"
    else: validacao = True

validacao = False
while (validacao == False):
    idade = int(raw_input('Idade: '))
    #  b. Idade: entre 0 e 150;
    if (idade <= 0 or idade >= 150):
        print "Idade deve estar entre 0 e 150 anos."
    else: validacao = True

validacao = False
while (validacao == False):
    sal = float(raw_input('Salario: ').replace(",","."))
    #  c. Salário: maior que zero;
    if (sal <= 0):
        print "Salario deve ser maior que 0 (zero)."
    else: validacao = True

validacao = False
while (validacao == False):
    sexo = raw_input('Sexo: ')
    #  d. Sexo: 'f' ou 'm';
    if (sexo != 'f' and sexo != 'm'):
        print "Sexo deve ser 'f' (feminino) ou 'm'(masculino)"
    else: validacao = True
    
validacao = False
while (validacao == False):
    eCivil = raw_input('Estado Civil: ')
    #  e. Estado Civil: 's', 'c', 'v', 'd';
    if (eCivil !='s' and eCivil !='c' and eCivil !='v' and eCivil !='d'):
        print"Estado Civil pode ser: s (solteiro), c (casado), v (viuvo) ou d(divorciado)"
    else: validacao = True


raw_input('\n\nQualquer tecla para finalizar...')
