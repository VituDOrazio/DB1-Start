# Faça um Programa que peça dois números e imprima a soma.

soma = 0
texto = ''
isValid = True
for i in range(2):
    try:
        numeroTexto = (input('Digite um número: '))
        numero=(float((numeroTexto.replace(',', '.'))))
        soma += numero
        if i > 0 and numero >= 0:
            texto = texto + ' + ' + str(numero)
        else:
            texto = texto + ' ' + str(numero)
    except:
        print('O valor digitado deve ser um número!')
        isValid = False
        break

if isValid:
    print(texto, '=', soma)
