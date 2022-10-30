# Importando bibliotecas
import functions as ft

# Variaveis globais do sistema


# Quantidade de caracteres que a senha possuira
tamanho_senha = {8, 15, 30}

# Recebendo valores do usuario # 


try: # Tentando receber o nome do usuario
    nome = input('Informe seu nome para a criação de um usuário: ')

except TypeError as err:
    print(f"Ocorreu um erro com o nome informado: {err}")

else:
    # Passando as instrucoes para o usuario escolher o tamanho da senha
    print("|-------------------------------------------------------|")
    print("|-------------------------------------------------------|")
    print("| Informe dentro das opções a quantidade de caracteres  |")
    print("| que você queira em sua senha:                         |")
    print("| 8 - Para uma senha Pequena;                           |")
    print("| 15 - Para uma senha Média;                            |")
    print("| 30 - Para uma senha Grande;                           |")
    print("|-------------------------------------------------------|")
    print("|-------------------------------------------------------|")

    
try: # Tentando Receber o tamanho da senha
    tm_senha = int(input("Digite o numero: "))

except ValueError as err:
    print(f"Ocorreu um erro com o valor informado: {err}")

else:
    # Tratamento dos dados recebidos
    if tm_senha not in tamanho_senha:
        print("Numero invalido informe um numero conforme o informado (8, 15 ou 30)")


# Chamando as Funções