import PySimpleGUI as sg
text = sg.popup_get_text('Palavra-passe', password_char='*')
sg.popup(f'Palavra-passe:{text}')