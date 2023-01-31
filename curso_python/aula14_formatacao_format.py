a = 'A'
b = 'B'
c = 1.1
string = 'a={0} b={nome2} c={nome3:.2f}'

# tudo que vier após um parametro nomeado, também precisa se nomeado
formato = string.format(a, nome2=b, nome3=c)

print(formato)