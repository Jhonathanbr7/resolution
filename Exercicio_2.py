# Recebe o número como entrada
num = int(input("Digite um número: "))

# Define os valores iniciais da sequência
fib1 = 0
fib2 = 1
fib = fib1 + fib2

# Percorre a sequência de Fibonacci até encontrar um número maior que o número digitado
while fib < num:
    fib1 = fib2
    fib2 = fib
    fib = fib1 + fib2

# Verifica se o número pertence à sequência de Fibonacci
if fib == num:
    print(num, "pertence à sequência de Fibonacci")
else:
    print(num, "não pertence à sequência de Fibonacci")