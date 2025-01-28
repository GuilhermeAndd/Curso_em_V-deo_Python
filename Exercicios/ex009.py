def tabuada(n1):
    for i in range (1, 11):
        resultado = n1 * i 
        print(f'{n1} x {i} = {resultado}')

n_i = int(input('Digite um número inteiro: '))
print('A tabuada do número digitado é: ')
print('-' * 12)
tabuada(n_i)
print('-' * 12)


