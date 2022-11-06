# importando biblioteca
import PySimpleGUI as sg  # modulo da interface grafica
import random 
# from functions import Gerar_senha # funcao para gerrar a senha aleatoria

"""
Sera necessario importar as funcoes criadas para gerar as senhas e os nomes, pois e necessario criar um objeto com a interface

"""
class PyProject:
    def __init__(self): # Criando o "gerador" da interface 
        sg.theme('Black') # Passando o tema da interface grafica

        # Passando as informacoes do layout da interface
        layout = [
            [sg.Text('Informe seu nome:', size=(20, 1)), sg.InputText(key='nome', size=(35, 1))],
            [sg.Text('Informe o site do login:', size=(20, 1)), sg.InputText(key='site', size=(35, 1))],
            [sg.Text('Qual o tamanho da senha:', size=(20, 1)), sg.Combo(values=[8, 11, 15], key='qtd_caracter', default_value=8, size=(2, 1))],
            [sg.Text('Console do Gerador:')],
            [sg.Output(size=(60, 2))],
            [sg.Text('Logins Salvos:')],
            [sg.Output(size=(60, 10))],
            [sg.Button('Gerrar Login')]
        ]

        # Definido a janela que recebera o layout a cima

        self.janela = sg.Window('Python-Project', layout)

  
    # Iniciando as funcoes do algoritmo
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerrar Login':
                nova_senha = self.Gerar_senha(valores)
                nick = self.Gerar_nick(valores)
                email = self.Gerar_email(valores)
                self.Salvar_Senha(nova_senha, email, nick, valores)


    # Gerando a senha com as informacoes passadas pelo usuario
    def Gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'
        chars = random.choices(char_list, k=int(valores['qtd_caracter']))
        new_pass = ''.join(chars)
        return new_pass


    # Gerando a senha com as informacoes passadas pelo usuario
    def Gerar_nick(self, valores):
        #lista1 = ['b' ,'c' ,'d' ,'f' ,'g' ,'h' ,'j' ,'k' ,'l' ,'m' ,'n' ,'p' ,'r' ,'s' ,'t' ,'v' ,'x']
        #lista2 = ['a' ,'e' ,'i' ,'o' ,'u']
        lista3 = ['@' ,'#' ,'$' ,'%' ,'&' ,'*']
        lista4 = ['1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9']

    #-- Randomizando os caracteres      
        #letra1 = random.choice(lista1)
        #letra2 = random.choice(lista2)    
        #letra3 = random.choice(lista1)
        #letra4 = random.choice(lista2)
        #letra5 = random.choice(lista1)
        #letra6 = random.choice(lista2)
        letra7 = random.choice(lista3)
        letra8 = random.choice(lista4)
        letra9 = random.choice(lista4)
        letra10 = random.choice(lista4)

        if valores['nome'] == '':
            print("Preencha todos os campos para gerar seu nick name!")
        else:    
            new_nome = valores['nome'] + letra7 + letra8 + letra9 + letra10
            return new_nome

    def Salvar_Senha(self, nova_senha, email, nick, valores):
        if valores['site'] == '' or valores['nome'] == '':
            print("Preencha todos os campos para gerar sua nova senha!")

        else:
            with open('Senhas.txt', 'a', newline='') as arquivo:
                arquivo.write(f"Senha Salva para o Site: {valores['site']}, com o usuario: {nick}, com a senha: {nova_senha}\n")
            print(f"Nick Criado: {nick}, E-mail geradp {email},senha Craida: {nova_senha}")
            print("Arquivo salvo com Sucesso em Senhas.txt")


project = PyProject()
project.Iniciar()
