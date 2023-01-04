km = float(input('Quantos km foram pecorridos: '))
dias = float(input('Quantos dias o carro foi alugado: '))
r = (km * 0.15) + (dias * 60)
print('O total a ser pago é: R${}'.format(r))