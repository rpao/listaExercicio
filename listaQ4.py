# -*- coding: utf-8 -*-
## Questão 4
## Calcular o reajuste dos salários: recebe o salario utiliza o critério correto para reajustar
## Informar na tela:
##  o salário antes do reajuste;
##  o percentual de aumento aplicado;
##  o valor do aumento;
##  o novo salário, após o aumento.


sal = float(raw_input('Salario: ').replace(",","."))

## salários até R$ 280,00 (incluindo) : aumento de 20%
if (sal <= 280.00):
    percentual = 20  
## salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
elif(sal < 700.00):
    percentual = 15
## salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
elif(sal < 1500.00):
    percentual = 10
## salários de R$ 1500,00 em diante : aumento de 5%.
else:
    percentual = 5

aumento = percentual*sal/100

# Imprimindo valores
print "Salario antes do reajuste: R$", sal
print "Percentual de aumento aplicado:",percentual,"%"
print "Valor do aumento: R$", aumento
print "Novo salario: R$", sal+aumento

raw_input('\n\nQualquer tecla para finalizar...')

