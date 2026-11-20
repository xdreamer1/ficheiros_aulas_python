import PySimpleGUI as sg
for i in range(10000):
    sg.one_line_progress_meter(
        'barra_progresso',
        i + 1,
        10000,
        'isto é uma barra de progresso utilizando PySimpleGUI'
    )