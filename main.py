# importando biblioteca
import random 

# Recebendo os dados do usuario.
nome = input("Informe o seu nome: ")
site = input("Informe o nome do site: ")
caracters = int(input("Informe a quantidade de caracteres da senha: "))


# Gerando a senha com as informacoes passadas pelo usuario
def Gerar_senha(qtd_caracter):
    banco_caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*'
    senha = random.choices(banco_caracteres, k=qtd_caracter)
    nova_senha = ''.join(senha)
    return nova_senha

# Gerando a senha com as informacoes passadas pelo usuario
def Gerar_nick(nome_user):
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

    if nome == '':
        print("Preencha todos os campos para gerar seu nick name!")
    else:    
        new_nome = nome_user + letra7 + letra8 + letra9 + letra10
        return new_nome


# Função para salvar as senhas e os logins
def Salvar_Senha(nova_senha, site, nick):
    if site == '' or nome == '':
        print("Preencha todos os campos para gerar sua nova senha!")

    else:
        with open('Senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"\nSenha Salva para o Site: {site}, com o usuario: {nick}, com a senha: {nova_senha}\n")
        print(f"Nick Criado: {nick}, senha criada: {nova_senha}, site: {site} no arquivo Senhas.txt")



# Salvando a senha gerada em uma nova variavel.
senha_gerada = Gerar_senha(caracters)

# Salvando o nick name gerado em uma nova variavel.
nick_gerado = Gerar_nick(nome)

# Salvando as informações geradas em um arquivo .txt.
Salvar_Senha(senha_gerada, site, nick_gerado)