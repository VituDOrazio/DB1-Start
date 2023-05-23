# Escreva uma classe em Python para converter um número inteiro em um numeral romano.

class Numero:
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
    conversor = [unidades, dezenas, centenas, milhares]

    def __init__(self, numero):
        self.numero = numero
        self.numeroConvertido = ''
        self.isInt = False
        self.maiorZero = False
        self.menor4000 = False
        self.error = ''

    def flags(self):
        # Verifica se o número é inteiro
        try:
            numeroInt = int(self.numero)
            self.isInt = True
        except:
            self.error = 'O número não é um inteiro.'

        # Verifica se o número é maior que 0
        try:
            if numeroInt > 0:
                self.maiorZero = True
            else:
                self.error = 'O número é menor que zero.'
        except:
            pass

        # Verifica se o número é menor que 4000
        try:
            if numeroInt <= 4000:
                self.menor4000 = True
            else:
                self.error = 'O número é maior ou igual a 4000 e a aplicação não suporta essa ação.'
        except:
            pass

    def converterRomanos(self):
        self.flags()
        # Se válido converte o número
        if self.isInt and self.maiorZero and self.menor4000:
            tamanho = len(self.numero)
            for i in range(tamanho):
                self.numeroConvertido = self.conversor[i][self.numero[(tamanho - 1) - i]] + self.numeroConvertido

# Entrada de dados
entrada = Numero(input("Digite o número que você deseja converter em romanos: "))
entrada.converterRomanos()

# Se a entrada é válida imprime o resultado
if entrada.isInt and entrada.maiorZero and entrada.menor4000:
    print(f"O número '{entrada.numero}' em romanos se escreve '{entrada.numeroConvertido}'.")
# Caso contrário, imprime o erro.
else:
    print(entrada.error)