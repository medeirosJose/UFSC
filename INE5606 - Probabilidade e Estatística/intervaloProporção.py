import PySimpleGUI as sg
import math

def intervalo_confianca_proporcao(proporcao_amostra, tamanho_amostra, nivel_confianca):
    valor_critico_z = 0.0

    if nivel_confianca == 0.90:
        valor_critico_z = 1.645
    elif nivel_confianca == 0.92:
        valor_critico_z = 1.75
    elif nivel_confianca == 0.95:
        valor_critico_z = 1.96
    elif nivel_confianca == 0.96:
        valor_critico_z = 2.054
    elif nivel_confianca == 0.99:
        valor_critico_z = 2.576
    else:
        raise ValueError("Nível de confiança inválido. Os valores aceitos são 0.90, 0.95, 0.96 ou 0.99.")

    erro_padrao = valor_critico_z * math.sqrt((proporcao_amostra * (1 - proporcao_amostra)) / tamanho_amostra)
    intervalo_inferior = proporcao_amostra - erro_padrao
    intervalo_superior = proporcao_amostra + erro_padrao

    return intervalo_inferior, intervalo_superior

# Layout da GUI
layout = [  [sg.Text("Digite a proporção amostral: "), sg.Input(key='-PROP-')],
            [sg.Text("Digite o tamanho da amostra: "), sg.Input(key='-TAM-')],
            [sg.Text("Escolha o nível de confiança: ")],
            [sg.Radio('0.90', "RADIO1", key='-RADIO-.90-', default=True), 
             sg.Radio('0.92', "RADIO1", key='-RADIO-.92-'), 
             sg.Radio('0.95', "RADIO1", key='-RADIO-.95-'), 
             sg.Radio('0.96', "RADIO1", key='-RADIO-.96-'), 
             sg.Radio('0.99', "RADIO1", key='-RADIO-.99-')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Criar a janela
window = sg.Window('Intervalo de Confiança', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        try:
            proporcao_amostra = float(values['-PROP-'])
            tamanho_amostra = int(values['-TAM-'])
            nivel_confianca = [0.90, 0.92, 0.95, 0.96, 0.99][list(values[key] for key in ['-RADIO-.90-', '-RADIO-.92-', '-RADIO-.95-', '-RADIO-.96-', '-RADIO-.99-']).index(True)]
            intervalo_inferior, intervalo_superior = intervalo_confianca_proporcao(proporcao_amostra, tamanho_amostra, nivel_confianca)
            sg.popup(f'IC(p) {nivel_confianca*100:.0f}%:  {intervalo_inferior:.4f} - {intervalo_superior:.4f}', title = 'Resultado')
        except ValueError as e:
            sg.popup('Erro: ' + str(e))
        except Exception as e:
            sg.popup('Erro desconhecido: ' + str(e))

window.close()
