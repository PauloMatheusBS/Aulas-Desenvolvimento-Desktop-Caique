# Lista de Exercícios (10/10)

#1 - Crie uma função que calcule o fatorial de um número dado pelo usuário.
def fatorial(n):
    if n < 0:
        return "Deu RUIM, n pode ser negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

num = int(input("Digite um número: "))
print(f"O fatorial de {num} é {fatorial(num)}.")

#############################################################################################################################################
#2 - Desenvolva um programa que mostre a tabuada de um número informado pelo usuário.
#3 - Escreva uma função que verifique se uma palavra ou frase é um palíndromo (pode ser lida da mesma maneira de trás para frente).
#4 - Faça um programa que verifique se um número fornecido é primo.
#5  - Desenvolva uma função que mostre os n primeiros termos da sequência de Fibonacci, onde n é informado pelo usuário.
#6 - Escreva um algoritmo que receba uma lista de números e retorne a lista ordenada de forma crescente (Bubble sort).
#7 - Faça um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa. O usuário deverá escolher a conversão desejada.
#8 - Crie um algoritmo que receba 5 números e exiba o maior e o menor número informados.