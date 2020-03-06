#Universidade Federal do Maranhão
#Projeto final fundamentos de Computação
# Valdimir Barros
# Maria Vitória
# João Yuri
#seção de importação de bibliotecas e módulos

####principal.py####

import sys #bibliotecas do sistema
import validarLogin #modulo de validação de acesso ao programa
import bancodeDados #modulo do banco de dados
####escopo de funcoes do programa principal####

#funcao para criar o banco de dados do sistema(tabelas)
#bancodeDados.criarBancodeDados()
#funcao de requisição de login e senha ao usuário
def login():
    login = input("Digite o login: ")
    senha = input("Digite sua senha: ")   
    validarLogin.validarLoginUsuario(login, senha)

    
#funcao de menu principal
def menuPrincipal():
    print('--'*26)
    print(' ####- MENU PRINCIPAL -#### ')
    print('--'*26)
    print('Entre com o número de uma opção abaixo: ')
    while True:
        print('1 - Entrar no sistema')
        print('9 - Sair do sistema')
        opcao = input('Opção n°: ')
        if opcao == '1':
            login()
            break
        elif opcao == '9':
            sys.exit()
        else:
            print("Erro!!! você digitou algo fora do sistema!")

####corpo do programa principal####
print('-='*26)
print(' #######- BEM VINDO AO SISTEMA HARVARD - #######')
print('-='*26)
menuPrincipal()
        
