#### módulo do professor ####
def menuProfessor():
    print('#### - MENU PROFESSOR - ####')
    while True:
        print('Opções disponíveis:')
        print('1 - Cadastrar notas de alunos(a)')
        print('9 - Retornar ao menu principal')
        opcaoMenuProf = input('Opção n°: ')
        if opcaoMenuProf == '1':
            menuCadastroNotas()
        elif opcaoMenuProf == '9':
            import principal
            principal.menuPrincipal()
        else:
            print('Opção inválida!')    

### funcao de menu de cadastro de notas de alunos ###
def menuCadastroNotas():
    import cadastro
    print('--'*26)
    print('#### - CADASTRO DAS NOTAS NAS TURMAS DOS ALUNOS - """"')
    print('--'*26)
    print('Informe o ano e a turma a serem cadastrados as notas:')
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
            cadastro.cadastrarNotasAlunosPrimeiroAnoA()                                
            break
        elif anoTurma == '2':
            cadastro.cadastrarNotasAlunosPrimeiroAnoB()                                
            break
        elif anoTurma == '3':
            cadastro.cadastrarNotasAlunosPrimeiroAnoC()                                
            break
        elif anoTurma == '4':
            cadastro.cadastrarNotasAlunosSegundoAnoA()                                
            break
        elif anoTurma == '5':
            cadastro.cadastrarNotasAlunosSegundoAnoB()                                
            break
        elif anoTurma == '6':
            cadastro.cadastrarNotasAlunosSegundoAnoC()                                
            break
        elif anoTurma == '7':
            cadastro.cadastrarNotasAlunosTerceiroAnoA()                                
            break
        elif anoTurma == '8':
            cadastro.cadastrarNotasAlunosTerceiroAnoB()                                
            break
        elif anoTurma == '9':
            cadastro.cadastrarNotasAlunosTerceiroAnoC()                                
            break
        elif anoTurma == '0':
            menuProfessor()
        else:
            print('Opção inválida! Tente novamente')


    
