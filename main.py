import PySimpleGUI as sg
from CalcRoot import calc_root as cr

sg.theme('DarkPurple6')

layout = [
    [sg.Text('Root Calculator')],
    [],
    [sg.Text('Insert Index')],
    [sg.InputText(key='-index-')],
    [],
    [sg.Text('Insert Radicand')],
    [sg.InputText(key='-radicand-')],
    [],
    [sg.Button('Calculate', key='-calculate-')],
    [],
    [sg.Text('', key='-root-')]
]

window = sg.Window('Root Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    index = values['-index-']
    radicand = values['-radicand-']

    if event == '-calculate-':
        if index.isdigit() and radicand.isdigit() :
            index = int(index)
            radicand = int(radicand)
            root = cr(radicand, index)
            window['-root-'].update(f'The root of radicand "{radicand}" with the index "{index}" is "{root}"')
        else:
            window['-root-'].update(f'Please insert an integer number')