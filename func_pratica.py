def mediafinal ():
    a = int (input("Escreva a primeira nota "))
    b = int (input ("Escreva a segunda nota "))
    c = int (input ("Escreva a terceira nota "))

    media = (a + b + c) / 3

    print(media)

    if media < 9:
        print(f"Infelizmente vocês tá reprovado")
    else: 
        print(f"Parabéns você está aprovado")
mediafinal()