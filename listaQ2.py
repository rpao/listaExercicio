# -*- coding: utf-8 -*-
## Questão 2

salHora = float(raw_input('Qual o salario/hora? ').replace(",","."))
horaMes = float(raw_input('Horas Trabalhadas por mes? ').replace(",","."))

## Salário do mês
salarioTotal = salHora*horaMes

## Desconto IR
ir = salarioTotal*0.11

## Desconto INSS
inss = salarioTotal*0.08

## Desconto sindicado
sind = salarioTotal*0.05

## Salario Liquido
salLiq = salarioTotal - ir - inss - sind

## Imprimindo dados
print "+ Salario Bruto: R$", salarioTotal
print "- IR (11%): R$",ir
print "- INSS (8%): R$",inss
print "- Sindicato (5%): R$",sind
print "= Salario Liquido: R$", salLiq

raw_input('\n\nQualquer tecla para finalizar...')
