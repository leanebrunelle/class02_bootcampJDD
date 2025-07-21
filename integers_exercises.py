# #### Integers (`int`)

# 1. Write a program that adds two integers entered by the user. 
# (Escreva um programa que soma dois números inteiros inseridos pelo usuário.)

number_one = int(input("Type a number: "))
number_two = int(input("Type another number: "))
number_total = number_one + number_two

print(f"The total value is: {number_total} \n")

# 2. Create a program that receives a number from the user and calculates the remainder of dividing that number by 5.
# (Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.)

divider = int(input("Type a number: "))
dividend = 5
division_total = divider / dividend
remainder = divider % dividend

print(f"The value of division is {division_total} and the remainder is {remainder}. \n")

# 3. Develop a program that multiplies two numbers provided by the user and displays the result.
# (Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.)

number_1 = int(input("Type a number: "))
number_2 = int(input("Type another number: "))
multiplication = number_1 * number_2

print(f"The value of multiplication is {multiplication}. \n")

# 4. Write a program that asks for two integers and prints the integer division of the first by the second.
# (Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.)

divisor_1 = int(input("Type a number: "))
dividend_1 = int(input("Typer another number: "))
division_1 = divisor_1 // dividend_1

print(f"The integer division is {division_1}. \n")

# 5. Write a program that calculates the square of a number provided by the user.
# (Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.)

provide_number = int(input("Type a number: "))
square_number = provide_number ** 2

print(f"The square of the value is {square_number}. \n")
