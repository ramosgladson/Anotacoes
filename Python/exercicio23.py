
numero = input('Digite um número de 0 a 9999: ')
if len(numero) > 4:
    print('Você digitou um número inválido.')
else:
    print('Você digitou {}'.format(numero))
    if len(numero) == 4:
        print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(numero[3], numero[2], numero[1], numero[0]))
    if len(numero) == 3:
        print('unidade: {}\ndezena: {}\ncentena: {}'.format(numero[2], numero[1], numero[0]))
    if len(numero) == 2:
        print('unidade: {}\ndezena: {}'.format(numero[1], numero[0]))
    if len(numero) == 1:
        print('unidade: {}'.format(numero[0]))
    print('Ou de forma matenática')
    milhar = int(numero)//1000
    centena = ((int(numero)%1000)//100)
    dezena = ((int(numero)%100)//10)
    unidade = ((int(numero)%10)) 
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))
