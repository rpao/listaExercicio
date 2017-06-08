# -*- coding: utf-8 -*-
## Questão 7
## Construa uma função que receba como parâmetro uma data no formato DD/MM/AAAA e
## devolva uma string no formato "D de mesPorExtenso de AAAA".
## Opcionalmente, valide a data e retorne uma mensagem caso a data seja inválida.

def _verificarAnoBissexto(ano):
    if (ano%400 == 0 or (ano%4 == 0 and ano%100 != 0)) :
        return True
    return False

def _validacao_data (D, M, A):
    # Se mês for menor que 1 (janeiro) ou maior que 12 (dezembro): Data inválida
    # Se o dia for menor que 1 ou maior que 31: data inválida
    if ( M < 1 or M > 12 or D < 1 or D > 31): return False

    # Para mês 2 (fevereiro)
    elif (M == 2):
        # Se ano for bissexto
        if (_verificarAnoBissexto(A)):
            # dia maior que 29: data inválida
            if (D > 29): return False
        # Se não for bisexto, então dia maior que 28: data inválida
        elif(D > 28): return False

    # Para os meses de 30 dias, se o dia é maior que 30: data inválida
    elif (M in [4, 6, 9, 11] and D > 30): return False

    # Se todos os casos falharam, a data é válida
    return True

# Obtém o nome do mês por extenso
def _mes_extenso(M):
    if (M == 1): mes = "Janeiro"
    elif (M == 2): mes = "Fevereiro"
    elif (M == 3): mes = "Março"
    elif (M == 4): mes = "Abril"
    elif (M == 5): mes = "Maio"
    elif (M == 6): mes = "Junho"
    elif (M == 7): mes = "Julho"
    elif (M == 8): mes = "Agosto"
    elif (M == 9): mes = "Setembro"
    elif (M == 10): mes = "Outubro"
    elif (M == 11): mes = "Novembro"
    else: mes = "Dezembro"
    return mes
        
            
## MAIN
strData = raw_input('Informe a data desejada: ')
data = strData.split("/")
# Se data for válida, faz a conversão de formato
if (_validacao_data(int(data[0]), int(data[1]), int(data[2]))):
    stringFinal = data[0] +" de "+ _mes_extenso(int(data[1])) +" de "+ data[2];
# Se não for válida, informa o usuário
else:
    stringFinal = "Data Invalida"

print stringFinal

raw_input('\n\nQualquer tecla para finalizar...')
