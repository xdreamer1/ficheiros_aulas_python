import PySimpleGUI as sg

path = sg.popup_get_file("Selecione um ficheiro")

print(path)