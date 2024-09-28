# if, elif, else, dentro de if, elif, else

# Ex.: Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Verifica se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print("E é um número par.")
    else:
        print("E é um número ímpar.")
elif numero < 0:
    print("O número é negativo.")
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print("E é um número par.")
    else:
        print("E é um número ímpar.")
else:
    print("O número é zero.")
