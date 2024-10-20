def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


def func_3():
    print("Olá mundo!")
    # se não colocar o return, por padrão ele retorna Nome como se a linha abaixo existisse.
    return None


print (calcular_total([10, 20, 34]))
print (retorna_antecessor_e_sucessor(10))
print(func_3())