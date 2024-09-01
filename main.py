from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from osgeo import gdal
import os
import tempfile
import time
from interp import Interpolador
from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.current_colorbar = None
        self.dfn = None
        MainWindow.setObjectName("Pyterpolador")
        MainWindow.resize(1192, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1191, 791))
        self.stackedWidget.setObjectName("stackedWidget")
       
        # Criando página 1
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(430, 270, 311, 101))
        font = QtGui.QFont()
        font.setFamily("ItalicT")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # Criando botões
        self.pushButton_menu_2 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_menu_2.setGeometry(QtCore.QRect(590, 380, 135, 28))
        self.pushButton_menu_2.setObjectName("pushButton_menu_2")
        self.pushButton_menu_1 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_menu_1.setGeometry(QtCore.QRect(400, 380, 135, 28))
        self.pushButton_menu_1.setObjectName("pushButton_menu_1")
        self.stackedWidget.addWidget(self.page_1)
        
        # Criando página 2
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(10, 450, 41, 16))
        self.label_8.setObjectName("label_8")
        # Criando botões
        self.pushButton_menu = QtWidgets.QPushButton(self.page_2)
        self.pushButton_menu.setGeometry(QtCore.QRect(10, 750, 131, 28))
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.pushButtonInterpolar = QtWidgets.QPushButton(self.page_2)
        self.pushButtonInterpolar.setGeometry(QtCore.QRect(10, 540, 171, 28))
        self.pushButtonInterpolar.setObjectName("pushButtonInterpolar")
        self.pushButtonSalvarTif = QtWidgets.QPushButton(self.page_2)
        self.pushButtonSalvarTif.setGeometry(QtCore.QRect(600, 760, 161, 28))
        self.pushButtonSalvarTif.setObjectName("pushButtonSalvarTif")
        self.pushButtonAbrirSHP = QtWidgets.QPushButton(self.page_2)
        self.pushButtonAbrirSHP.setGeometry(QtCore.QRect(10, 10, 131, 28))
        self.pushButtonAbrirSHP.setObjectName("pushButtonAbrirSHP")
        # Criando Combo Box
        self.comboBoxAlgoritmo = QtWidgets.QComboBox(self.page_2)
        self.comboBoxAlgoritmo.setGeometry(QtCore.QRect(10, 230, 171, 22))
        self.comboBoxAlgoritmo.setObjectName("comboBoxAlgoritmo")
        self.comboBoxAlgoritmo.addItem("")
        self.comboBoxAlgoritmo.addItem("")
        self.comboBoxAlgoritmo.addItem("")
        self.comboBoxPotencia = QtWidgets.QComboBox(self.page_2)
        self.comboBoxPotencia.setGeometry(QtCore.QRect(10, 410, 171, 22))
        self.comboBoxPotencia.setObjectName("comboBoxPotencia")
        self.comboBoxPotencia.addItem("")
        self.comboBoxPotencia.addItem("")
        self.comboBoxPotencia.addItem("")
        self.comboBoxPotencia.addItem("")
        self.comboBoxPaletaCor = QtWidgets.QComboBox(self.page_2)
        self.comboBoxPaletaCor.setGeometry(QtCore.QRect(10, 470, 171, 22))
        self.comboBoxPaletaCor.setObjectName("comboBoxPaletaCor")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        self.comboBoxPaletaCor.addItem("")
        # Criando Double Spin Box
        self.doubleSpinBoxRaioa = QtWidgets.QDoubleSpinBox(self.page_2)
        self.doubleSpinBoxRaioa.setGeometry(QtCore.QRect(10, 290, 131, 22))
        self.doubleSpinBoxRaioa.setObjectName("doubleSpinBoxRaioa")
        self.doubleSpinBoxRaioa.setMaximum(100000)
        self.doubleSpinBoxRaiob = QtWidgets.QDoubleSpinBox(self.page_2)
        self.doubleSpinBoxRaiob.setGeometry(QtCore.QRect(10, 350, 131, 22))
        self.doubleSpinBoxRaiob.setObjectName("doubleSpinBoxRaiob")
        self.doubleSpinBoxRaiob.setMaximum(100000)
        self.doubleSpinBoxResolucao = QtWidgets.QDoubleSpinBox(self.page_2)
        self.doubleSpinBoxResolucao.setGeometry(QtCore.QRect(10, 170, 131, 22))
        self.doubleSpinBoxResolucao.setObjectName("doubleSpinBoxResolucao")
        self.doubleSpinBoxResolucao.setMaximum(100000)
        # Criando Line Edit
        self.lineEditColunaDados = QtWidgets.QLineEdit(self.page_2)
        self.lineEditColunaDados.setGeometry(QtCore.QRect(10, 110, 171, 22))
        self.lineEditColunaDados.setObjectName("lineEditColunaDados")
        self.lineEditCaminho = QtWidgets.QLineEdit(self.page_2)
        self.lineEditCaminho.setGeometry(QtCore.QRect(10, 50, 171, 22))
        self.lineEditCaminho.setObjectName("lineEdit")
        # Criando Labels
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 171, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(10, 330, 131, 16))
        self.label_6.setObjectName("label_6")        
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(10, 390, 101, 16))
        self.label_7.setObjectName("label_7")
        # Criando Plot Widget
        self.MplWidget = MplWidget(self.page_2)
        self.MplWidget.setGeometry(QtCore.QRect(230, 10, 951, 741))
        self.MplWidget.setObjectName("MplWidget")
        
        self.stackedWidget.addWidget(self.page_2)
        
        # Criando página 3
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Atribuindo métodos aos botões
        self.pushButton_menu_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_menu_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_menu.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButtonInterpolar.clicked.connect(self.atualiza_grafico)
        #Botão obtem caminho do arquivo
        self.pushButtonAbrirSHP.clicked.connect(self.obtem_caminho_arquivo)
        #Botão converte gráfico em tif e salva no caminho escolhido
        self.pushButtonSalvarTif.clicked.connect(self.show_save_dialog)

    def show_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Informação")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def obtem_caminho_arquivo(self):
        caminho_arquivo, _ = QFileDialog.getOpenFileName(None,
        "Selecione um arquivo",
        "",  # Diretório inicial
        "(*.shp)")
        self.lineEditCaminho.setText(caminho_arquivo)
    
    def show_save_dialog(self):
        print("vou pegar o path onde ira salvar")
        # Abre o diálogo de salvar arquivo
        file_path, _ = QFileDialog.getSaveFileName(None,
                                                   "Salvar Arquivo",
                                                   "",
                                                   "(*.tif)",)
        if file_path:
            self.transforma_TIFF(file_path)

    def transforma_TIFF(self,file_path):
        self.file_path = file_path
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xyz") as arquivo_temp_xyz:
            self.dfn.to_csv(arquivo_temp_xyz.name, index = False, header = None, sep = " ")
            arquivo_temporario = arquivo_temp_xyz.name
        
        # Abre o arquivo temporário como um dataset GDAL
        temp_dataset = gdal.Open(arquivo_temporario)

        if temp_dataset is not None:
            gdal.Translate(self.file_path, temp_dataset, outputSRS="EPSG:31983", xRes=self.doubleSpinBoxResolucao.value(),
                            yRes=self.doubleSpinBoxResolucao.value())
            temp_dataset = None
            import gc
            gc.collect()
        else:
            print("Erro ao abrir o arquivo temporário como dataset GDAL")

        # Espera breve para assegurar que todos os processos liberem o arquivo
        time.sleep(1)

        # Forçar a liberação do arquivo temporário
        try:
            os.remove(arquivo_temporario)
            print(f'Arquivo temporário removido: {arquivo_temporario}')
        except OSError as e:
            print(f'Erro ao remover o arquivo temporário: {e}')
        self.show_message("Arquivo salvo com sucesso")
    # +".tif"
    def save_file(self, file_path):
        print("vou começar os trabalhos aqui...")
        self.file_path = file_path
        Interpolador.transforma_TIFF(self.dfn,self.file_path)
    

    def define_algoritmo(self):
        #Determinando algoritmo escolhido na comboBox
        if self.comboBoxAlgoritmo.currentText() == "Vizinhos mais Próximos":
            algoritmo = "Vizinhos" 
        elif self.comboBoxAlgoritmo.currentText() == "Média dos Pontos":
            algoritmo = "Media" 
        elif self.comboBoxAlgoritmo.currentText() == "Inverso da Distância (IDW)":
            algoritmo = "IDW"
        return algoritmo

    def atualiza_grafico(self):
        
        if self.current_colorbar is not None:
            self.current_colorbar.remove()
            self.current_colorbar = None

        algoritmo = self.define_algoritmo()
        #Instanciando objeto de interpolação
        interpolacao = Interpolador(self.lineEditCaminho.text(), self.lineEditColunaDados.text(), algoritmo, self.doubleSpinBoxResolucao.value(),
                                     self.doubleSpinBoxRaioa.value(), self.doubleSpinBoxRaiob.value(),int(self.comboBoxPotencia.currentText()))
        #Interpolando com o método interpolar
        dados = interpolacao.interpolar()
        print("vou instanciar objeto ao self objeto")
        self.latitude_pixels = interpolacao.latitude_pixels
        self.longitude_pixels = interpolacao.longitude_pixels
        self.valores_z = dados
        self.dfn = interpolacao.gera_data_frame_de_dados()
        #Remodelando a lista em um array no formato do grid
        grid_de_valores_interpolados = Interpolador.remodelando_valores_interpolados(dados,interpolacao.xi)
        minx, miny, maxx, maxy = interpolacao.pontos.obtem_geolimites()
  
        self.MplWidget.canvas.axes.clear()
        im = self.MplWidget.canvas.axes.imshow(grid_de_valores_interpolados, extent=(minx-5, maxx+5, miny-5, maxy+5), origin="lower", cmap=self.comboBoxPaletaCor.currentText())
        self.current_colorbar = self.MplWidget.canvas.figure.colorbar(im, ax=self.MplWidget.canvas.axes, orientation='horizontal')
        self.current_colorbar.set_label('Valores Interpolados')
        self.MplWidget.canvas.axes.set_title(self.comboBoxAlgoritmo.currentText())
        self.MplWidget.canvas.axes.set_xlabel("Latitude")
        self.MplWidget.canvas.axes.set_ylabel("Longitude")
        self.MplWidget.canvas.draw()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyterpolador"))
        self.label.setText(_translate("MainWindow", "PyTerpolator"))
        self.pushButton_menu_2.setText(_translate("MainWindow", "Info"))
        self.pushButton_menu_1.setText(_translate("MainWindow", "Interpolar"))
        self.label_8.setText(_translate("MainWindow", "Cor:"))
        self.comboBoxAlgoritmo.setItemText(0, _translate("MainWindow", "Vizinhos mais Próximos"))
        self.comboBoxAlgoritmo.setItemText(1, _translate("MainWindow", "Média dos Pontos"))
        self.comboBoxAlgoritmo.setItemText(2, _translate("MainWindow", "Inverso da Distância (IDW)"))
        self.pushButtonSalvarTif.setText(_translate("MainWindow", "Salvar Como (.TIF)"))
        self.label_5.setText(_translate("MainWindow", "Raio Horizontal"))
        self.label_2.setText(_translate("MainWindow", "Coluna de Dados"))
        self.comboBoxPotencia.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxPotencia.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxPotencia.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxPotencia.setItemText(3, _translate("MainWindow", "4"))
        self.pushButton_menu.setText(_translate("MainWindow", "Retornar ao Menu"))
        self.label_4.setText(_translate("MainWindow", "Algorítmo:"))
        self.pushButtonInterpolar.setText(_translate("MainWindow", "Interpolar"))
        self.label_3.setText(_translate("MainWindow", "Resolução Espacial (m)"))
        self.comboBoxPaletaCor.setItemText(0, _translate("MainWindow", "Oranges"))
        self.comboBoxPaletaCor.setItemText(1, _translate("MainWindow", "Greys"))
        self.comboBoxPaletaCor.setItemText(2, _translate("MainWindow", "Purples"))
        self.comboBoxPaletaCor.setItemText(3, _translate("MainWindow", "Blues"))
        self.comboBoxPaletaCor.setItemText(4, _translate("MainWindow", "Greens"))
        self.comboBoxPaletaCor.setItemText(5, _translate("MainWindow", "Reds"))
        self.comboBoxPaletaCor.setItemText(6, _translate("MainWindow", "YlOrBr"))
        self.comboBoxPaletaCor.setItemText(7, _translate("MainWindow", "YlOrRd"))
        self.comboBoxPaletaCor.setItemText(8, _translate("MainWindow", "YlGnBu"))
        self.comboBoxPaletaCor.setItemText(9, _translate("MainWindow", "PuBuGn"))
        self.comboBoxPaletaCor.setItemText(10, _translate("MainWindow", "BuGn"))
        self.comboBoxPaletaCor.setItemText(11, _translate("MainWindow", "YlGn"))
        self.comboBoxPaletaCor.setItemText(12, _translate("MainWindow", "viridis"))
        self.comboBoxPaletaCor.setItemText(13, _translate("MainWindow", "plasma"))
        self.comboBoxPaletaCor.setItemText(14, _translate("MainWindow", "inferno"))
        self.comboBoxPaletaCor.setItemText(15, _translate("MainWindow", "magma"))
        self.comboBoxPaletaCor.setItemText(16, _translate("MainWindow", "cividis"))
        self.comboBoxPaletaCor.setItemText(17, _translate("MainWindow", "PiYG"))
        self.comboBoxPaletaCor.setItemText(18, _translate("MainWindow", "PRGn"))
        self.comboBoxPaletaCor.setItemText(19, _translate("MainWindow", "BrBG"))
        self.comboBoxPaletaCor.setItemText(20, _translate("MainWindow", "PuOr"))
        self.comboBoxPaletaCor.setItemText(21, _translate("MainWindow", "RdGy"))
        self.comboBoxPaletaCor.setItemText(22, _translate("MainWindow", "RdBu"))
        self.comboBoxPaletaCor.setItemText(23, _translate("MainWindow", "RdYlBu"))
        self.comboBoxPaletaCor.setItemText(24, _translate("MainWindow", "RdYlGn"))
        self.comboBoxPaletaCor.setItemText(25, _translate("MainWindow", "Spectral"))
        self.comboBoxPaletaCor.setItemText(26, _translate("MainWindow", "coolwarm"))
        self.comboBoxPaletaCor.setItemText(28, _translate("MainWindow", "seismic"))
        self.pushButtonAbrirSHP.setText(_translate("MainWindow", "Abrir Arquivo (.shp)"))
        self.label_7.setText(_translate("MainWindow", "Potência (IDW)"))
        self.label_6.setText(_translate("MainWindow", "Raio Vertical"))

from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
