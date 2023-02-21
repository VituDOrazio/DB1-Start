#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

#Meses e seus respectivos últimos dias
#O ano bissexto é tratado mais adiante
meses = [1,2,3,4,5,6,7,8,9,10,11,12]
dias = [31,28,31,30,31,30,31,31,30,31,30,31]

#Quebra a string digitada em uma lista 'dd', 'mm', 'aaaa'
data = input('Digite a data no formato dd/mm/aaaa: ')
listaData = data.split("/")
novaListaData = []

#Transforma as strings da lista em inteiros e verifica se foram digitados apenas números inteiros
isInt = True
index = 0
while index < len(listaData):
    try:
        novaListaData.insert(index, int(listaData[index]))
    except: isInt = False
    index += 1

#Verifica se o ano é bissexto a partir do resto da divisão por 4
#e modifica seu respectivo último dia na lista de dias
isBissexto = False
try:
    if listaData[2] % 4 == 0:
        isBissexto = True
        dias[1] = 29
    else:
        isBissexto = False
        dias[1] = 28
except: pass

#Verifica se a data é válida:
#1. Ano maior que 0
#2. Mês pertence à lista de meses
#3. Dia maior que 0 e menor ou igual último dia do mês
isValid = False
index = 0
while index < len(meses) or isValid == False:
    try:
        if novaListaData[2] > 0 and novaListaData[1] == meses[index] and 0 < novaListaData[0] <= dias[index]:
            isValid = True
            break
    except: pass
    index += 1

if isInt and isValid:
    print('A data ',data,' é válida!')
else: print('A data ',data, ' NÃO é válida!')