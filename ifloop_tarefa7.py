compositores = ["mozart", "beethoven", "bach", "handel", "vivaldi"]

compositores_digitados = input("Escreva um nome de um compositor:").lower()

if compositores_digitados in compositores:
    print(f"O compositor {compositores_digitados} está na lista.")

else:
    print(f"O compositor {compositores_digitados} não está na lista.")