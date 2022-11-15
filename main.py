import re
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')

def CalcularIMC(alturaEmCentimetros, peso):
    alturaEmMetros = alturaEmCentimetros/100
    imc = peso / alturaEmMetros ** 2
    return "%.2f" % imc

def InformarSituacao(imc):
    if imc < 17:
        return "Muito abaixo do peso"
    if imc >= 17 and imc <= 18.49:
        return "Abaixo do peso"
    if imc >= 18.50 and imc <= 24.99:
        return "Peso normal"
    if imc >= 25 and imc <= 29.99:
        return "Acima do peso"
    if imc >= 30 and imc <= 34.99:
        return "Obesidade I"
    if imc >= 35 and imc <= 39.99:
        return "Obesidade II (severa)"

    return "Obesidade III (mórbida)"

def Reiniciar():
    for key in valores:
        janela[key].update('')

column1 = [
    [
        sg.Text('Altura (cm)', size=(15,0)),
        sg.Input(key='altura', size=(15,1))
    ],
    [
        sg.Text('Peso (kg)', size=(15, 0)),
        sg.Input(key='peso', size=(15, 1))
    ],
]
column2 = [
    [
        sg.Multiline(key='resultado', size=(62, 5))
    ]
]

layout = [
    [
        sg.Text('Nome do Paciente:', size=(15, 0)),
        sg.Input(key='nome', size=(62, 0))
    ],
    [
        sg.Text('Endereço Completo:', size=(15, 0)),
        sg.Input(key='endereco', size=(62, 0))
    ],
    [
        sg.Column(column1, vertical_alignment='top', pad=(0, 0)),
        sg.Column(column2, vertical_alignment='top', pad=(0, 0))
    ],
    [
        sg.Column(layout=[], pad=(60,0)),
        sg.Button('Calcular', size=(10,0)),
        sg.Button('Reiniciar', size=(10,5)),
        sg.Column(layout=[], pad=(40,0)),
        sg.Button('Sair', size=(10,0))
    ],
]

janela = sg.Window('Cálculo do IMC - indice de Massa Corporal', layout, size=(500, 180))

caracteresPermitidos = '^[0-9\.]+$'

#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED or eventos == "Sair":
        break

    if eventos == "Calcular" and re.search(caracteresPermitidos, valores['altura']) and re.search(caracteresPermitidos, valores['peso']):
        resultado = CalcularIMC(float(valores['altura']), float(valores['peso']))
        situacao = InformarSituacao(float(resultado))
        janela['resultado'].update(f"{valores['nome']} seu IMC é: {resultado}\nSua situação é: {situacao}")

    if eventos == "Reiniciar":
        Reiniciar()

janela.close()
