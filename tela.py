import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        Layout = [
        [sg.Text('País'),sg.Input()],
        [sg.Text('Capital'),sg.Input()],
        [sg.Button('Enviar Dados do País')]
        ]

        #Janela
        janela = sg.Window("Dados do País").layout(Layout)

        #Extrair os dados da Tela
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        print(self.values)


tela = TelaPython()
tela.Iniciar()
