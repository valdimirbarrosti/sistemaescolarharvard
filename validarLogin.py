####validaLogin.py####
import sys #bibliotecas do sistema
contasCord =[['jose.renato' , 'jose123']]
boasVindas = 'Seja bem vindo(a)!\nVocê está logado como: {}'
### funcao que valida o login e senha no banco de dados SQLite3 ###
def validarLoginUsuario(login, senha):             
    contaProfessorExistente = 'nao'
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlValidarProfessor = "SELECT rowid,* FROM professor WHERE usuario=? and senha=?" #comando de consulta se o usuario e senha existem no banco de dados
    for row in interagir.execute(sqlValidarProfessor,[login,senha]): #varre a tabela professor em busca de login e senha igual ao que foi informado na função
        contaProfessorExistente = 'sim'
    for contCord in range(len(contasCord)): #varre a lista de contas de coordenadores ( ATUALIZAR PARA O BD)
        if contasCord[contCord][0] == login and contasCord[contCord][1] == senha:
            print(boasVindas.format(login))            
            print('Cargo: COORDENADOR PEDAGÓGICO') 
            contaInexistente1 = 'nao'
            import coordenadorPedagogico
            coordenadorPedagogico.menuCoordenador()
            break
        else:
            contaInexistente1 = 'sim'
    if contaProfessorExistente == 'sim':            
        print(boasVindas.format(login))
        print('Cargo: PROFESSOR')
        contaInexistente2 = 'nao'
        import professor
        professor.menuProfessor()
    else:
        contaInexistente2 = 'sim'  
    if contaInexistente1 == 'sim' and contaInexistente2 == 'sim':
        print('Usuário e/ou senha incorreto(s)')
        while True:       
            print('1 - Tentar novamente')
            print('9 - Retornar ao menu principal')
            perguntaRepetirLogin = input('Opção n°: ')
            if perguntaRepetirLogin == '1':
                login = input('Digite o login: ')
                senha = input('Digite a sua senha: ')
                validarLoginUsuario(login ,senha)
                break
            elif perguntaRepetirLogin == '9':
                import principal
                principal.menuPrincipal()
                break
            else:
                print("Opcao inválida! Digite um dos números abaixo: ")    
    def nomeLogin():
        return login                   
                        
                    
                     
            
