import fatorial
import time

while True:
    try:
        print('*********************')
        print('*Cálculo do Fatorial*')
        print('*********************')
        num = int(input('Escreva seu Número inteiro >=0 (Número negativo para sair) = '))
        if num < 0:
            print('Aplicativo fechando', sep='', end='')
            for exit in range(3):
                print('.', sep='', end='')
                time.sleep(0.5)
            time.sleep(0.5)
            break
        print(num, '! = ', sep='', end='')
        if num <=10:
            for i in range(num, 1, -1):
                print(i,' x ', sep='', end='')
            print('1',sep='',end='')
            print(' = ', sep='', end='')
            print(fatorial.fatorial(num))
        else:
            print(fatorial.fatorial(num))
        time.sleep(1)
    except ValueError:
        print('\n **Por favor, escreva um número inteiro** \n')
        time.sleep(1)
