
numeroEncontrar = int(input('Informe um número para saber se ele pertence a sequência de Fibonacci?'))
quantTermos = 50
cont = 3
t1 = 0
t2 = 1
print(t1,' - ',t2,end=' - ')
lista = [0,1]
while cont <= quantTermos:
    t3 = t1 + t2
    print(t3,end=' - ')
    t1 = t2
    t2 = t3
    cont += 1
    lista.append(t3)
print('Fim do Programa')


if numeroEncontrar in lista:
    print('Tem na lista')
else:
    print('Não tem na Lista')

