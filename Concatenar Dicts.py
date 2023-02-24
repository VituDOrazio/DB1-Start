"""
Escreva um programa que concatene os dicionários abaixo e crie um novo
Exemplo dicionário(Dict):
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Resultado esperado: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

dic1 = {1: 10, 3: 20, 'Teste': 'Valor'}
dic2 = {3: 30, 4: 40, 100: 'Valor'}
dic3 = {5: 50, 3: 60, 'Teste': 100}
lista = [dic1, dic2, dic3]

dic4 = {}
for dict in lista:
    for chave in dict:
        dic4[chave] = dict[chave]
print('União - Concatenando e sobrescrevendo:\n', dic4)

# Criando nova chave para não sobrescrever
dic5 = {}
for dict in lista:
    for chave in dict:

        n = ' (1)'
        chaveAux = str(chave)
        for registrada in dic5.keys():
            while chaveAux == registrada:
                chaveAux = str(chave) + n
                n = ' (' + str(int(n.replace(' (', "").replace(')', "")) + 1) + ')'

        dic5[chaveAux] = dict[chave]
print('\nInterseção - Concatenando criando nova chave se repetida:\n', dic5)
