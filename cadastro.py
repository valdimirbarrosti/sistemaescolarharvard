
## funcao para cadastrar professor no banco de dados ##
def cadastrarProf(nomeProf,discProf,userProf,senhaProf): 
   import sqlite3
   conectar = sqlite3.connect("bancodeDados.db") 
   interagir = conectar.cursor()
   sqlInserir = "INSERT INTO professor VALUES ('{}','{}','{}','{}')".format(nomeProf,discProf,userProf,senhaProf) #variavel que recebe o comando SQL para ser manipulado pelo metodo execute abaixo
   interagir.execute(sqlInserir)       
   conectar.commit()
'''
    Assume-se que cada lista alunoDados conterá 5 elementos:
        elemento nº 1: NOME DO ALUNO
        elemento nº 2: LISTA DE NOTAS DE PORTUGUES
        elemento nº 3: LISTA DE NOTAS DE MATEMÁTICA
        elemento nº 4: LISTA DE NOTAS DE GEOGRAFIA
        elemento nº 5: LISTA DE NOTAS DE HISTÓRIA
    Assume-se que a lista anoTurma conterá as listas alunoDados sendo adicionadas
    em cada loop e no final será salva no seu respectivo anoTurma.txt.   
'''
### funcões que vão salvar as notas dos alunos no banco de dados SQLlite3 do sistema ###    
def cadastrarNotasAlunosPrimeiroAnoA(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM primeiroanoa ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE primeiroanoa SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoa SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoa SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoa SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...") 

def cadastrarNotasAlunosPrimeiroAnoB(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM primeiroanob ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE primeiroanob SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanob SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanob SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanob SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...") 

def cadastrarNotasAlunosPrimeiroAnoC(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM primeiroanoc ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE primeiroanoc SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoc SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoc SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoc SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...") 

def cadastrarNotasAlunosSegundoAnoA(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM segundoanoa ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE segundoanoa SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE segundoanoa SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE segundoanoa SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE segundoanoa SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...") 
        
 def cadastrarNotasAlunosPrimeiroAnoA(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM primeiroanoa ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE primeiroanoa SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoa SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoa SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoa SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...")            
            
def cadastrarNotasAlunosSegundoAnoB(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM segundoanob ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE segundoanob SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE segundoanob SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE segundoanob SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE segundoanob SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...")         
 
 def cadastrarNotasAlunosPrimeiroAnoA(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM primeiroanoa ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE primeiroanoa SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoa SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoa SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE primeiroanoa SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...") 

def cadastrarNotasAlunosTerceiroAnoA(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM terceiroanoa ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE terceiroanoa SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE terceiroanoa SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE terceiroanoa SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE terceiroanoa SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...") 

def cadastrarNotasAlunosTerceiroAnoB(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM terceiroanob ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE terceiroanob SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE terceiroanob SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE terceiroanob SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE terceiroanob SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...")    

def cadastrarNotasAlunosTerceiroAnoC(): 
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    sqlSelecionarDisciplina ="SELECT disciplina FROM professor WHERE usuario='alex.barradas'"
    for row in interagir.execute(sqlSelecionarDisciplina):
        discProf = str(row[0])
        print(discProf)    
    interagir.execute("SELECT nomealuno FROM terceiroanoc ORDER BY nomealuno")
    if discProf == 'portugues':
        print('Cadastre suas notas referentes a disciplina de português:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Prt = float(input("1ª nota de Português: "))
            n2Prt = float(input("2ª nota de Português: "))
            n3Prt = float(input("3ª nota de Português: "))
            n4Prt = float(input("4ª nota de Português: "))
            mediaPrt = (n1Prt+n2Prt+n3Prt+n4Prt)/4
            if mediaPrt>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'    
            interagir.execute("UPDATE terceiroanoc SET nota1prt={}, nota2prt={}, nota3prt={}, nota4prt={}, mediaprt={}, situacaoprt='{}' WHERE nomealuno='{}'".format(n1Prt,n2Prt,n3Prt,n4Prt, mediaPrt, situacaoDisc, nomeAluno[0], ))
        conectar.commit()
    if discProf == 'matematica':
        print('Cadastre suas notas referentes a disciplina de matemática:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Mtm = float(input("1ª nota de Matemática: "))
            n2Mtm = float(input("2ª nota de Matemática: "))
            n3Mtm = float(input("3ª nota de Matemática: "))
            n4Mtm = float(input("4ª nota de Matemática: "))
            mediaMtm = (n1Mtm+n2Mtm+n3Mtm+n4Mtm)/4
            if mediaMtm>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE terceiroanoc SET nota1mtm={}, nota2mtm={}, nota3mtm={}, nota4mtm={}, mediamtm={}, situacaomtm='{}' WHERE nomealuno='{}'".format(n1Mtm,n2Mtm,n3Mtm,n4Mtm, mediaMtm, situacaoDisc, nomeAluno[0]))   
    if discProf == 'geografia':
        print('Cadastre suas notas referentes a disciplina de geografia:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Geo = float(input("1ª nota de Geografia: "))  
            n2Geo = float(input("2ª nota de Geografia: "))
            n3Geo = float(input("3ª nota de Geografia: "))
            n4Geo = float(input("4ª nota de Geografia: "))
            mediaGeo = (n1Geo+n2Geo+n3Geo+n4Geo)/4
            if mediaGeo>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE terceiroanoc SET nota1geo={}, nota2geo={}, nota3geo={}, nota4geo={}, mediageo={}, situacaogeo='{}' WHERE nomealuno='{}'".format(n1Geo,n2Geo,n3Geo,n4Geo, mediaGeo, situacaoDisc, nomeAluno[0]))
    if discProf == 'historia':
        print('Cadastre suas notas referentes a disciplina de história:')
        for nomeAluno in interagir.fetchall():
            print("Aluno: {}".format(nomeAluno[0]))               
            n1Hst = float(input("1ª nota de História: "))
            n2Hst = float(input("2ª nota de História: "))
            n3Hst = float(input("3ª nota de História: "))
            n4Hst = float(input("4ª nota de História: "))
            mediaHst = (n1Hst+n2Hst+n3Hst+n4Hst)/4
            if mediaHst>=7:
                situacaoDisc = 'APROVADO'
            else:
                situacaoDisc = 'REPROVADO'
            interagir.execute("UPDATE terceiroanoc SET nota1hst={}, nota2hst={}, nota3hst={}, nota4hst={}, mediahst={}, situacaohst WHERE nomealuno='{}'".format(n1Hst,n2Hst,n3Hst,n4Hst, mediaHst, situacaoDisc, nomeAluno[0]))     
    conectar.commit()
    print('As notas foram cadastradas com sucesso!')      
    print("Retornando ao menu anterior...")  

### funções que vão salvar os nomes dos alunos(tarefa do coordenador) no banco de dados SQLlite3 do sistema ###

def cadastrarPrimeiroAnoA():
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    quantidadeAlunos = int(input('Informe quantidade de alunos a serem cadastrados na turma: '))
    turma = 'primeiro ano turma A'
    for contador in range(0,quantidadeAlunos):
        nomeAluno = input("Informe o nome completo do aluno(a): ")      
        sqlCadastroNomeAluno = "INSERT INTO primeiroanoa(nomealuno) VALUES ('{}')".format(nomeAluno)
        interagir.execute(sqlCadastroNomeAluno)
        print("Aluno(a) {} cadastrado com sucesso no {}!".format(nomeAluno,turma))      
    print("Os alunos foram cadastrados com sucesso! \nlista de alunos cadastrados no {}".format(turma))
    conectar.commit()
    import coordenadorPedagogico
    coordenadorPedagogico.menuCoordenador()

def cadastrarPrimeiroAnoB():
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    quantidadeAlunos = int(input('Informe quantidade de alunos presentes na turma: '))
    turma = 'primeiro ano turma B'
    for contador in range(0,quantidadeAlunos):
        nomeAluno = input("nome do aluno: ")      
        sqlCadastroNomeAluno = "INSERT INTO primeiroanob(nomealuno) VALUES ('{}')".format(nomeAluno)
        interagir.execute(sqlCadastroNomeAluno)
        print("Aluno(a) {} cadastrado com sucesso no {}!".format(nomeAluno,turma))      
    print("Os alunos foram cadastrados com sucesso! \nlista de alunos cadastrados no {}".format(turma))
    conectar.commit()
    import coordenadorPedagogico
    coordenadorPedagogico.menuCoordenador()

def cadastrarPrimeiroAnoC():
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    quantidadeAlunos = int(input('Informe quantidade de alunos presentes na turma: '))
    turma = 'primeiro ano turma C'
    for contador in range(0,quantidadeAlunos):
        nomeAluno = input("nome do aluno: ")      
        sqlCadastroNomeAluno = "INSERT INTO primeiroanoc(nomealuno) VALUES ('{}')".format(nomeAluno)
        interagir.execute(sqlCadastroNomeAluno)
        print("Aluno(a) {} cadastrado com sucesso no {}!".format(nomeAluno,turma))      
    print("Os alunos foram cadastrados com sucesso! \nlista de alunos cadastrados no {}".format(turma))
    conectar.commit()
    import coordenadorPedagogico
    coordenadorPedagogico.menuCoordenador()

def cadastrarSegundoAnoA():
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    quantidadeAlunos = int(input('Informe quantidade de alunos presentes na turma: '))
    turma = 'segundo ano turma A'
    for contador in range(0,quantidadeAlunos):
        nomeAluno = input("nome do aluno: ")      
        sqlCadastroNomeAluno = "INSERT INTO segundoanoa(nomealuno) VALUES ('{}')".format(nomeAluno)
        interagir.execute(sqlCadastroNomeAluno)
        print("Aluno(a) {} cadastrado com sucesso no {}!".format(nomeAluno,turma))      
    print("Os alunos foram cadastrados com sucesso! \nlista de alunos cadastrados no {}".format(turma))
    conectar.commit()
    import coordenadorPedagogico
    coordenadorPedagogico.menuCoordenador()

def cadastrarSegundoAnoB():
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    quantidadeAlunos = int(input('Informe quantidade de alunos presentes na turma: '))
    turma = 'segundo ano turma B'
    for contador in range(0,quantidadeAlunos):
        nomeAluno = input("nome do aluno: ")      
        sqlCadastroNomeAluno = "INSERT INTO segundoanob(nomealuno) VALUES ('{}')".format(nomeAluno)
        interagir.execute(sqlCadastroNomeAluno)
        print("Aluno(a) {} cadastrado com sucesso no {}!".format(nomeAluno,turma))      
    conectar.commit()
    import coordenadorPedagogico
    coordenadorPedagogico.menuCoordenador()

def cadastrarSegundoAnoC():
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    quantidadeAlunos = int(input('Informe quantidade de alunos presentes na turma: '))
    turma = 'segundo ano turma C'
    for contador in range(0,quantidadeAlunos):
        nomeAluno = input("nome do aluno: ")      
        sqlCadastroNomeAluno = "INSERT INTO segundoanoc(nomealuno) VALUES ('{}')".format(nomeAluno)
        interagir.execute(sqlCadastroNomeAluno)
        print("Aluno(a) {} cadastrado com sucesso no {}!".format(nomeAluno,turma))      
    conectar.commit()
    import coordenadorPedagogico
    coordenadorPedagogico.menuCoordenador()

def cadastrarTerceiroAnoA():
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    quantidadeAlunos = int(input('Informe quantidade de alunos presentes na turma: '))
    turma = 'terceiro ano turma A'
    for contador in range(0,quantidadeAlunos):
        nomeAluno = input("nome do aluno: ")      
        sqlCadastroNomeAluno = "INSERT INTO terceiroanoa(nomealuno) VALUES ('{}')".format(nomeAluno)
        interagir.execute(sqlCadastroNomeAluno)
        print("Aluno(a) {} cadastrado com sucesso no {}!".format(nomeAluno,turma))      
    conectar.commit()
    import coordenadorPedagogico
    coordenadorPedagogico.menuCoordenador()

def cadastrarTerceiroAnoB():
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    quantidadeAlunos = int(input('Informe quantidade de alunos presentes na turma: '))
    turma = 'terceiro ano turma B'
    for contador in range(0,quantidadeAlunos):
        nomeAluno = input("nome do aluno: ")      
        sqlCadastroNomeAluno = "INSERT INTO terceiroanob(nomealuno) VALUES ('{}')".format(nomeAluno)
        interagir.execute(sqlCadastroNomeAluno)
        print("Aluno(a) {} cadastrado com sucesso no {}!".format(nomeAluno,turma))      
    conectar.commit()
    import coordenadorPedagogico
    coordenadorPedagogico.menuCoordenador()

def cadastrarTerceiroAnoC():
    import sqlite3
    conectar = sqlite3.connect("bancodeDados.db") 
    interagir = conectar.cursor()
    quantidadeAlunos = int(input('Informe quantidade de alunos presentes na turma: '))
    turma = 'terceiro ano turma C'
    for contador in range(0,quantidadeAlunos):
        nomeAluno = input("nome do aluno: ")      
        sqlCadastroNomeAluno = "INSERT INTO terceiroanoc(nomealuno) VALUES ('{}')".format(nomeAluno)
        interagir.execute(sqlCadastroNomeAluno)
        print("Aluno(a) {} cadastrado com sucesso no {}!".format(nomeAluno,turma))      
    conectar.commit()
    import coordenadorPedagogico
    coordenadorPedagogico.menuCoordenador()

