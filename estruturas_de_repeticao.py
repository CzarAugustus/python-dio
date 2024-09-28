# for e while

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando a estrutura de repetição for para iterar sobre a lista
for numero in numeros:
    print(f"Usando for: {numero}")

# Inicializando o contador
contador = 0

# Usando a estrutura de repetição while
while contador < len(numeros):
    print(f"Usando while: {numeros[contador]}")
    contador += 1


texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print() # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
