numero = int(input("Digite um numero qualquer: "))

def fibonacci_list(numero):
    fib_seq = [0, 1]
    while (fib_seq[-1]) < numero:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

if numero in fibonacci_list(numero):
    print("O número digitado pertence a sequência de fibonacci.")
else:
    print("O número digitado não pertence a sequência de fibonacci.")