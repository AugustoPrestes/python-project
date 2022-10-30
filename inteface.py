# importando biblioteca 
import PySimpleGUI as sg  # modulo da interface grafica

"""
Sera necessario importar as funcoes criadas para gerar as senhas e os nomes, pois e necessario criar um objeto com a interface

"""
class PyProject:
    def __init__(self): # Criando o "gerador" da interface 
        sg.theme('Black') # Passando o tema da interface grafica

        # Passando as informacoes do layout da interface
        layout = [
            [sg.Text('Informe seu nome:', size=(30, 1)), sg.InputText(key='nome', size=(30, 1))],
            [sg.Text('Qual o tamanho da senha:', size=(20, 1)), sg.Combo(values=[8, 11, 15], key='qtd_caracter', default_value=8,size=(2, 1))],
            [sg.Text('Console do Gerador:')],
            [sg.Output(size=(60, 2))],
            [sg.Text('Logins Salvos:')],
            [sg.Output(size=(60, 10))],
            [sg.Button('Gerrar Login')]
        ]

        # Definido a janela que recebera o layout a cima

        self.janela = sg.Window('Python-Project', layout)


    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.Window_closed:
                break

project = PyProject()

project.Iniciar()
