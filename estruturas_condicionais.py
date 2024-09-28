# if, elif, else

MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe a sua idade: "))

if idade < IDADE_ESPECIAL:
        print ("Você não pode votar.")
elif IDADE_ESPECIAL <= idade < MAIOR_IDADE or idade > 70:
        print ("Voto facultativo.")
elif MAIOR_IDADE <= idade <= 70:
        print ( "Voto obrigatório.")
else:
         print ( "Idade inválida.")
