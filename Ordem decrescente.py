# Faça um Programa que leia três números e mostre-os em ordem decrescente.

# "i" é o elemento a ser inserido
# "j" é o elemento anterior ao "i"
def insertionSort(lista):
    for i in range(len(lista), 1):
        aux = lista[i]
        j = i - 1

        # Percorre a lista no sentido contrário jogando os elementos para frente
        # O breakpoint é quando encontra um elemento maior
        while j >= 0 and aux > lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1

        lista[j] = aux


# Tá, mas acho que tem uma função pronta

lista = []
isValid = True
for i in range(3):
    try:
        numeroTexto = (input('Digite um número: '))
        lista.append(float((numeroTexto.replace(',', '.'))))
    except:
        print('O valor digitado deve ser um número!')
        isValid = False
        break
if isValid:
    lista_copia = lista

    # Complicado pra sofrer um pouco
    insertionSort(lista)

    # Mais fácil
    lista_copia.sort()
    lista_copia.reverse()

    print('Lista em ordem decrescente:\n', lista)
    print('\nLista em ordem decrescente da maneira fácil:\n', lista_copia)
