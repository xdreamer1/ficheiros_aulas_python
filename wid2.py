import tkinter as tk

janela = tk.Tk()
janela.title("Sistema Pack")

tk.Button(janela, text="Topo").pack(side="top", fill="x")
tk.Button(janela, text="Esquerda").pack(side="left", fill="y")
tk.Button(janela, text="Direita").pack(side="right", fill="y")
tk.Button(janela, text="Fundo").pack(side="bottom", fill="x")

janela.mainloop()