def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    #salva carro no BD
    print (modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", "1999", "ABC-1234", marca="FIAT", motor="1.0", combustivel="Gasolina")
