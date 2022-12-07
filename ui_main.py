# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1325, 862)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mainContainer = QFrame(self.centralwidget)
        self.mainContainer.setObjectName(u"mainContainer")
        self.mainContainer.setFrameShape(QFrame.StyledPanel)
        self.mainContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topFrame = QFrame(self.mainContainer)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnMenu = QPushButton(self.topFrame)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setStyleSheet(u"background-color: None;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QSize(45, 45))

        self.horizontalLayout_2.addWidget(self.btnMenu, 0, Qt.AlignLeft)

        self.label = QLabel(self.topFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.topFrame)

        self.mainFrame = QFrame(self.mainContainer)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pagesMenu = QStackedWidget(self.mainFrame)
        self.pagesMenu.setObjectName(u"pagesMenu")
        self.pageMenu = QWidget()
        self.pageMenu.setObjectName(u"pageMenu")
        self.pagesMenu.addWidget(self.pageMenu)
        self.pageNotas = QWidget()
        self.pageNotas.setObjectName(u"pageNotas")
        self.frame_9 = QFrame(self.pageNotas)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 10, 961, 551))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.tableNotas = QTableWidget(self.frame_9)
        if (self.tableNotas.columnCount() < 6):
            self.tableNotas.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableNotas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableNotas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableNotas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableNotas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableNotas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableNotas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableNotas.setObjectName(u"tableNotas")
        self.tableNotas.setGeometry(QRect(30, 80, 911, 321))
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(200, 420, 401, 51))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnAlteraNota = QPushButton(self.frame_10)
        self.btnAlteraNota.setObjectName(u"btnAlteraNota")

        self.horizontalLayout_6.addWidget(self.btnAlteraNota)

        self.btnExcelNota = QPushButton(self.frame_10)
        self.btnExcelNota.setObjectName(u"btnExcelNota")

        self.horizontalLayout_6.addWidget(self.btnExcelNota)

        self.pagesMenu.addWidget(self.pageNotas)
        self.pageCadastroFuncionarios = QWidget()
        self.pageCadastroFuncionarios.setObjectName(u"pageCadastroFuncionarios")
        self.tabWidget_2 = QTabWidget(self.pageCadastroFuncionarios)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(40, 40, 941, 641))
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.pageCadastraFuncionario = QFrame(self.tab_3)
        self.pageCadastraFuncionario.setObjectName(u"pageCadastraFuncionario")
        self.pageCadastraFuncionario.setGeometry(QRect(40, 10, 731, 501))
        self.pageCadastraFuncionario.setMaximumSize(QSize(16777215, 16777215))
        self.pageCadastraFuncionario.setFrameShape(QFrame.StyledPanel)
        self.pageCadastraFuncionario.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.pageCadastraFuncionario)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.txtLogradouroFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtLogradouroFuncionario.setObjectName(u"txtLogradouroFuncionario")

        self.gridLayout_5.addWidget(self.txtLogradouroFuncionario, 3, 0, 1, 3)

        self.txtEmailFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtEmailFuncionario.setObjectName(u"txtEmailFuncionario")

        self.gridLayout_5.addWidget(self.txtEmailFuncionario, 1, 2, 1, 2)

        self.txtDepartamento = QLineEdit(self.pageCadastraFuncionario)
        self.txtDepartamento.setObjectName(u"txtDepartamento")

        self.gridLayout_5.addWidget(self.txtDepartamento, 1, 4, 1, 1)

        self.txtNumeroEnderecoFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtNumeroEnderecoFuncionario.setObjectName(u"txtNumeroEnderecoFuncionario")

        self.gridLayout_5.addWidget(self.txtNumeroEnderecoFuncionario, 4, 0, 1, 2)

        self.txtNomeFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtNomeFuncionario.setObjectName(u"txtNomeFuncionario")
        self.txtNomeFuncionario.setEnabled(True)

        self.gridLayout_5.addWidget(self.txtNomeFuncionario, 0, 1, 1, 4)

        self.txtBairroFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtBairroFuncionario.setObjectName(u"txtBairroFuncionario")

        self.gridLayout_5.addWidget(self.txtBairroFuncionario, 4, 2, 1, 1)

        self.txtUfFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtUfFuncionario.setObjectName(u"txtUfFuncionario")
        self.txtUfFuncionario.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_5.addWidget(self.txtUfFuncionario, 5, 2, 1, 1)

        self.btnCadastrarFuncionario = QPushButton(self.pageCadastraFuncionario)
        self.btnCadastrarFuncionario.setObjectName(u"btnCadastrarFuncionario")
        self.btnCadastrarFuncionario.setMinimumSize(QSize(180, 29))

        self.gridLayout_5.addWidget(self.btnCadastrarFuncionario, 6, 2, 1, 2)

        self.txtFoneFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtFoneFuncionario.setObjectName(u"txtFoneFuncionario")

        self.gridLayout_5.addWidget(self.txtFoneFuncionario, 1, 0, 1, 2)

        self.txtComplementoFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtComplementoFuncionario.setObjectName(u"txtComplementoFuncionario")

        self.gridLayout_5.addWidget(self.txtComplementoFuncionario, 4, 3, 1, 2)

        self.idFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.idFuncionario.setObjectName(u"idFuncionario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.idFuncionario.sizePolicy().hasHeightForWidth())
        self.idFuncionario.setSizePolicy(sizePolicy1)
        self.idFuncionario.setMaximumSize(QSize(80, 80))

        self.gridLayout_5.addWidget(self.idFuncionario, 0, 0, 1, 1)

        self.txtMunicipioFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtMunicipioFuncionario.setObjectName(u"txtMunicipioFuncionario")

        self.gridLayout_5.addWidget(self.txtMunicipioFuncionario, 5, 0, 1, 2)

        self.txtCepFuncionario = QLineEdit(self.pageCadastraFuncionario)
        self.txtCepFuncionario.setObjectName(u"txtCepFuncionario")

        self.gridLayout_5.addWidget(self.txtCepFuncionario, 2, 0, 1, 3)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tableWidget_2 = QTableWidget(self.tab_4)
        if (self.tableWidget_2.columnCount() < 12):
            self.tableWidget_2.setColumnCount(12)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, __qtablewidgetitem17)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(10, 60, 801, 411))
        self.frame_3 = QFrame(self.tab_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(190, 480, 401, 60))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnAlterarFuncionario = QPushButton(self.frame_3)
        self.btnAlterarFuncionario.setObjectName(u"btnAlterarFuncionario")
        self.btnAlterarFuncionario.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.btnAlterarFuncionario)

        self.btnExcelFuncionario = QPushButton(self.frame_3)
        self.btnExcelFuncionario.setObjectName(u"btnExcelFuncionario")
        self.btnExcelFuncionario.setCursor(QCursor(Qt.BusyCursor))

        self.horizontalLayout_5.addWidget(self.btnExcelFuncionario)

        self.btnExcluirFuncionario = QPushButton(self.frame_3)
        self.btnExcluirFuncionario.setObjectName(u"btnExcluirFuncionario")
        self.btnExcluirFuncionario.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.btnExcluirFuncionario)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.pagesMenu.addWidget(self.pageCadastroFuncionarios)
        self.pageCadastroProfessor = QWidget()
        self.pageCadastroProfessor.setObjectName(u"pageCadastroProfessor")
        self.frame_4 = QFrame(self.pageCadastroProfessor)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 10, 951, 631))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.tabWidget_3 = QTabWidget(self.pageCadastroProfessor)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(40, 20, 901, 601))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.frame_5 = QFrame(self.tab_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 30, 741, 501))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.txtUfProfessor = QLineEdit(self.frame_5)
        self.txtUfProfessor.setObjectName(u"txtUfProfessor")
        self.txtUfProfessor.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_6.addWidget(self.txtUfProfessor, 5, 4, 1, 1)

        self.txtidProfessor = QLineEdit(self.frame_5)
        self.txtidProfessor.setObjectName(u"txtidProfessor")
        sizePolicy1.setHeightForWidth(self.txtidProfessor.sizePolicy().hasHeightForWidth())
        self.txtidProfessor.setSizePolicy(sizePolicy1)
        self.txtidProfessor.setMaximumSize(QSize(80, 80))

        self.gridLayout_6.addWidget(self.txtidProfessor, 0, 0, 1, 1)

        self.txtNomeProfessor = QLineEdit(self.frame_5)
        self.txtNomeProfessor.setObjectName(u"txtNomeProfessor")
        self.txtNomeProfessor.setEnabled(True)

        self.gridLayout_6.addWidget(self.txtNomeProfessor, 0, 1, 1, 3)

        self.txtFoneProfessor = QLineEdit(self.frame_5)
        self.txtFoneProfessor.setObjectName(u"txtFoneProfessor")

        self.gridLayout_6.addWidget(self.txtFoneProfessor, 1, 0, 1, 2)

        self.txtEmailProfessor = QLineEdit(self.frame_5)
        self.txtEmailProfessor.setObjectName(u"txtEmailProfessor")

        self.gridLayout_6.addWidget(self.txtEmailProfessor, 1, 2, 1, 2)

        self.txtDisciplina = QLineEdit(self.frame_5)
        self.txtDisciplina.setObjectName(u"txtDisciplina")

        self.gridLayout_6.addWidget(self.txtDisciplina, 1, 4, 1, 2)

        self.txtMunicipioProfessor = QLineEdit(self.frame_5)
        self.txtMunicipioProfessor.setObjectName(u"txtMunicipioProfessor")

        self.gridLayout_6.addWidget(self.txtMunicipioProfessor, 5, 2, 1, 2)

        self.txtCepProfessor = QLineEdit(self.frame_5)
        self.txtCepProfessor.setObjectName(u"txtCepProfessor")

        self.gridLayout_6.addWidget(self.txtCepProfessor, 3, 0, 1, 3)

        self.txtEspecializacao = QLineEdit(self.frame_5)
        self.txtEspecializacao.setObjectName(u"txtEspecializacao")

        self.gridLayout_6.addWidget(self.txtEspecializacao, 2, 0, 1, 3)

        self.txtLogradouroProfessor = QLineEdit(self.frame_5)
        self.txtLogradouroProfessor.setObjectName(u"txtLogradouroProfessor")

        self.gridLayout_6.addWidget(self.txtLogradouroProfessor, 4, 0, 1, 2)

        self.txtNumeroEnderecoProfessor = QLineEdit(self.frame_5)
        self.txtNumeroEnderecoProfessor.setObjectName(u"txtNumeroEnderecoProfessor")

        self.gridLayout_6.addWidget(self.txtNumeroEnderecoProfessor, 5, 0, 1, 2)

        self.txtComplementoProfessor = QLineEdit(self.frame_5)
        self.txtComplementoProfessor.setObjectName(u"txtComplementoProfessor")

        self.gridLayout_6.addWidget(self.txtComplementoProfessor, 4, 4, 1, 2)

        self.txtBairroProfessor = QLineEdit(self.frame_5)
        self.txtBairroProfessor.setObjectName(u"txtBairroProfessor")

        self.gridLayout_6.addWidget(self.txtBairroProfessor, 4, 2, 1, 2)

        self.btnCadastrarProfessor = QPushButton(self.frame_5)
        self.btnCadastrarProfessor.setObjectName(u"btnCadastrarProfessor")
        self.btnCadastrarProfessor.setMinimumSize(QSize(180, 29))

        self.gridLayout_6.addWidget(self.btnCadastrarProfessor, 6, 2, 1, 1)

        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tableProfessor = QTableWidget(self.tab_6)
        if (self.tableProfessor.columnCount() < 13):
            self.tableProfessor.setColumnCount(13)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(8, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(9, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(10, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(11, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableProfessor.setHorizontalHeaderItem(12, __qtablewidgetitem30)
        self.tableProfessor.setObjectName(u"tableProfessor")
        self.tableProfessor.setGeometry(QRect(0, 10, 821, 431))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableProfessor.sizePolicy().hasHeightForWidth())
        self.tableProfessor.setSizePolicy(sizePolicy2)
        self.tableProfessor.setTabKeyNavigation(True)
        self.tableProfessor.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.frame_6 = QFrame(self.tab_6)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(210, 470, 401, 43))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnAlterarProfessor = QPushButton(self.frame_6)
        self.btnAlterarProfessor.setObjectName(u"btnAlterarProfessor")
        self.btnAlterarProfessor.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btnAlterarProfessor)

        self.btnExcluirProfessor = QPushButton(self.frame_6)
        self.btnExcluirProfessor.setObjectName(u"btnExcluirProfessor")
        self.btnExcluirProfessor.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btnExcluirProfessor)

        self.btnExcelProfessor = QPushButton(self.frame_6)
        self.btnExcelProfessor.setObjectName(u"btnExcelProfessor")
        self.btnExcelProfessor.setCursor(QCursor(Qt.BusyCursor))

        self.horizontalLayout_7.addWidget(self.btnExcelProfessor)

        self.tabWidget_3.addTab(self.tab_6, "")
        self.pagesMenu.addWidget(self.pageCadastroProfessor)
        self.pageCadastroDisciplina = QWidget()
        self.pageCadastroDisciplina.setObjectName(u"pageCadastroDisciplina")
        self.tabMateria = QTabWidget(self.pageCadastroDisciplina)
        self.tabMateria.setObjectName(u"tabMateria")
        self.tabMateria.setGeometry(QRect(0, 20, 941, 601))
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.frame_7 = QFrame(self.tab_7)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(70, 60, 571, 401))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.txtIdMateria = QLineEdit(self.frame_7)
        self.txtIdMateria.setObjectName(u"txtIdMateria")

        self.gridLayout_7.addWidget(self.txtIdMateria, 0, 0, 1, 1)

        self.txtMateria = QLineEdit(self.frame_7)
        self.txtMateria.setObjectName(u"txtMateria")
        self.txtMateria.setMinimumSize(QSize(0, 0))
        self.txtMateria.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_7.addWidget(self.txtMateria, 0, 1, 1, 1)

        self.txtIdProfessorMateria = QLineEdit(self.frame_7)
        self.txtIdProfessorMateria.setObjectName(u"txtIdProfessorMateria")
        self.txtIdProfessorMateria.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_7.addWidget(self.txtIdProfessorMateria, 2, 0, 1, 1)

        self.txtAnoMateria = QLineEdit(self.frame_7)
        self.txtAnoMateria.setObjectName(u"txtAnoMateria")

        self.gridLayout_7.addWidget(self.txtAnoMateria, 2, 1, 1, 1)

        self.btnCadastraDisciplina = QPushButton(self.frame_7)
        self.btnCadastraDisciplina.setObjectName(u"btnCadastraDisciplina")

        self.gridLayout_7.addWidget(self.btnCadastraDisciplina, 3, 1, 1, 1)

        self.txtTurmaMateria = QLineEdit(self.frame_7)
        self.txtTurmaMateria.setObjectName(u"txtTurmaMateria")

        self.gridLayout_7.addWidget(self.txtTurmaMateria, 0, 2, 1, 1)

        self.tabMateria.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.tableMateria = QTableWidget(self.tab_8)
        if (self.tableMateria.columnCount() < 6):
            self.tableMateria.setColumnCount(6)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableMateria.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableMateria.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableMateria.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableMateria.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableMateria.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableMateria.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        self.tableMateria.setObjectName(u"tableMateria")
        self.tableMateria.setGeometry(QRect(20, 50, 761, 361))
        self.frame_8 = QFrame(self.tab_8)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(150, 430, 441, 60))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAlterarDisciplina = QPushButton(self.frame_8)
        self.btnAlterarDisciplina.setObjectName(u"btnAlterarDisciplina")

        self.horizontalLayout.addWidget(self.btnAlterarDisciplina)

        self.btnExcelDisciplina = QPushButton(self.frame_8)
        self.btnExcelDisciplina.setObjectName(u"btnExcelDisciplina")

        self.horizontalLayout.addWidget(self.btnExcelDisciplina)

        self.btnExcluirDisciplina = QPushButton(self.frame_8)
        self.btnExcluirDisciplina.setObjectName(u"btnExcluirDisciplina")

        self.horizontalLayout.addWidget(self.btnExcluirDisciplina)

        self.tabMateria.addTab(self.tab_8, "")
        self.pagesMenu.addWidget(self.pageCadastroDisciplina)
        self.pagePresenca = QWidget()
        self.pagePresenca.setObjectName(u"pagePresenca")
        self.frame_11 = QFrame(self.pagePresenca)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 10, 881, 691))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.tableWidget_6 = QTableWidget(self.frame_11)
        if (self.tableWidget_6.columnCount() < 3):
            self.tableWidget_6.setColumnCount(3)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setGeometry(QRect(80, 310, 701, 291))
        self.calendarWidget = QCalendarWidget(self.frame_11)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(80, 50, 341, 221))
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(730, 20, 91, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_3.setFont(font1)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(190, 610, 421, 51))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnCadastraPresenca = QPushButton(self.frame_12)
        self.btnCadastraPresenca.setObjectName(u"btnCadastraPresenca")

        self.horizontalLayout_3.addWidget(self.btnCadastraPresenca)

        self.btnAlteraPresenca = QPushButton(self.frame_12)
        self.btnAlteraPresenca.setObjectName(u"btnAlteraPresenca")

        self.horizontalLayout_3.addWidget(self.btnAlteraPresenca)

        self.btnExcelPresenca = QPushButton(self.frame_12)
        self.btnExcelPresenca.setObjectName(u"btnExcelPresenca")

        self.horizontalLayout_3.addWidget(self.btnExcelPresenca)

        self.pagesMenu.addWidget(self.pagePresenca)
        self.pageCadastroAluno = QWidget()
        self.pageCadastroAluno.setObjectName(u"pageCadastroAluno")
        self.tabWidget = QTabWidget(self.pageCadastroAluno)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 931, 641))
        font2 = QFont()
        font2.setPointSize(9)
        self.tabWidget.setFont(font2)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 0, 791, 571))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txtMunicipio = QLineEdit(self.frame)
        self.txtMunicipio.setObjectName(u"txtMunicipio")

        self.gridLayout_2.addWidget(self.txtMunicipio, 5, 0, 1, 2)

        self.txtEmail = QLineEdit(self.frame)
        self.txtEmail.setObjectName(u"txtEmail")

        self.gridLayout_2.addWidget(self.txtEmail, 2, 2, 1, 1)

        self.txtBairro = QLineEdit(self.frame)
        self.txtBairro.setObjectName(u"txtBairro")

        self.gridLayout_2.addWidget(self.txtBairro, 4, 2, 1, 1)

        self.txtLogradouro = QLineEdit(self.frame)
        self.txtLogradouro.setObjectName(u"txtLogradouro")

        self.gridLayout_2.addWidget(self.txtLogradouro, 3, 2, 1, 2)

        self.txtRa = QLineEdit(self.frame)
        self.txtRa.setObjectName(u"txtRa")
        sizePolicy1.setHeightForWidth(self.txtRa.sizePolicy().hasHeightForWidth())
        self.txtRa.setSizePolicy(sizePolicy1)
        self.txtRa.setMaximumSize(QSize(80, 80))

        self.gridLayout_2.addWidget(self.txtRa, 1, 0, 1, 1)

        self.txtUf = QLineEdit(self.frame)
        self.txtUf.setObjectName(u"txtUf")
        self.txtUf.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.txtUf, 5, 2, 1, 1)

        self.txtTurma = QLineEdit(self.frame)
        self.txtTurma.setObjectName(u"txtTurma")

        self.gridLayout_2.addWidget(self.txtTurma, 1, 3, 1, 1)

        self.txtNome = QLineEdit(self.frame)
        self.txtNome.setObjectName(u"txtNome")
        self.txtNome.setEnabled(True)

        self.gridLayout_2.addWidget(self.txtNome, 1, 1, 1, 2)

        self.txtCep = QLineEdit(self.frame)
        self.txtCep.setObjectName(u"txtCep")

        self.gridLayout_2.addWidget(self.txtCep, 3, 0, 1, 2)

        self.txtNumeroEndereco = QLineEdit(self.frame)
        self.txtNumeroEndereco.setObjectName(u"txtNumeroEndereco")

        self.gridLayout_2.addWidget(self.txtNumeroEndereco, 4, 0, 1, 2)

        self.txtComplemento = QLineEdit(self.frame)
        self.txtComplemento.setObjectName(u"txtComplemento")

        self.gridLayout_2.addWidget(self.txtComplemento, 4, 3, 1, 1)

        self.txtMatricula = QLineEdit(self.frame)
        self.txtMatricula.setObjectName(u"txtMatricula")

        self.gridLayout_2.addWidget(self.txtMatricula, 0, 0, 1, 2)

        self.txtFone = QLineEdit(self.frame)
        self.txtFone.setObjectName(u"txtFone")

        self.gridLayout_2.addWidget(self.txtFone, 2, 0, 1, 2)

        self.btnCadastrarAluno = QPushButton(self.frame)
        self.btnCadastrarAluno.setObjectName(u"btnCadastrarAluno")
        self.btnCadastrarAluno.setMinimumSize(QSize(180, 29))
        self.btnCadastrarAluno.setMaximumSize(QSize(16777215, 1))

        self.gridLayout_2.addWidget(self.btnCadastrarAluno, 6, 2, 1, 1)

        self.txtAno = QLineEdit(self.frame)
        self.txtAno.setObjectName(u"txtAno")
        self.txtAno.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_2.addWidget(self.txtAno, 2, 3, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tableAluno = QTableWidget(self.tab_2)
        if (self.tableAluno.columnCount() < 14):
            self.tableAluno.setColumnCount(14)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableAluno.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(5, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(6, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(7, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(8, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(9, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(10, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(11, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableAluno.setHorizontalHeaderItem(12, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        self.tableAluno.setHorizontalHeaderItem(13, __qtablewidgetitem53)
        self.tableAluno.setObjectName(u"tableAluno")
        self.tableAluno.setGeometry(QRect(16, 66, 901, 441))
        self.tableAluno.setLayoutDirection(Qt.LeftToRight)
        self.tableAluno.setFrameShape(QFrame.Box)
        self.tableAluno.setFrameShadow(QFrame.Plain)
        self.tableAluno.setLineWidth(0)
        self.tableAluno.setMidLineWidth(0)
        self.tableAluno.setAutoScroll(True)
        self.tableAluno.setDragEnabled(False)
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(250, 520, 361, 43))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnAlterarAlunos = QPushButton(self.frame_2)
        self.btnAlterarAlunos.setObjectName(u"btnAlterarAlunos")
        self.btnAlterarAlunos.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btnAlterarAlunos)

        self.btnExcluirAlunos = QPushButton(self.frame_2)
        self.btnExcluirAlunos.setObjectName(u"btnExcluirAlunos")
        self.btnExcluirAlunos.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.btnExcluirAlunos)

        self.btnExcelAlunos = QPushButton(self.frame_2)
        self.btnExcelAlunos.setObjectName(u"btnExcelAlunos")
        self.btnExcelAlunos.setCursor(QCursor(Qt.BusyCursor))

        self.horizontalLayout_4.addWidget(self.btnExcelAlunos)

        self.tabWidget.addTab(self.tab_2, "")
        self.pagesMenu.addWidget(self.pageCadastroAluno)

        self.verticalLayout_4.addWidget(self.pagesMenu)


        self.verticalLayout.addWidget(self.mainFrame)

        self.mainFrame.raise_()
        self.topFrame.raise_()

        self.gridLayout_3.addWidget(self.mainContainer, 0, 1, 1, 1)

        self.leftFrame = QFrame(self.centralwidget)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMaximumSize(QSize(200, 16777215))
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logoFrame = QFrame(self.leftFrame)
        self.logoFrame.setObjectName(u"logoFrame")
        self.logoFrame.setFrameShape(QFrame.StyledPanel)
        self.logoFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.logoFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.logo = QLabel(self.logoFrame)
        self.logo.setObjectName(u"logo")

        self.gridLayout_4.addWidget(self.logo, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.logoFrame)

        self.buttonsFrame = QFrame(self.leftFrame)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setMaximumSize(QSize(160, 16777215))
        self.buttonsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.buttonsFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.buttonsFrame)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setEnabled(True)
        self.toolBox.setMinimumSize(QSize(140, 0))
        self.toolBox.setMaximumSize(QSize(230, 16777215))
        self.toolBox.setSizeIncrement(QSize(230, 120))
        self.toolBox.setBaseSize(QSize(230, 0))
        font3 = QFont()
        font3.setBold(False)
        self.toolBox.setFont(font3)
        self.toolBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.pageHome.setEnabled(True)
        self.pageHome.setGeometry(QRect(0, 0, 140, 676))
        self.gridLayout = QGridLayout(self.pageHome)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(0, 120, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.btnMenuDisciplina = QPushButton(self.pageHome)
        self.btnMenuDisciplina.setObjectName(u"btnMenuDisciplina")
        self.btnMenuDisciplina.setMaximumSize(QSize(130, 16777215))
        self.btnMenuDisciplina.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btnMenuDisciplina, 3, 0, 1, 1)

        self.btnMenuCadastroProfessor = QPushButton(self.pageHome)
        self.btnMenuCadastroProfessor.setObjectName(u"btnMenuCadastroProfessor")
        self.btnMenuCadastroProfessor.setMaximumSize(QSize(130, 16777215))
        self.btnMenuCadastroProfessor.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btnMenuCadastroProfessor, 1, 0, 1, 1)

        self.btnMenuPresenca = QPushButton(self.pageHome)
        self.btnMenuPresenca.setObjectName(u"btnMenuPresenca")
        self.btnMenuPresenca.setMaximumSize(QSize(130, 16777215))
        self.btnMenuPresenca.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btnMenuPresenca, 4, 0, 1, 1)

        self.btnMenuNotas = QPushButton(self.pageHome)
        self.btnMenuNotas.setObjectName(u"btnMenuNotas")
        self.btnMenuNotas.setMaximumSize(QSize(130, 16777215))
        self.btnMenuNotas.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btnMenuNotas, 5, 0, 1, 1)

        self.btnMenuCadastroFuncionario = QPushButton(self.pageHome)
        self.btnMenuCadastroFuncionario.setObjectName(u"btnMenuCadastroFuncionario")
        self.btnMenuCadastroFuncionario.setMaximumSize(QSize(130, 16777215))
        self.btnMenuCadastroFuncionario.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btnMenuCadastroFuncionario, 2, 0, 1, 1)

        self.btnMenuCadastroAluno = QPushButton(self.pageHome)
        self.btnMenuCadastroAluno.setObjectName(u"btnMenuCadastroAluno")
        self.btnMenuCadastroAluno.setMaximumSize(QSize(130, 16777215))
        self.btnMenuCadastroAluno.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btnMenuCadastroAluno, 0, 0, 1, 1)

        self.toolBox.addItem(self.pageHome, u"Menu")
        self.pageInformacoes = QWidget()
        self.pageInformacoes.setObjectName(u"pageInformacoes")
        self.pageInformacoes.setGeometry(QRect(0, 0, 140, 676))
        self.verticalLayout_6 = QVBoxLayout(self.pageInformacoes)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.toolBox.addItem(self.pageInformacoes, u"Informa\u00e7\u00f5es")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.buttonsFrame)


        self.gridLayout_3.addWidget(self.leftFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pagesMenu.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabMateria.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.mainContainer.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnMenu.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/menu.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnMenu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema Escolar - Scholeio", None))
#if QT_CONFIG(tooltip)
        self.mainFrame.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pagesMenu.setToolTip(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pageMenu.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.tableNotas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"R.A", None));
        ___qtablewidgetitem1 = self.tableNotas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Aluno", None));
        ___qtablewidgetitem2 = self.tableNotas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"portugu\u00eas", None));
        ___qtablewidgetitem3 = self.tableNotas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"matem\u00e1tica", None));
        ___qtablewidgetitem4 = self.tableNotas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ci\u00eancias", None));
        ___qtablewidgetitem5 = self.tableNotas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"geografia", None));
        self.btnAlteraNota.setText(QCoreApplication.translate("MainWindow", u"Registrar Nota", None))
        self.btnExcelNota.setText(QCoreApplication.translate("MainWindow", u"Importar .csv", None))
        self.txtLogradouroFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txtEmailFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txtDepartamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.txtNumeroEnderecoFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txtNomeFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txtBairroFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txtUfFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.btnCadastrarFuncionario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.txtFoneFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txtComplementoFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.idFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id", None))
        self.txtMunicipioFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mun\u00edcipio", None))
        self.txtCepFuncionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Cadastra Funcionario", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"id Funcionario", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Departamento", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        self.btnAlterarFuncionario.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcelFuncionario.setText(QCoreApplication.translate("MainWindow", u"Importar .csv", None))
        self.btnExcluirFuncionario.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Funcionario", None))
        self.txtUfProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txtidProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id", None))
        self.txtNomeProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txtFoneProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txtEmailProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txtDisciplina.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Disciplina", None))
        self.txtMunicipioProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mun\u00edcipio", None))
        self.txtCepProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txtEspecializacao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Especializa\u00e7\u00e3o", None))
        self.txtLogradouroProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txtNumeroEnderecoProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txtComplementoProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txtBairroProfessor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.btnCadastrarProfessor.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Cadastro Professor", None))
        ___qtablewidgetitem18 = self.tableProfessor.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"id ", None));
        ___qtablewidgetitem19 = self.tableProfessor.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem20 = self.tableProfessor.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem21 = self.tableProfessor.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem22 = self.tableProfessor.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Disciplina", None));
        ___qtablewidgetitem23 = self.tableProfessor.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Especializa\u00e7\u00e3o", None));
        ___qtablewidgetitem24 = self.tableProfessor.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem25 = self.tableProfessor.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None));
        ___qtablewidgetitem26 = self.tableProfessor.horizontalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtablewidgetitem27 = self.tableProfessor.horizontalHeaderItem(9)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem28 = self.tableProfessor.horizontalHeaderItem(10)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem29 = self.tableProfessor.horizontalHeaderItem(11)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtablewidgetitem30 = self.tableProfessor.horizontalHeaderItem(12)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        self.btnAlterarProfessor.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcluirProfessor.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btnExcelProfessor.setText(QCoreApplication.translate("MainWindow", u"Importar .csv", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Professor", None))
        self.txtIdMateria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id Materia", None))
        self.txtMateria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Disciplina", None))
        self.txtIdProfessorMateria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"id Professor", None))
        self.txtAnoMateria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ano ", None))
        self.btnCadastraDisciplina.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.txtTurmaMateria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Turma", None))
        self.tabMateria.setTabText(self.tabMateria.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Cadastro Disciplina", None))
        ___qtablewidgetitem31 = self.tableMateria.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"id Disciplina", None));
        ___qtablewidgetitem32 = self.tableMateria.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Disciplina", None));
        ___qtablewidgetitem33 = self.tableMateria.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"id Professor", None));
        ___qtablewidgetitem34 = self.tableMateria.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Professor", None));
        ___qtablewidgetitem35 = self.tableMateria.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Ano", None));
        ___qtablewidgetitem36 = self.tableMateria.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        self.btnAlterarDisciplina.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcelDisciplina.setText(QCoreApplication.translate("MainWindow", u"Importar .csv", None))
        self.btnExcluirDisciplina.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabMateria.setTabText(self.tabMateria.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Disciplina", None))
        ___qtablewidgetitem37 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"R.A", None));
        ___qtablewidgetitem38 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Alunos", None));
        ___qtablewidgetitem39 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.btnCadastraPresenca.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Presen\u00e7a", None))
        self.btnAlteraPresenca.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcelPresenca.setText(QCoreApplication.translate("MainWindow", u"Importar .csv", None))
        self.txtMunicipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mun\u00edcipio", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txtBairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txtLogradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txtRa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R.A", None))
        self.txtUf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txtTurma.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Turma", None))
        self.txtNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txtCep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txtNumeroEndereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txtComplemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txtMatricula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Matricula", None))
        self.txtFone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.btnCadastrarAluno.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.txtAno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ano", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro Alunos", None))
        ___qtablewidgetitem40 = self.tableAluno.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Matricula", None));
        ___qtablewidgetitem41 = self.tableAluno.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"R.A", None));
        ___qtablewidgetitem42 = self.tableAluno.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem43 = self.tableAluno.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem44 = self.tableAluno.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem45 = self.tableAluno.horizontalHeaderItem(5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem46 = self.tableAluno.horizontalHeaderItem(6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None));
        ___qtablewidgetitem47 = self.tableAluno.horizontalHeaderItem(7)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtablewidgetitem48 = self.tableAluno.horizontalHeaderItem(8)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem49 = self.tableAluno.horizontalHeaderItem(9)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem50 = self.tableAluno.horizontalHeaderItem(10)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtablewidgetitem51 = self.tableAluno.horizontalHeaderItem(11)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem52 = self.tableAluno.horizontalHeaderItem(12)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Ano", None));
        ___qtablewidgetitem53 = self.tableAluno.horizontalHeaderItem(13)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        self.btnAlterarAlunos.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcluirAlunos.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btnExcelAlunos.setText(QCoreApplication.translate("MainWindow", u"Importar .csv", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alunos", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/escolar.png\"/></p></body></html>", None))
        self.btnMenuDisciplina.setText(QCoreApplication.translate("MainWindow", u"Disciplinas", None))
        self.btnMenuCadastroProfessor.setText(QCoreApplication.translate("MainWindow", u"Professores", None))
        self.btnMenuPresenca.setText(QCoreApplication.translate("MainWindow", u"Presen\u00e7a", None))
        self.btnMenuNotas.setText(QCoreApplication.translate("MainWindow", u"Notas", None))
        self.btnMenuCadastroFuncionario.setText(QCoreApplication.translate("MainWindow", u"Funcionarios", None))
        self.btnMenuCadastroAluno.setText(QCoreApplication.translate("MainWindow", u"Alunos", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageHome), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.pageInformacoes), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
    # retranslateUi

