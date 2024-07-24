class Temperaute:
    def __init__(self):
        pass
    def kelvin(self, c):
        return c + 273
    def fahrenheit(self, c):
        return ((c / 5) * 9) + 32
calcular = Temperaute()

print(f'Qual temperatura voce quer converter? \n1- Kelvin \n2- Fahrenheit')
opcao = input('Escreva o numero daquilo que deseja calcular: ')

if opcao == '1':
    c = float(input('Digite a temperatura em graus Celsius: '))
    print(f'{c}°C vira {calcular.kelvin(c)}K')
elif opcao == '2':
    c = float(input('Digite a temperatura em graus Celsius: '))
    print(f'{c}°C vira {calcular.fahrenheit(c)}°F')