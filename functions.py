
import random as rd

# Funcao para gerar as senha aleatorias
def Gerar_senha(quantidade):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*<>|?'
    chars_list= rd.choices(char_list, k=quantidade) 
    senha = ''.join(chars)
    return senha

