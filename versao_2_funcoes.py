# Conversor de temperatura: Celsius, Fahrenheit e Kelvin

# Cada função recebe uma temperatura, faz a conta e devolve o resultado.

def celsius_para_fahrenheit(c):
    return c * 1.8 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9

def celsius_para_kelvin(c):
    return c + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

# Função principal: pergunta a conversão, chama a função certa e mostra o resultado.

def main():
    resposta = input("Entre quais temperaturas voce deseja fazer a conversao? C para F, F para C, C para K, K para C, F para K ou K para F? ").strip().upper()

    if resposta == "C PARA F":
        temperatura = float(input("Qual e a sua temperatura em Celsius? "))
        print(f"Sua temperatura em Fahrenheit e: {celsius_para_fahrenheit(temperatura):.2f}")

    elif resposta == "F PARA C":
        temperatura = float(input("Qual e a sua temperatura em Fahrenheit? "))
        print(f"Sua temperatura em Celsius e: {fahrenheit_para_celsius(temperatura):.2f}")

    elif resposta == "C PARA K":
        temperatura = float(input("Qual e a sua temperatura em Celsius? "))
        print(f"Sua temperatura em Kelvin e: {celsius_para_kelvin(temperatura):.2f}")

    elif resposta == "K PARA C":
        temperatura = float(input("Qual e a sua temperatura em Kelvin? "))
        print(f"Sua temperatura em Celsius e: {kelvin_para_celsius(temperatura):.2f}")

    elif resposta == "F PARA K":
        temperatura = float(input("Qual e a sua temperatura em Fahrenheit? "))
        print(f"Sua temperatura em Kelvin e: {fahrenheit_para_kelvin(temperatura):.2f}")

    elif resposta == "K PARA F":
        temperatura = float(input("Qual e a sua temperatura em Kelvin? "))
        print(f"Sua temperatura em Fahrenheit e: {kelvin_para_fahrenheit(temperatura):.2f}")

    else:
        print("Eita! A opcao digitada e invalida. Tente digitar exatamente como as opcoes sugeridas (ex: F para C).")

main()
