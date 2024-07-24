class Areas:
    def __init__(self):
        pass
    def quadrado(self, lado):
        return lado ** 2
    def triangulo(self, base, altura):
        return(base * altura) / 2
    def circulo(self, raio):
        return(raio ** 2) * 3.14

calcular = Areas()

print(f'Qual área deseja calcular? \n1- Quadrado \n2- Triangulo \n3- Circulo')
opcao = input('Insira sua respota (1 / 2 / 3): ')

if opcao == '1':
    print('Voce escolheu -> Quadrado')
    lado = float(input('Coloque o lado do quadrado: '))
    print(f'A area do quadrado e {calcular.quadrado(lado)}')
elif opcao == '2':
    print('Voce escolheu -> Triangulo')
    base = float(input('Valor da base: '))
    altura = float(input('Valor da altura: '))
    print(f'A area do triangulo e {calcular.triangulo(base, altura)}')
elif opcao == '3':
    print('Voce escolheu -> Circulo')
    raio = float(input('Valor do raio: '))
    print(f'A area do circulo e {calcular.circulo(raio)}')