#### modulo do coordenador pedagógico ####
####corpo do programa####
#### MENUS PARA CADASTRO DE PROFESSORES E ALUNOS #####

# menu de cadastro de professores # 

def menuCadastrarProfessor():
    dadosProfessor=[]
    turmaProfessor=[]
    import validarLogin
    print('-'*26)
    print('#### - CADASTRO DE PROFESSOR - ####')
    print('-'*26)
    print('Informe os dados do professor:')
    nomeProf = input('Nome completo: ')
    while True:
        print(' === OPCÕES DE DISCIPLINAS === ')
        print('1 - Portugues')
        print('2 - Matematica')
        print('3 - Geografia')
        print('4 - Historia')
        opcaoDisc = input('Disciplina: ') #PORTUGUES,MATEMATICA,GEOGRAGRAFIA, HISTORIA
        if opcaoDisc =='1':
            discProf = ('portugues')
            break
        elif opcaoDisc =='2':
              discProf = ('matematica')
              break
        elif  opcaoDisc =='3':
               discProf = ('geografia')
               break
        elif   opcaoDisc =='4':
                discProf = ('historia')
                break
        else:
            print('Opção inválida! Tente novamente')  
    userProf = input('Nome de usuário(login: "NOME.SOBRENOME"): ')
    senhaProf = input('Senha de usuário: ')
    import cadastro        
    cadastro.cadastrarProf(nomeProf,discProf,userProf,senhaProf)
    '''print('~ BANCO DE ANOS E TURMAS ~')
    print('--'*26)
    print('#### - CADASTRO DE PROFESSOR NA TURMA DE ALUNOS - """"')
    print('--'*26)
    print('1 - Primeiro ano A')
    print('2 - Primeiro ano B')
    print('3 - Primeiro ano C')
    print('4 - Segundo ano A')
    print('5 - Segundo ano B')
    print('6 - Segundo ano C')
    print('7 - Terceiro ano A')
    print('8 - Terceiro ano B')
    print('9 - Terceiro ano C')
    print('0 - Retornar ao menu anterior')
    continuarCadastroTurmaProf = 'sim'            
    while True:      
        while continuarCadastroTurmaProf == 'sim':
            print('Informe o ano e a turma a serem vinculados ao professor:')
            anoTurma = input('Opção nº: ')
            if anoTurma == '1':
                turmaProfessor.append('primeiroAnoA')                              
                desejaContinuarCadTurmaProf = input('Deseja adicionar mais uma turma ao professor? \n 1 - Sim  \n 2 - Não')
                while True:
                    if desejaContinuarCadTurmaProf == '1': 
                        break
                    elif desejaContinuarCadTurmaProf == '2':
                        continuarCadastroTurmaProf = 'nao'                                       
                        break  
                    else:
                        print('Opção inválida! Tente novamente')               
            elif anoTurma == '2':                                           
                turmaProfessor.append('primeiroAnoB')                              
                desejaContinuarCadTurmaProf = input('Deseja adicionar mais uma turma ao professor? \n 1 - Sim  \n 2 - Não')
                while True:
                    if desejaContinuarCadTurmaProf == '1': 
                        break
                    elif desejaContinuarCadTurmaProf == '2':
                        continuarCadastroTurmaProf = 'nao'                   
                        break  
                    else:
                        print('Opção inválida! Tente novamente')
            elif anoTurma == '3':
                turmaProfessor.append('primeiroAnoC')                              
                desejaContinuarCadTurmaProf = input('Deseja adicionar mais uma turma ao professor? \n 1 - Sim  \n 2 - Não')
                while True:
                    if desejaContinuarCadTurmaProf == '1': 
                        break
                    elif desejaContinuarCadTurmaProf == '2':
                        continuarCadastroTurmaProf = 'nao'                                           
                        break  
                    else:
                        print('Opção inválida! Tente novamente')                                                
            elif anoTurma == '4':
                turmaProfessor.append('segundoAnoA')                              
                desejaContinuarCadTurmaProf = input('Deseja adicionar mais uma turma ao professor? \n 1 - Sim  \n 2 - Não')
                while True:
                    if desejaContinuarCadTurmaProf == '1': 
                        break
                    elif desejaContinuarCadTurmaProf == '2':
                        continuarCadastroTurmaProf = 'nao'                                         
                        break  
                    else:
                        print('Opção inválida! Tente novamente')                                             
            elif anoTurma == '5':
                turmaProfessor.append('segundoAnoB')                              
                desejaContinuarCadTurmaProf = input('Deseja adicionar mais uma turma ao professor? \n 1 - Sim  \n 2 - Não')
                while True:
                    if desejaContinuarCadTurmaProf == '1': 
                        break
                    elif desejaContinuarCadTurmaProf == '2':
                        continuarCadastroTurmaProf = 'nao'                                      
                        break  
                    else:
                        print('Opção inválida! Tente novamente')                                                        
            elif anoTurma == '6':
                turmaProfessor.append('segundoAnoC')                              
                desejaContinuarCadTurmaProf = input('Deseja adicionar mais uma turma ao professor? \n 1 - Sim  \n 2 - Não')
                while True:
                    if desejaContinuarCadTurmaProf == '1': 
                        break
                    elif desejaContinuarCadTurmaProf == '2':
                        continuarCadastroTurmaProf = 'nao'                                          
                        break  
                    else:
                        print('Opção inválida! Tente novamente')                                              
            elif anoTurma == '7':
                turmaProfessor.append('terceiroAnoA')                              
                desejaContinuarCadTurmaProf = input('Deseja adicionar mais uma turma ao professor? \n 1 - Sim  \n 2 - Não')
                while True:
                    if desejaContinuarCadTurmaProf == '1': 
                        break
                    elif desejaContinuarCadTurmaProf == '2':
                        continuarCadastroTurmaProf = 'nao'                                  
                        break  
                    else:
                        print('Opção inválida! Tente novamente')
            elif anoTurma == '8':
                turmaProfessor.append('terceiroAnoB')                              
                desejaContinuarCadTurmaProf = input('Deseja adicionar mais uma turma ao professor? \n 1 - Sim  \n 2 - Não')
                while True:
                    if desejaContinuarCadTurmaProf == '1': 
                        break
                    elif desejaContinuarCadTurmaProf == '2':
                        continuarCadastroTurmaProf = 'nao'                   
                        break  
                    else:
                        print('Opção inválida! Tente novamente')                                               
            elif anoTurma == '9':
                turmaProfessor.append('terceiroAnoC')                              
                desejaContinuarCadTurmaProf = input('Deseja adicionar mais uma turma ao professor? \n 1 - Sim  \n 2 - Não')
                while True:
                    if desejaContinuarCadTurmaProf == '1': 
                        break
                    elif desejaContinuarCadTurmaProf == '2':
                        continuarCadastroTurmaProf = 'nao'                   
                        break  
                    else:
                        print('Opção inválida! Tente novamente')                                                   
            elif anoTurma == '0':
                break  
            else:
                print('Opção inválida! Tente novamente')      
        break'''
    print('O professor cadastrado com sucesso! \n Retornando ao menu principal')
    menuCoordenador()

#menu de cadastro de aluno#

def menuCadastrarAluno():
    import cadastro
    print('--'*26)
    print('#### - CADASTRO TURMA DE ALUNOS - """"')
    print('--'*26)
    print('Informe o ano e a turma a serem cadastrados:')
    print('1 - Primeiro ano A')
    print('2 - Primeiro ano B')
    print('3 - Primeiro ano C')
    print('4 - Segundo ano A')
    print('5 - Segundo ano B')
    print('6 - Segundo ano C')
    print('7 - Terceiro ano A')
    print('8 - Terceiro ano B')
    print('9 - Terceiro ano C')
    print('0 - Retornar ao menu anterior')     
    while True:
        anoTurma = input('Opção nº: ')
        if anoTurma == '1':
            cadastro.cadastrarPrimeiroAnoA()                                
            break
        elif anoTurma == '2':
            cadastro.cadastrarPrimeiroAnoB()                                
            break
        elif anoTurma == '3':
            cadastro.cadastrarPrimeiroAnoC()                                
            break
        elif anoTurma == '4':
            cadastro.cadastrarSegundoAnoA()                                
            break
        elif anoTurma == '5':
            cadastro.cadastrarSegundoAnoB()                                
            break
        elif anoTurma == '6':
            cadastro.cadastrarSegundoAnoC()                                
            break
        elif anoTurma == '7':
            cadastro.cadastrarTerceiroAnoA()                                
            break
        elif anoTurma == '8':
            cadastro.cadastrarTerceiroAnoB()                                
            break
        elif anoTurma == '9':
            cadastro.cadastrarTerceiroAnoC()                                
            break
        elif anoTurma == '0':
            menuCoordenador()
        else:
            print('Opção inválida! Tente novamente')                     


#menu principal da seção de estastíticas
def menuEstatisticasPrincipal():
    import estatisticas
    print('--'*26)
    print('#### - MENU DE ESTATÍSTICAS - """"')
    print('--'*26)
    print('Selecione a opção:')
    print('1 - Notas e situação de alunos(aprovados e reprovados)')
    print('2 - Professores cadastrados')
    print('9 - Retornar ao menu anterior')     
    while True:
        anoTurma = input('Opção nº: ')
        if anoTurma == '1':
            menuEstatisticasAlunos()                              
        elif anoTurma == '2':
            menuEstatisticasProfessor() 
        elif anoTurma == '9':
            menuCoordenador() 
        else:
            print('Opção inválida! Tente novamente')

#menu de estatíticas dos professores#
def menuEstatisticasProfessor():
    import estatisticas
    estatisticas.estatisticasProfessor()
    menuEstatisticasPrincipal()
#menu de estatísticas dos alunos#
def menuEstatisticasAlunos():
    import estatisticas
    print('--'*26)
    print('#### - ESTATÍSTICAS DAS TURMAS DE ALUNOS - """"')
    print('--'*26)
    print('Informe o ano e a turma a serem verificados:')
    print('1 - Primeiro ano A')
    print('2 - Primeiro ano B')
    print('3 - Primeiro ano C')
    print('4 - Segundo ano A')
    print('5 - Segundo ano B')
    print('6 - Segundo ano C')
    print('7 - Terceiro ano A')
    print('8 - Terceiro ano B')
    print('9 - Terceiro ano C')
    print('0 - Retornar ao menu anterior')     
    while True:
        anoTurma = input('Opção nº: ')
        if anoTurma == '1':
            estatisticas.estatisticasPrimeiroAnoA()                              
            break
        elif anoTurma == '2':
            estatisticas.estatisticasPrimeiroAnoB() 
            break
        elif anoTurma == '3':
            estatisticas.estatisticasPrimeiroAnoC()                                 
            break
        elif anoTurma == '4':
            estatisticas.estatisticasSegundoAnoA()                                 
            break
        elif anoTurma == '5':
            estatisticas.estatisticasSegundoAnoB()                                 
            break
        elif anoTurma == '6':
            estatisticas.estatisticasSegundoAnoC()                                 
            break
        elif anoTurma == '7':
            cestatisticas.estatisticasTerceiroAnoA()                                 
            break
        elif anoTurma == '8':
            estatisticas.estatisticasTerceiroAnoA()                                 
            break
        elif anoTurma == '9':
            estatisticas.estatisticasTerceiroAnoC()                                 
            break
        elif anoTurma == '0':
            menuCoordenador() 
        else:
            print('Opção inválida! Tente novamente')  


# menu de opções disponíveis ao coordenador pedagógico #
def menuCoordenador():

    print('--'*26)
    print('#### - MENU COORDENADOR PEDAGÓGICO - #####')
    print('--'*26)
    print('Opções disponíveis:')
    print('1 - Cadastrar professor')
    print('2 - Cadastrar aluno')
    print('3 - Exibir estatísticas')
    print('9 - Retornar ao menu principal')
    opcaoMenuCoord = input('Opção n°: ')
    while True:
        if opcaoMenuCoord == '1':
            menuCadastrarProfessor()
        elif opcaoMenuCoord == '2':
            menuCadastrarAluno()
        elif opcaoMenuCoord == '3':
            menuEstatisticasPrincipal()
        elif opcaoMenuCoord == '9':
            import principal
            principal.menuPrincipal()
        else:
            print('Opção inválida! Tente novamente')                     


    
  
