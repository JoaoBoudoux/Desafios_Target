import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(num):
    
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))#numero que vai ser verificado


if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")