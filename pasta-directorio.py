import PySimpleGUI as sg
caminho = sg.popup_get_file('Selecione um ficheiro do seu computador ' \
'e visualize onde está localizado')
print(caminho)