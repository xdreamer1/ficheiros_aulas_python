"""Tarefa 1"""
informacoes_pessoa = {
    "nome": "Conceição",
    "idade": "65",
    "local de nascimento": "estoril",
    "função": "empregada doméstica",
}

"""Tarefa 2"""
nome = informacoes_pessoa["nome"]
idade = informacoes_pessoa["idade"]
print(nome)
print(idade)
"""também tinha criado este código e resultou print(informacoes_pessoa["nome"])"""

"""Tarefa 3"""
informacoes_pessoa["função"] = "cozinheira"
print(informacoes_pessoa)

"""Tarefa 4"""
informacoes_pessoa["email"] = "maria@kmail.com"
informacoes_pessoa["contacto telefónico"] = "568949257"

"""Tarefa 5"""
informacoes_pessoa.pop("função")
print(informacoes_pessoa)

"""Tarefa 6"""

print("Por favor, introduza um nome de um amigo.")
nome = input()
if nome in informacoes_pessoa.values():
    print("Existe")
else:
    print("Não existe")
