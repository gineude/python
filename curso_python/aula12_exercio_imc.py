nome = 'Gineude Silvestre'
altura = 1.70
peso = 78
# imc = peso / (altura * altura)
imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos', 'e seu IMC é')
print(round(imc, 2))