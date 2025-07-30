# #### try-except e if

# 21: Conversor de Temperatura
try:
    celsius_temp = float(input("Type the temperture (°C): "))
    fahrenheit_temp = (celsius_temp * 9/5) +32
    print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F \n")
except ValueError:
    print("Please, Enter a valid value to temperature. \n")

# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação