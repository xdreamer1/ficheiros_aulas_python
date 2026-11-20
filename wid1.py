import tkinter as tk #Importa a biblioteca Tkinter, que permite criar janelas e interfaces

janela = tk.Tk() # Cria a janela principal da aplicação

label = tk.Label(janela, text="Olá Mundo") # Cria um texto com a mensagem "Olá Mundo."

label.pack() # Posiciona e apresenta o texto na janela

janela.mainloop() # Mantém a janela aberta e ativa, permitindo a interação do utilizador