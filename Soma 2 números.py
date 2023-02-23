# Faça um Programa que peça dois números e imprima a soma.

soma = 0
lista = []
texto = ''
isValid = True
for numero in range(2):
    try:
        numeroTexto = (input('Digite um número: '))
        lista.append(float((numeroTexto.replace(',', '.'))))
        soma += lista[numero]
        if numero > 0 and lista[numero] >= 0:
            texto = texto + ' + ' + str(lista[numero])
        else:
            texto = texto + ' ' + str(lista[numero])
    except:
        print('O valor digitado deve ser um número!')
        isValid = False
        break

if isValid:
    print(texto, '=', soma)
