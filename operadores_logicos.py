# AND = para ser True, tudo tem de ser True
# or = para ser True, pelo menos um tem de ser True

print (True and True)
print (True and False)
print (False and False)
print (True or True)
print (True or False)
print (False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp2)


conta_normal_saldo_suficiente = (saldo >= saque and saque <= limite)  
conta_especial_saldo_suficiente = (conta_especial and saldo >= saque)

exp3 = conta_normal_saldo_suficiente or conta_especial_saldo_suficiente
print(exp3)


