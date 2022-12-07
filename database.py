import psycopg2


class Data_base:

    
    ''' Conexao com o banco'''

    def connect(self):
        self.connection = psycopg2.connect(host='localhost', dbname='dbscholeio1', user='postgres', password='admin')

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)    
            return 'erro'


################## ALUNOOOOOOOOOOOOOOOOOOOOOOOS #############################################

    '''Tabela alunos'''
    def create_table_aluno(self):
        self.connect()
        cursor = self.connection.cursor()
        create_aluno = ''' DROP TABLE IF EXISTS aluno CASCADE ;
                            CREATE TABLE aluno (
                                Matricula INT,
                                RA INT PRIMARY KEY,
                                Nome VARCHAR (60) NOT NULL,
                                Telefone INT NOT NULL,
                                Email VARCHAR (70) NOT NULL,
                                CEP VARCHAR (10) NOT NULL,
                                Logradouro VARCHAR(100) NOT NULL,
                                Numero INT NOT NULL,
                                Bairro VARCHAR(20) NOT NULL,
                                Complemento VARCHAR(20),
                                Municipio VARCHAR(20) not null,
                                UF VARCHAR(3) not null,
                                Ano int not null,
                                Turma VARCHAR(2) not null
                            ); '''
        cursor.execute(create_aluno)
        self.close_connection()


    def registrar_aluno(self, fullDataSet):

            
            self.connect()
            
            cursor = self.connection.cursor()
            
            try:
                cursor.execute('INSERT INTO aluno (matricula,ra,nome,telefone,email,cep,logradouro,numero,bairro,complemento,municipio,uf,ano,turma) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', fullDataSet)
                self.connection.commit()
                return "OK", "Aluno cadastrado com sucesso!"
            except Exception as e:
                print(e)
                return 'erro', str(e)

            finally:
                self.close_connection()
        

    def select_all_aluno(self):
            try:
                self.connect()
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM Aluno ORDER BY NOME")
                alunos = cursor.fetchall()
                return alunos

            except Exception as e:
                print(e)
            finally:
                self.close_connection()

    def delete_aluno(self, ra):
        
            try:
                self.connect()
                cursor = self.connection.cursor()
                cursor.execute(f"DELETE FROM aluno WHERE RA = '{ra}'")
                self.connection.commit()
                return 'OK', "Aluno excluido com sucesso!"
            except Exception as e:
                return 'erro', str(e)
            finally:
                self.close_connection()

    def update_aluno(self, fullDataSet):
        
            self.connect()
            
            try:
                cursor = self.connection.cursor()
                cursor.execute(f""" UPDATE aluno set
                            
                        matricula = '{fullDataSet[0]}',
                        ra = '{fullDataSet[1]}',
                        nome = '{fullDataSet[2]}',
                        telefone = '{fullDataSet[3]}',
                        email = '{fullDataSet[4]}',
                        cep = '{fullDataSet[5]}',
                        logradouro = '{fullDataSet[6]}',
                        numero = '{fullDataSet[7]}',
                        bairro = '{fullDataSet[8]}',
                        complemento = '{fullDataSet[9]}',
                        municipio = '{fullDataSet[10]}'
                        uf = '{fullDataSet[11]}'
                        ano = '{fullDataSet[12]}'
                        turma = '{fullDataSet[13]}'
                        WHERE RA = '{fullDataSet[1]}'""")                  
                self.connection.commit()
                return 'OK', 'Dados atualizado com sucesso!'
            except Exception as e:
                return "erro", str(e)
            finally:
                self.close_connection()



################# PROFESSOREEEEEEEEEES #############################################

    '''Tabela Professor'''
    def create_table_professor(self):
            self.connect()
            cursor = self.connection.cursor()
            create_professor = ''' DROP TABLE IF EXISTS aluno CASCADE ;
                                    CREATE TABLE IF NOT EXISTS professor (
                                            
                                            id_professor int PRIMARY KEY ,
                                            nome_professor VARCHAR (50) NOT NULL ,
                                            tel_professor INT not null ,
                                            email_professor VARCHAR (70) NOT NULL ,
                                            disciplina_professor VARCHAR (50) NOT NULL ,
                                            especializacao_professor VARCHAR (20) NOT NULL ,
                                            cep_professor VARCHAR (13) NOT NULL ,
                                            logd_professor VARCHAR (60) not null,
                                            num_professor int NOT NULL,
                                            bairro_professor VARCHAR (30) NOT NULL,
                                            comple_professor VARCHAR (30),
                                            muni_professor VARCHAR (20) NOT NULL,
                                            uf_professor CHAR (3) NOT NULL
                                            ) '''
            cursor.execute(create_professor)
            self.close_connection()

    def registrar_professor(self, fullDataSet):

            
            self.connect()
            
            cursor = self.connection.cursor()
            
            try:
                cursor.execute('INSERT INTO professor (id_professor,nome_professor,tel_professor,email_professor,disciplina_professor,especializacao_professor,cep_professor,logd_professor,num_professor,bairro_professor,comple_professor,muni_professor,uf_professor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', fullDataSet)
                self.connection.commit()
                return "OK", "Professor cadastrado com sucesso!"
            except Exception as e:
                print(e)
                return 'erro', str(e)

            finally:
                self.close_connection()       

    def select_all_professor(self):
            try:
                self.connect()
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM Professor ORDER BY nome_professor")
                professor = cursor.fetchall()
                return professor

            except Exception as e:
                print(e)
            finally:
                self.close_connection()

################# FUNCIONARIOOOOOS #############################################

################# DISCIPLINAAAAAAS #############################################


    def create_table_materia(self):
        self.connect()
        cursor = self.connection.cursor()
        create_aluno = ''' DROP TABLE IF EXISTS materia CASCADE ;
                            CREATE TABLE materia (
                                id_materia int PRIMARY KEY ,
                                id_professor INT ,
                                disciplina VARCHAR (25) NOT NULL ,
                                ano_materia INT NOT NULL ,
                                turma_materia VARCHAR (2) NOT NULL,
                                FOREIGN KEY (id_professor) REFERENCES professor(id_professor)
                            ); '''
        cursor.execute(create_aluno)
        self.close_connection()


    def registrar_materia(self, fullDataSet):

            
            self.connect()
            
            cursor = self.connection.cursor()
            
            try:
                cursor.execute('INSERT INTO materia (id_materia,id_professor,disciplina,ano_materia,turma_materia) VALUES (%s, %s, %s, %s, %s)', fullDataSet)
                self.connection.commit()
                return "OK", "Materia cadastrada com sucesso!"
            except Exception as e:
                print(e)
                return 'erro', str(e)

            finally:
                self.close_connection() 

    '''SELECT PARA PUXAR ALUNOS E NOTAS COM A CHAVE PRIMARIA E ESTRANGEIRA'''
    def select_all_materia(self):
            try:
                self.connect()
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM materia ORDER BY id_materia")

                
                materia = cursor.fetchall()
                return materia

            except Exception as e:
                print(e)
            finally:
                self.close_connection()


################# PRESENÇAAAAAAAA #############################################




################# NOTAAAAAAAAAAAAAAAAS #############################################
    '''SELECT PARA PUXAR ALUNOS E NOTAS COM A CHAVE PRIMARIA E ESTRANGEIRA'''
    def select_all_notas(self):
            try:
                self.connect()
                cursor = self.connection.cursor()
                cursor.execute("SELECT notas.RA, aluno.Nome,notas.N_port, notas.N_matematica, notas.N_ciencias, notas.N_historia, notas.N_geografia FROM notas INNER JOIN aluno ON notas.RA = aluno.RA")

                
                alunos = cursor.fetchall()
                return alunos

            except Exception as e:
                print(e)
            finally:
                self.close_connection()