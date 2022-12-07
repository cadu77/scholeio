from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
from qt_material import apply_stylesheet
from PySide6 import QtCore
import psycopg2
import sys
from func_cep import consulta_cep
import pandas as pd
from database import Data_base

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("SCHOLEIO - Sistema escolar")
        appIcon = QIcon(":/icons/imgs/escolar.png")
        self.setWindowIcon(appIcon)
        self.banco = Data_base()
        self.consulta_nota()
        self.consulta_aluno()
        self.consulta_professor()
        self.consulta_materia()
        

        '''Botão Menu'''
        self.btnMenu.clicked.connect(self.leftMenu)

        #=========================================================================================#

        '''Paginas do sistema'''
        self.btnMenu.clicked.connect(lambda: self.pagesMenu.setCurrentWidget(self.pageMenu))
        self.btnMenuCadastroAluno.clicked.connect(lambda: self.pagesMenu.setCurrentWidget(self.pageCadastroAluno))
        self.btnMenuCadastroProfessor.clicked.connect(lambda: self.pagesMenu.setCurrentWidget(self.pageCadastroProfessor))
        self.btnMenuCadastroFuncionario.clicked.connect(lambda: self.pagesMenu.setCurrentWidget(self.pageCadastroFuncionarios))
        self.btnMenuDisciplina.clicked.connect(lambda: self.pagesMenu.setCurrentWidget(self.pageCadastroDisciplina))
        self.btnMenuPresenca.clicked.connect(lambda: self.pagesMenu.setCurrentWidget(self.pagePresenca))
        self.btnMenuNotas.clicked.connect(lambda: self.pagesMenu.setCurrentWidget(self.pageNotas))

        #=========================================================================================#


        '''Botão cadastro Aluno'''
        self.btnCadastrarAluno.clicked.connect(self.registrar_aluno)

        '''Botão cadastro Professor'''
        self.btnCadastrarProfessor.clicked.connect(self.registrar_professor)

        '''Botão cadastro Materia'''
        self.btnCadastraDisciplina.clicked.connect(self.registrar_professor)
        
        ''' Preenchendo os campos dos cep'''
        self.txtCep.editingFinished.connect(self.consulta_api)

        '''Gerando excel alunos'''
        self.btnExcelAlunos.clicked.connect(self.excel)

    '''Botão lateral Menu'''
    def leftMenu(self):
        width = self.leftFrame.width()

        if width == 0:
            newWidth = 200
        else:
            newWidth = 0

        self.animation = QtCore.QPropertyAnimation(self.leftFrame, b'maximumWidth')
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InCubic)
        self.animation.start()


    
    '''funcao de cep'''

    def consulta_api(self):
        campos = consulta_cep(self.txtCep.text())
        
        self.txtLogradouro.setText(campos[0])
        self.txtComplemento.setText(campos[1])
        self.txtBairro.setText(campos[2])
        self.txtMunicipio.setText(campos[3])
        self.txtUf.setText(campos[4])



    '''Função EXCEL'''
    def excel(self):
        conect = psycopg2.connect(host='localhost', dbname='dbscholeio1', user='postgres', password='admin')
        alunos = pd.read_sql_query("SELECT * FROM aluno",con=conect)
        alunos.to_excel("relatorios/aluno.xlsx",sheet_name='Aluno',index=False)

        
        #alunos.to_excel, _ = QFileDialog.getSaveFileName(self, "Salvando excel file", "", "Arquivo Excel (*.xlsx)")
        
          
       

        self.msg('Ok', 'Relatório gerado com sucesso')


    '''Registro dos campos alunos no banco de dados'''
    def registrar_aluno(self):
        
        fullDataSet = (
            self.txtMatricula.text(), self.txtRa.text(), self.txtNome.text(), self.txtFone.text(), self.txtEmail.text(), 
            self.txtCep.text(), self.txtLogradouro.text(), self.txtNumeroEndereco.text(), self.txtBairro.text(), self.txtComplemento.text(),
            self.txtMunicipio.text(), self.txtUf.text(), self.txtTurma.text(), self.txtAno.text()
        )

        #Cadastrando no banco
        resposta = self.banco.registrar_aluno(fullDataSet)
        self.msg(resposta[0], resposta[1])

    #=========================================================================================#
        
    '''Registro dos campos professores no banco de dados'''   
    def registrar_professor(self):
        
        fullDataSet = (
            self.txtidProfessor.text(), self.txtNomeProfessor.text(), self.txtFoneProfessor.text(), self.txtEmailProfessor.text(), self.txtDisciplina.text(), self.txtEspecializacao.text(),
            self.txtCepProfessor.text(), self.txtLogradouroProfessor.text(), self.txtNumeroEnderecoProfessor.text(), self.txtBairroProfessor.text(), self.txtComplementoProfessor.text(),
            self.txtMunicipioProfessor.text(), self.txtUfProfessor.text()
        )

        #Cadastrando no banco
        resposta = self.banco.registrar_professor(fullDataSet)
        self.msg(resposta[0], resposta[1])



    '''Registro dos campos MATERIA no banco de dados'''
    def registrar_materia(self):
        
        fullDataSet = (
            self.txtIdMateria.text(), self.txtMateria.text(), self.txtTurmaMateria.text(), self.txtIdProfessorMateria.text(), self.txtAnoMateria.text()
        )

        #Cadastrando no banco
        resposta = self.banco.registrar_materia(fullDataSet)
        self.msg(resposta[0], resposta[1])











    '''SELECT PARA PUXAR ALUNOS E NOTAS COM A CHAVE PRIMARIA E ESTRANGEIRA'''
    def consulta_nota(self):
        resultado = self.banco.select_all_notas()
        self.tableNotas.clearContents()
        self.tableNotas.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tableNotas.setItem(row,column, QTableWidgetItem(str(data)))

    '''SELECT PARA PUXAR TODOS OS ALUNOS NA TABELA'''
    def consulta_aluno(self):
        resultado = self.banco.select_all_aluno()
        self.tableAluno.clearContents()
        self.tableAluno.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tableAluno.setItem(row,column, QTableWidgetItem(str(data)))

    '''SELECT PARA PUXAR TODOS OS PROFESSORES NA TABELA'''
    def consulta_professor(self):
        resultado = self.banco.select_all_professor()
        self.tableProfessor.clearContents()
        self.tableProfessor.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tableProfessor.setItem(row,column, QTableWidgetItem(str(data)))

    '''SELECT PARA PUXAR TODOS OS FUNCIONARIOS NA TABELA'''
    '''
    def consulta_professor(self):
        resultado = self.banco.select_all_funcionarios()
        self.tableFuncionarios.clearContents()
        self.tableFuncionarios.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tableFuncionarios.setItem(row,column, QTableWidgetItem(str(data)))

    '''


    '''SELECT PARA PUXAR TODOS OS PROFESSORES NA TABELA'''
    def consulta_materia(self):
        resultado = self.banco.select_all_materia()
        self.tableMateria.clearContents()
        self.tableMateria.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data in enumerate(text):
                self.tableMateria.setItem(row,column, QTableWidgetItem(str(data)))




        
    '''Mensagens de erro'''
    def msg(self, tipo, mensage):
        msgbox = QMessageBox()
        if tipo.lower() == 'ok':
            msgbox.setIcon(QMessageBox.Information)
        elif tipo.lower() == 'erro':
            msgbox.setIcon(QMessageBox.Critical)
        elif tipo.lower() == 'aviso':
            msgbox.setIcon(QMessageBox.Warning)
        
        msgbox.setText(mensage)
        msgbox.exec()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    banco = Data_base()
    banco.create_table_aluno()
    banco.create_table_professor()
    banco.create_table_materia()
    window = MainWindow()
    window.show()
    app.exec()