# Faça um Programa que pergunte quanto você ganha por
# hora e o número de horas trabalhadas no mês. Calcule e
# mostre o total do seu salário no referido mês.

# Primeiro um while pra manter o programa aberto até a saída do usuário
isOpened = True
while isOpened:

# Recebe os valores e verifica se são números (os decimais podem ser separados por "," ou ".")
    isNum = False
    salarioHoraTexto = (input('\nSalário por hora: R$'))
    horasTexto = (input('Horas trabalhadas: '))
    try:
        salarioHora = float(salarioHoraTexto.replace(',', '.'))
        horas = float(horasTexto.replace(',', '.'))
        isNum = True
    except: isNum = False

# Calcula o salário e formata para R$ 0.000,00
# Por fim pergunta se o usuário deseja continuar
    if isNum == True and salarioHora >= 0 and horas >= 0:
        salarioMes = format(salarioHora * horas, '_.2f')
        salarioMesTexto = str(salarioMes).replace('.', ',').replace('_', '.')
        print('\nEste mês, seu salário é de R$', salarioMesTexto)
        resposta = input('\nCalcular outro salário?'
                         '\nSim [S] | Não [N]\n')
    else:
        resposta = input('\nOs valores precisam ser numéricos e positivos. Deseja tentar novamente?'
                         '\nSim [S] | Não [N]\n')

# Loop até receber uma resposta válida "S" ou "N"
# Este loop sai com o comando break
    notValid = True
    while notValid:
        if resposta.upper() == 'S':
            break
        elif resposta.upper() == 'N':
            isOpened = False
            break
        else:
            resposta = input('\nDesculpa, não pude identifcar sua resposta. Deseja tentar novamente?'
                             '\nDigite, sem aspas, "S" para Sim ou "N" para Não\n')
