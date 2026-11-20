
emails_concelhos = {
    "Lisboa": "lisboa@kmail.com",
    "Porto": "porto@kmail.com",
    "Faro": "faro@kmail.com",
}

"""Consultar - Quero saber o email do Porto"""

email = emails_concelhos["Faro"]
print(email)

"""Adicionar / modificar email de um novo concelho"""

emails_concelhos["Braga"] = "braga1@kmail.com"
print(emails_concelhos)

"""Mostrar nomes dos concelhos (chaves)"""

print(emails_concelhos.keys())

for concelho in emails_concelhos:
  email = emails_concelhos[concelho]
  print(email)

"""Remover / Eliminar entrada no dicionário"""

emails_concelhos.pop("Faro")
print(emails_concelhos)

"""Verificar se existe"""

if "leiria" in emails_concelhos:
  print("Existe")
else:
  print("Não existe")

"""Verificar se os valores existem"""

if "lisboa2@kmail.com" in emails_concelhos.values():
  print("Existe")
else:
  print("Não existe")