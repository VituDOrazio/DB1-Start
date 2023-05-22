# Escreva uma classe em Python para converter um número inteiro em um numeral romano.

class Romanos:
    # Conversores
    unidades = {
        '0': '',
        '1': 'I',
        '2': 'II',
        '3': 'III',
        '4': 'IV',
        '5': 'V',
        '6': 'VI',
        '7': 'VII',
        '8': 'VIII',
        '9': 'IX'
    }
    dezenas = {
        '0': '',
        '1': 'X',
        '2': 'XX',
        '3': 'XXX',
        '4': 'XL',
        '5': 'L',
        '6': 'LX',
        '7': 'LXX',
        '8': 'LXXX',
        '9': 'LC'
    }
    centenas = {
        '0': '',
        '1': 'C',
        '2': 'CC',
        '3': 'CCC',
        '4': 'CD',
        '5': 'D',
        '6': 'DC',
        '7': 'DCC',
        '8': 'DCCC',
        '9': 'DM'
    }
    milhares = {
        '0': '',
        '1': 'M',
        '2': 'MM',
        '3': 'MMM'
    }

    # Lista com os conversores para rodar no for
    conversor = ['', unidades, dezenas, centenas, milhares]

    def __init__(self, numero):
        self.numero = numero
        self.numeroConvertido = ''
        self.isValid = True
        self.error = ''

        try:
            # Verifica se o número é inteiro, se não for entra no except
            numeroInt = int(numero)

            # Verifica se o número é menor que 4000
            if numeroInt >= 4000:
                self.isValid = False
                self.error = 'O número é maior ou igual a 4000 e a aplicação não suporta essa ação.'

            # Verifica se o número é maior que 0
            if numeroInt < 0:
                self.isValid = False
                self.error = 'O número é menor que zero.'
        except:
            self.isValid = False
            self.error = 'O número não é um inteiro.'

        # Se válido converte o número
        if self.isValid:
            tamanho = len(numero)
            for i in range(tamanho):
                self.numeroConvertido = self.numeroConvertido + self.conversor[tamanho - i][numero[i]]


# Entrada de dados
entrada = Romanos(input("Digite o número que você deseja converter em romanos: "))

# Se a entrada é válida imprime o resultado
if entrada.isValid:
    print(f"O número '{entrada.numero}' em romanos se escreve '{entrada.numeroConvertido}'.")
# Caso contrário, imprime o erro.
else:
    print(entrada.error)
