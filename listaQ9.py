# -*- coding: cp1252 -*-
# Quest�o 9
# 1. Abrir o arquivo "usuarios.txt" e obter os dados dos usu�rios
# 2. Converter o espa�o utilizado de bytes para Megabytes
# 3. Calcular o percentual de uso
# 4. Gerar um relat�rio

## Fun��o que converte de bytes para Megabytes
def _converteBytesMB(bytes):
    ##return bytes*0.000000953666
    return bytes/1048576.0

## Fun��o para calculo do percentual de cada usuario
def _calcularPercentual(espacoTotal, espacoUser):
    return espacoUser*100/espacoTotal


## MAIN
## Acessando arquivo
ref_arquivo = open('usuarios.txt', 'r')
linha = ref_arquivo.readlines()
ref_arquivo.close()

## Organizando os dados lidos
users = []
qtdUsers = 0

for i in range (len(linha)):
    linha[i] = linha[i].replace("\n","")
    users.append(linha[i].split(' '))
    try:
        ## Tenta converter para MB
        users[i][1] = float("%.2f"%(_converteBytesMB(float(users[i][1].replace(",",".")))))
    except:
        ## Se n�o for poss�vel, usu�rio n�o possui um valor valido de bytes utilizados e � exclu�do da lista
        users.remove(users[i])

## Calculo do espa�o total utilizado
espacoTotal = 0
for i in range(len(users)):
    espacoTotal += users[i][1]

## Calculo do percentual
percentual = []
for i in range(len(users)):
    percentual.append(float("%.2f"%(_calcularPercentual(espacoTotal, users[i][1]))))

## Dados do Relat�rio
texto =[]
texto.append("ACME Inc. Uso do espa�o em disco pelos usu�rios\n------------------------------------------------------------------------\nNr. Usu�rio Espa�o utilizado % do uso\n")
for i in range(len(users)):
    texto.append(str(i)+" "+users[i][0]+" "+str(users[i][1])+" MB "+str(percentual[i])+"\n")
texto.append("\nEspa�o total ocupado: "+str(espacoTotal)+" MB\nEspa�o m�dio ocupado: "+str(float("%.2f"%(espacoTotal/len(users))))+"MB")

## Imprimindo relat�rio na tela
for i in range (len(texto)):
    print texto[i]
"Relat�rio gerado com sucessor..."

## Escrevendo Relat�rio
ref_relatorio = open('relat�rio.txt', 'w')
ref_relatorio.writelines(texto)
ref_relatorio.close()

raw_input('\n\nQualquer tecla para finalizar...')
