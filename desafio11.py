base = float(input('Informe a largura da sua parede em metros: '))
altura = float(input('Informe a altura da sua parede em metros: '))
a = (base*altura)/2
print('Voce precisa de {:.2f}L de tinta para pintar a parede da sua casa'.format(a))