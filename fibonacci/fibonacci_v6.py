#!/usr/bin/python3
# 0, 1, 1, 2, 3, 5, 8, 13, 21...


def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:
            break
    return resultado


if __name__ == "__main__":
    # listar os 20 primeiros números da sequência
    i=0
    for fib in fibonacci(20):
        i += 1
        print(f'{i}) {fib}')
        
