# #### Floating Point Numbers (`float`)
# #### Números de Ponto Flutuante (`float`)

# 6. Write a program that receives two floating point numbers and perfoms theis addition.
# Escreva um programa que receba dois números flutuantes e realize sua adição.

# print("Write a program that receives two floating point numbers and perfoms theis addition.\n")
# try:
#     num_01 = float(input("Type a floating number: "))
#     num_02 = float(input("Type another floating number: "))
#     sum_calculation = num_01 + num_02

#     print(f"The sum of {num_01} and {num_02} is: {sum_calculation} \n")
# except ValueError:
#     (print("invalid input.Please enter a valid number"))

# 7. Creat a program that calculate the average of two floating point numbers provided by the user
# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# num_03 = float(input("Type a floating point number: "))
# num_04 = float(input("Type another floating point number: "))
# average_calculation = (num_03 + num_04) / 2

# print(f"The average of {num_03} and {num_04} is {average_calculation} \n")

# 8. Develop a program that calculates the
# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# num_05_str = input("Type a floating point number: ")
# num_05 = float(num_05_str)
# num_06_str = input("Type another number to get the power of first number: ")
# num_06 = float(num_06_str)
# power_num = num_05 ** num_06

# print(f"{num_05} to the power to {num_06} is {power_num}")


# 9. make a program that converts the temperature from Celsius to Fahrenheit.
# Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius_temp = float(input("Type the temperture (°C): "))
fahrenheit_temp = (celsius_temp * 9/5) +32

print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F \n")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.