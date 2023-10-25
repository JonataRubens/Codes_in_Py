import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout= [
            [sg.Text('Nome'),sg.Input()]
            [sg.Text('idade'),sg.Input()]
            [sg.Button('Enviar dados')]
        ]
        #janela
        janela = sg.Window("Dados do Usuário").layout(layout)
        self.button, self.values = janela.Read()

    def Start(self):
        print(self.value)

tela = TelaPython
tela.Start
