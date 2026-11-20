import io

with io.open('emails.txt', 'r') as t:
    texto = t.read()
    print(texto)