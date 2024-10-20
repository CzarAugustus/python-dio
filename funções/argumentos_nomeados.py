def salvar_carro(marca, modelo, ano, placa):
    #salva carro no BD
    print (f"Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}")

#FORMAS DE PASSAR
salvar_carro("fiat", "Palio", "1999", "ABC-1234")
salvar_carro(marca="Renault", modelo="Sandero", ano="1999", placa="ABC-5678")
salvar_carro(**{"marca": "volkswagen", "modelo": "Polo", "ano": "1999", "placa": "DFG-1234"})