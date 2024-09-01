
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from osgeo import gdal
import os
import tempfile
import time
from interp import Interpolador
from mplwidget import MplWidget
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.current_colorbar = None
        self.dfn = None
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(900, 700)
        MainWindow.showMaximized()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Labels
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 171, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 330, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 390, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 450, 41, 16))
        self.label_8.setObjectName("label_8")
        
        #Line Edits
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 171, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2_coluna_dados = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2_coluna_dados.setGeometry(QtCore.QRect(10, 110, 171, 22))
        self.lineEdit_2_coluna_dados.setObjectName("lineEdit_2_coluna_dados")
        
        #SpinBox
        self.doubleSpinBox_resolucao = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_resolucao.setGeometry(QtCore.QRect(10, 170, 131, 22))
        self.doubleSpinBox_resolucao.setObjectName("doubleSpinBox_resolucao")
        self.doubleSpinBox_resolucao.setMaximum(100000)

        self.doubleSpinBox_2_raioa = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2_raioa.setGeometry(QtCore.QRect(10, 290, 131, 22))
        self.doubleSpinBox_2_raioa.setObjectName("doubleSpinBox_2_raioa")
        self.doubleSpinBox_2_raioa.setMaximum(100000)

        self.doubleSpinBox_3_raiob = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_3_raiob.setGeometry(QtCore.QRect(10, 350, 131, 22))
        self.doubleSpinBox_3_raiob.setObjectName("doubleSpinBox_3_raiob")
        self.doubleSpinBox_3_raiob.setMaximum(100000)
        
        #ComboBox
        #ComboBox escolhe algoritmo
        self.comboBox_algoritmo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_algoritmo.setGeometry(QtCore.QRect(10, 230, 171, 22))
        self.comboBox_algoritmo.setObjectName("comboBox_algoritmo")
        self.comboBox_algoritmo.addItem("")
        self.comboBox_algoritmo.addItem("")
        self.comboBox_algoritmo.addItem("")

        #ComboBox escolhe potencia do algoritmo IDW
        self.comboBox_2_potencia = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2_potencia.setGeometry(QtCore.QRect(10, 410, 171, 22))
        self.comboBox_2_potencia.setObjectName("comboBox_2_potencia")
        self.comboBox_2_potencia.addItem("")
        self.comboBox_2_potencia.addItem("")
        self.comboBox_2_potencia.addItem("")
        self.comboBox_2_potencia.addItem("")

        #ComboBox escolhe palheta de cores
        self.comboBox_3_cor = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3_cor.setGeometry(QtCore.QRect(10, 470, 171, 22))
        self.comboBox_3_cor.setObjectName("comboBox_3_cor")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        self.comboBox_3_cor.addItem("")
        
        #PushButtons
        #Botão retorna ao Menu
        self.pushButton_menu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_menu.setGeometry(QtCore.QRect(10, 610, 61, 28))
        self.pushButton_menu.setObjectName("pushButton_menu")
        #Botão salva arquivo como tif
        self.pushButton_2_salvarfile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_salvarfile.setGeometry(QtCore.QRect(460, 620, 161, 28))
        self.pushButton_2_salvarfile.setObjectName("pushButton_2_salvarfile")
        #Botão busca caminho do arquivo
        self.pushButton_abrirfile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_abrirfile.setGeometry(QtCore.QRect(10, 10, 131, 28))
        self.pushButton_abrirfile.setObjectName("pushButton_abrirfile")
        #Botão Interpolar
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 540, 171, 28))
        self.pushButton.setObjectName("pushButton")
 
        #Cria Widget Figura
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(190, 0, 701, 621))
        self.MplWidget.setObjectName("MplWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #Conectando métodos aos botões
        #Botão interpolar que plota o gráfico
        self.pushButton.clicked.connect(self.atualiza_grafico)
        #Botão obtem caminho do arquivo
        self.pushButton_abrirfile.clicked.connect(self.obtem_caminho_arquivo)
        #Botão converte gráfico em tif e salva no caminho escolhido
        self.pushButton_2_salvarfile.clicked.connect(self.show_save_dialog)

    def obtem_caminho_arquivo(self):
        caminho_arquivo, _ = QFileDialog.getOpenFileName(None,
        "Selecione um arquivo",
        "",  # Diretório inicial
        "(*.shp)")
        self.lineEdit.setText(caminho_arquivo)
    
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
            gdal.Translate(self.file_path, temp_dataset, outputSRS="EPSG:31983", xRes=self.doubleSpinBox_resolucao.value(),
                            yRes=self.doubleSpinBox_resolucao.value())
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
        
    # +".tif"
    def save_file(self, file_path):
        print("vou começar os trabalhos aqui...")
        self.file_path = file_path
        Interpolador.transforma_TIFF(self.dfn,self.file_path)
    

    def define_algoritmo(self):
        #Determinando algoritmo escolhido na comboBox
        if self.comboBox_algoritmo.currentText() == "Vizinhos mais Próximos":
            algoritmo = "Vizinhos" 
        elif self.comboBox_algoritmo.currentText() == "Média dos Pontos":
            algoritmo = "Media" 
        elif self.comboBox_algoritmo.currentText() == "Inverso da Distância (IDW)":
            algoritmo = "IDW"
        return algoritmo

    def atualiza_grafico(self):
        
        if self.current_colorbar is not None:
            self.current_colorbar.remove()
            self.current_colorbar = None

        algoritmo = self.define_algoritmo()

        #Instanciando objeto de interpolação
        interpolacao = Interpolador(self.lineEdit.text(), self.lineEdit_2_coluna_dados.text(), algoritmo, self.doubleSpinBox_resolucao.value(),
                                     self.doubleSpinBox_2_raioa.value(), self.doubleSpinBox_3_raiob.value(),int(self.comboBox_2_potencia.currentText()))
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
        im = self.MplWidget.canvas.axes.imshow(grid_de_valores_interpolados, extent=(minx-5, maxx+5, miny-5, maxy+5), origin="lower", cmap=self.comboBox_3_cor.currentText())
        self.current_colorbar = self.MplWidget.canvas.figure.colorbar(im, ax=self.MplWidget.canvas.axes, orientation='horizontal')
        self.current_colorbar.set_label('Valores Interpolados')
        self.MplWidget.canvas.axes.set_title(self.comboBox_algoritmo.currentText())
        self.MplWidget.canvas.draw()

        #self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Coluna de Dados"))
        self.label_3.setText(_translate("MainWindow", "Resolução Espacial (m)"))
        self.label_4.setText(_translate("MainWindow", "Algorítmo:"))
        self.comboBox_algoritmo.setItemText(0, _translate("MainWindow", "Vizinhos mais Próximos"))
        self.comboBox_algoritmo.setItemText(1, _translate("MainWindow", "Média dos Pontos"))
        self.comboBox_algoritmo.setItemText(2, _translate("MainWindow", "Inverso da Distância (IDW)"))
        self.label_5.setText(_translate("MainWindow", "Raio Horizontal"))
        self.label_6.setText(_translate("MainWindow", "Raio Vertical"))
        self.label_7.setText(_translate("MainWindow", "Potência (IDW)"))
        self.label_8.setText(_translate("MainWindow", "Cor:"))
        self.comboBox_2_potencia.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2_potencia.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2_potencia.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2_potencia.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_3_cor.setItemText(0, _translate("MainWindow", "Oranges"))
        self.comboBox_3_cor.setItemText(1, _translate("MainWindow", "Greys"))
        self.comboBox_3_cor.setItemText(2, _translate("MainWindow", "Purples"))
        self.comboBox_3_cor.setItemText(3, _translate("MainWindow", "Blues"))
        self.comboBox_3_cor.setItemText(4, _translate("MainWindow", "Greens"))
        self.comboBox_3_cor.setItemText(5, _translate("MainWindow", "Reds"))
        self.comboBox_3_cor.setItemText(6, _translate("MainWindow", "YlOrBr"))
        self.comboBox_3_cor.setItemText(7, _translate("MainWindow", "YlOrRd"))
        self.comboBox_3_cor.setItemText(8, _translate("MainWindow", "YlGnBu"))
        self.comboBox_3_cor.setItemText(9, _translate("MainWindow", "PuBuGn"))
        self.comboBox_3_cor.setItemText(10, _translate("MainWindow", "BuGn"))
        self.comboBox_3_cor.setItemText(11, _translate("MainWindow", "YlGn"))
        self.comboBox_3_cor.setItemText(12, _translate("MainWindow", "viridis"))
        self.comboBox_3_cor.setItemText(13, _translate("MainWindow", "plasma"))
        self.comboBox_3_cor.setItemText(14, _translate("MainWindow", "inferno"))
        self.comboBox_3_cor.setItemText(15, _translate("MainWindow", "magma"))
        self.comboBox_3_cor.setItemText(16, _translate("MainWindow", "cividis"))
        self.comboBox_3_cor.setItemText(17, _translate("MainWindow", "PiYG"))
        self.comboBox_3_cor.setItemText(18, _translate("MainWindow", "PRGn"))
        self.comboBox_3_cor.setItemText(19, _translate("MainWindow", "BrBG"))
        self.comboBox_3_cor.setItemText(20, _translate("MainWindow", "PuOr"))
        self.comboBox_3_cor.setItemText(21, _translate("MainWindow", "RdGy"))
        self.comboBox_3_cor.setItemText(22, _translate("MainWindow", "RdBu"))
        self.comboBox_3_cor.setItemText(23, _translate("MainWindow", "RdYlBu"))
        self.comboBox_3_cor.setItemText(24, _translate("MainWindow", "RdYlGn"))
        self.comboBox_3_cor.setItemText(25, _translate("MainWindow", "Spectral"))
        self.comboBox_3_cor.setItemText(26, _translate("MainWindow", "coolwarm"))
        self.comboBox_3_cor.setItemText(28, _translate("MainWindow", "seismic"))
        self.pushButton_menu.setText(_translate("MainWindow", "Menu"))
        self.pushButton_2_salvarfile.setText(_translate("MainWindow", "Salvar Como (.TIF)"))
        self.pushButton_abrirfile.setText(_translate("MainWindow", "Abrir Arquivo (.shp)"))
        self.pushButton.setText(_translate("MainWindow", "Interpolar"))
from mplwidget import MplWidget


# if __name__ == "__main__":

# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()
# sys.exit(app.exec_())
