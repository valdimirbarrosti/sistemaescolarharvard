#criacao do banco de dados da aplicacao#
def criarBancodeDados(): #essa funcao é comentada apos sua primeira chamada
   import sqlite3
   conectar = sqlite3.connect("bancodeDados.db") 
   interagir = conectar.cursor()
   ## criacao da tabela que contem os dados dos professores ##
   interagir.execute('CREATE TABLE professor(nomeprofessor text, disciplina text, usuario text, senha text)')  
   ## abaixo estao as tabelas referentes a cada turma##
   interagir.execute('''
CREATE TABLE primeiroanoa(nomealuno text,
nota1prt real, nota2prt real, nota3prt real, nota4prt real,
nota1mtm real, nota2mtm real, nota3mtm real, nota4mtm real,
nota1geo real, nota2geo real, nota3geo real, nota4geo real,
nota1hst real, nota2hst real, nota3hst real, nota4hst real,
mediaprt real, mediamtm real, mediageo real, mediahst real, 
situacaoprt text, situacaomtm text, situacaogeo text, situacaohst text)
                     ''')
   interagir.execute('''
CREATE TABLE primeiroanob(nomealuno text,
nota1prt real, nota2prt real, nota3prt real, nota4prt real,
nota1mtm real, nota2mtm real, nota3mtm real, nota4mtm real,
nota1geo real, nota2geo real, nota3geo real, nota4geo real,
nota1hst real, nota2hst real, nota3hst real, nota4hst real,
mediaprt real, mediamtm real, mediageo real, mediahst real,
situacaoprt text, situacaomtm text, situacaogeo text, situacaohst text)
                     ''')
   interagir.execute('''
CREATE TABLE primeiroanoc(nomealuno text,
nota1prt real, nota2prt real, nota3prt real, nota4prt real,
nota1mtm real, nota2mtm real, nota3mtm real, nota4mtm real,
nota1geo real, nota2geo real, nota3geo real, nota4geo real,
nota1hst real, nota2hst real, nota3hst real, nota4hst real,
mediaprt real, mediamtm real, mediageo real, mediahst real,
situacaoprt text, situacaomtm text, situacaogeo text, situacaohst text)
                     ''')
   interagir.execute('''
CREATE TABLE segundoanoa(nomealuno text,
nota1prt real, nota2prt real, nota3prt real, nota4prt real,
nota1mtm real, nota2mtm real, nota3mtm real, nota4mtm real,
nota1geo real, nota2geo real, nota3geo real, nota4geo real,
nota1hst real, nota2hst real, nota3hst real, nota4hst real,
mediaprt real, mediamtm real, mediageo real, mediahst real,
situacaoprt text, situacaomtm text, situacaogeo text, situacaohst text)
                     ''')
   interagir.execute('''
CREATE TABLE segundoanob(nomealuno text,
nota1prt real, nota2prt real, nota3prt real, nota4prt real,
nota1mtm real, nota2mtm real, nota3mtm real, nota4mtm real,
nota1geo real, nota2geo real, nota3geo real, nota4geo real,
nota1hst real, nota2hst real, nota3hst real, nota4hst real,
mediaprt real, mediamtm real, mediageo real, mediahst real,
situacaoprt text, situacaomtm text, situacaogeo text, situacaohst text)
                     ''')
   interagir.execute('''
CREATE TABLE segundoanoc(nomealuno text,
nota1prt real, nota2prt real, nota3prt real, nota4prt real,
nota1mtm real, nota2mtm real, nota3mtm real, nota4mtm real,
nota1geo real, nota2geo real, nota3geo real, nota4geo real,
nota1hst real, nota2hst real, nota3hst real, nota4hst real,
mediaprt real, mediamtm real, mediageo real, mediahst real,
situacaoprt text, situacaomtm text, situacaogeo text, situacaohst text)
                     ''')
   interagir.execute('''
CREATE TABLE terceiroanoa(nomealuno text,
nota1prt real, nota2prt real, nota3prt real, nota4prt real,
nota1mtm real, nota2mtm real, nota3mtm real, nota4mtm real,
nota1geo real, nota2geo real, nota3geo real, nota4geo real,
nota1hst real, nota2hst real, nota3hst real, nota4hst real,
mediaprt real, mediamtm real, mediageo real, mediahst real,
situacaoprt text, situacaomtm text, situacaogeo text, situacaohst text)
                     ''')
   interagir.execute('''
CREATE TABLE terceiroanob(nomealuno text,
nota1prt real, nota2prt real, nota3prt real, nota4prt real,
nota1mtm real, nota2mtm real, nota3mtm real, nota4mtm real,
nota1geo real, nota2geo real, nota3geo real, nota4geo real,
nota1hst real, nota2hst real, nota3hst real, nota4hst real,
mediaprt real, mediamtm real, mediageo real, mediahst real,
situacaoprt text, situacaomtm text, situacaogeo text, situacaohst text)
                     ''')
   interagir.execute('''
CREATE TABLE terceiroanoc(nomealuno text,
nota1prt real, nota2prt real, nota3prt real, nota4prt real,
nota1mtm real, nota2mtm real, nota3mtm real, nota4mtm real,
nota1geo real, nota2geo real, nota3geo real, nota4geo real,
nota1hst real, nota2hst real, nota3hst real, nota4hst real,
mediaprt real, mediamtm real, mediageo real, mediahst real,
situacaoprt text, situacaomtm text, situacaogeo text, situacaohst text)
                        ''')
   conectar.commit()

    


      
  
   


   

 