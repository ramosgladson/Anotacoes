a = input('Digite algo: ')
print('É alfanumerico? {}'.format(a.isalnum()))
print('É somente numeros? {}'.format(a.isnumeric()))
print('É somente letras? {}'.format(a.isalpha()))
print('É inteiro? {}'.format(a.isdecimal()))
print('Tem somente letras minúsculas? {}'.format(a.islower()))
print('Tem somente letras maiúsculas? {}'.format(a.isupper()))