from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog,QDialog, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QCheckBox
from osgeo import gdal
import geopandas as gpd
import os
import tempfile
import time
from controller.InterpolacaoController import InterpolacaoController
from view.Mplwidget import MplWidget

class TableWindow(QDialog):
    """
    Janela secundária para exibir a tabela de atributos do shapefile.
    """
    def __init__(self, shapefile_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tabela de Atributos")
        self.resize(800, 600)

        # Layout principal
        layout = QVBoxLayout(self)

        # Tabela
        self.table = QTableWidget(self)
        layout.addWidget(self.table)

        # Carregar o shapefile e exibir os dados na tabela
        self.carregar_dados(shapefile_path)

    def carregar_dados(self, shapefile_path):
        try:
            gdf = gpd.read_file(shapefile_path)

            # Configurar a tabela
            self.table.setRowCount(len(gdf))
            self.table.setColumnCount(len(gdf.columns))
            self.table.setHorizontalHeaderLabels(gdf.columns)

            # Preencher a tabela com os dados
            for i, row in gdf.iterrows():
                for j, value in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(str(value)))
        except Exception as e:
            print(f"Erro ao carregar o shapefile: {e}")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.current_colorbar = None
        self.dfn = None
        self.pontos_plotados = None
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
        self.label.setGeometry(QtCore.QRect(0, 100, 1191, 100))
        font = QtGui.QFont()
        font.setFamily("ItalicT")
        font.setPointSize(30)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("""
            background-color: #E8F5E9; /* Verde claro */
            color: #1B5E20; /* Verde escuro */
            border: 2px solid #A5D6A7; /* Verde suave */
            border-radius: 15px;
            padding: 10px;
            text-align: center;
        """)
        # Criando botões
        # Centralizando botões dinamicamente
        button_width = 150
        button_height = 40
        spacing = 20
        central_x = (1191 - (2 * button_width + spacing)) // 2
        central_y = 300

        self.pushButton_menu_2 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_menu_2.setGeometry(QtCore.QRect(central_x + button_width + spacing, central_y, button_width, button_height))
        self.pushButton_menu_2.setObjectName("pushButton_menu_2")
        self.pushButton_menu_2.setStyleSheet(
            "background-color: #4CAF50; color: white; font-weight: bold; border-radius: 10px;")
        self.pushButton_menu_1 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_menu_1.setGeometry(QtCore.QRect(central_x, central_y, button_width, button_height))
        self.pushButton_menu_1.setObjectName("pushButton_menu_1")
        self.pushButton_menu_1.setStyleSheet(
            "background-color: #4CAF50; color: white; font-weight: bold; border-radius: 10px;")
        self.stackedWidget.addWidget(self.page_1)


        # Criando os labels para o autor e o repositório no GitHub
        self.label_author = QtWidgets.QLabel(self.centralwidget)
        self.label_author.setGeometry(QtCore.QRect(10, 780, 300, 20))  # Posicionado no canto inferior esquerdo
        self.label_author.setObjectName("label_author")
        self.label_author.setStyleSheet("color: #4CAF50; font-size: 12px; font-style: italic;") 

        # Criando o label do repositório com link clicável
        self.label_repo = QtWidgets.QLabel(self.centralwidget)
        self.label_repo.setGeometry(QtCore.QRect(30, 800, 400, 20))  # Posicionado abaixo do label do autor
        self.label_repo.setObjectName("label_repo")
        self.label_repo.setStyleSheet("color: #1976D2; font-size: 12px;")
        self.label_repo.setText(
            '<a href="https://github.com/Bruno-Regis/Projeto-TCC" style="text-decoration: none; color: #1976D2;">'
            'GitHub: https://github.com/Bruno-Regis/Projeto-TCC</a>'
        )
        self.label_repo.setOpenExternalLinks(True)
        # Adicionando o ícone do GitHub ao lado do link
        self.icon_github = QtWidgets.QLabel(self.centralwidget)
        self.icon_github.setGeometry(QtCore.QRect(10, 800, 20, 20))  # Posicionado ao lado do link do GitHub
        self.icon_github.setObjectName(r"C:\dev\interpolador\View\icongithub.svg")
        pixmap = QPixmap("C:\dev\interpolador\View\icongithub.png") 
        self.icon_github.setPixmap(pixmap)
        self.icon_github.setScaledContents(True)  # Ajusta o tamanho do ícone ao label
# Configurando os textos dos labels
        self.label_author.setText("Desenvolvedor: Bruno Regis Borges da Costa Netto")
        self.label_repo.setText("Repositório: https://github.com/Bruno-Regis/Projeto-TCC")


        # Criando página 2
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        
        # Checkbox
        self.checkbox = QtWidgets.QCheckBox(self.page_2)
        self.checkbox.setGeometry(QtCore.QRect(10, 620, 131, 28))

        # Criando botõees
        self.pushButton_menu = QtWidgets.QPushButton(self.page_2)
        self.pushButton_menu.setGeometry(QtCore.QRect(10, 750, 131, 28))
        self.pushButton_menu.setObjectName("pushButton_menu")
        self.pushButtonInterpolar = QtWidgets.QPushButton(self.page_2)
        self.pushButtonInterpolar.setGeometry(QtCore.QRect(10, 580, 171, 28))
        self.pushButtonInterpolar.setObjectName("pushButtonInterpolar")
        self.pushButtonSalvarTif = QtWidgets.QPushButton(self.page_2)
        self.pushButtonSalvarTif.setGeometry(QtCore.QRect(600, 760, 161, 28))
        self.pushButtonSalvarTif.setObjectName("pushButtonSalvarTif")
        self.pushButtonAbrirSHP = QtWidgets.QPushButton(self.page_2)
        self.pushButtonAbrirSHP.setGeometry(QtCore.QRect(10, 10, 131, 28))
        self.pushButtonAbrirSHP.setObjectName("pushButtonAbrirSHP")
        self.pushButtonAbrirTB = QtWidgets.QPushButton(self.page_2)
        self.pushButtonAbrirTB.setGeometry(QtCore.QRect(10, 100, 171, 28))
        self.pushButtonAbrirTB.setObjectName("pushButtonAbrirTB")
        # Criando Combo Box
        self.comboBoxAlgoritmo = QtWidgets.QComboBox(self.page_2)
        self.comboBoxAlgoritmo.setGeometry(QtCore.QRect(10, 280, 171, 22))
        self.comboBoxAlgoritmo.setObjectName("comboBoxAlgoritmo")
        self.comboBoxAlgoritmo.addItem("")
        self.comboBoxAlgoritmo.addItem("")
        self.comboBoxAlgoritmo.addItem("")
        self.comboBoxPotencia = QtWidgets.QComboBox(self.page_2)
        self.comboBoxPotencia.setGeometry(QtCore.QRect(10, 460, 171, 22))
        self.comboBoxPotencia.setObjectName("comboBoxPotencia")
        self.comboBoxPotencia.addItem("")
        self.comboBoxPotencia.addItem("")
        self.comboBoxPotencia.addItem("")
        self.comboBoxPotencia.addItem("")
        self.comboBoxPaletaCor = QtWidgets.QComboBox(self.page_2)
        self.comboBoxPaletaCor.setGeometry(QtCore.QRect(10, 520, 171, 22))
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
        self.doubleSpinBoxRaioa.setGeometry(QtCore.QRect(10, 340, 131, 22))
        self.doubleSpinBoxRaioa.setObjectName("doubleSpinBoxRaioa")
        self.doubleSpinBoxRaioa.setMaximum(100000)
        self.doubleSpinBoxRaiob = QtWidgets.QDoubleSpinBox(self.page_2)
        self.doubleSpinBoxRaiob.setGeometry(QtCore.QRect(10, 400, 131, 22))
        self.doubleSpinBoxRaiob.setObjectName("doubleSpinBoxRaiob")
        self.doubleSpinBoxRaiob.setMaximum(100000)
        self.doubleSpinBoxResolucao = QtWidgets.QDoubleSpinBox(self.page_2)
        self.doubleSpinBoxResolucao.setGeometry(QtCore.QRect(10, 220, 131, 22))
        self.doubleSpinBoxResolucao.setObjectName("doubleSpinBoxResolucao")
        self.doubleSpinBoxResolucao.setMaximum(100000)
        # Criando Line Edit
        self.lineEditColunaDados = QtWidgets.QLineEdit(self.page_2)
        self.lineEditColunaDados.setGeometry(QtCore.QRect(10, 160, 171, 22))
        self.lineEditColunaDados.setObjectName("lineEditColunaDados")
        self.lineEditCaminho = QtWidgets.QLineEdit(self.page_2)
        self.lineEditCaminho.setGeometry(QtCore.QRect(10, 45, 171, 22))
        self.lineEditCaminho.setObjectName("lineEdit")
        # Criando Labels
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(10, 320, 171, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(10, 380, 131, 16))
        self.label_6.setObjectName("label_6")        
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(10, 430, 101, 16))
        self.label_7.setObjectName("label_7")
        self.label_sistcoord = QtWidgets.QLabel(self.page_2)
        self.label_sistcoord.setGeometry(QtCore.QRect(10, 75, 151, 16))
        self.label_sistcoord.setObjectName("label_EPSG")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(10, 500, 41, 16))
        self.label_8.setObjectName("label_8")

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
        self.menubar.setGeometry(QtCore.QRect(10, 750, 1192, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_menu3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_menu3.setGeometry(QtCore.QRect(10, 750, 131, 28))
        self.pushButton_menu3.setObjectName("pushButton_menu3")
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Título
        self.label_theory_title = QtWidgets.QLabel(self.page_3)
        self.label_theory_title.setGeometry(QtCore.QRect(300, 20, 600, 60))
        self.label_theory_title.setStyleSheet("font-size: 24px; font-weight: bold; color: #4CAF50; text-align: center;")
        self.label_theory_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_theory_title.setText("Métodos disponíves na versão")

        # Seção: Vizinhos Mais Próximos
        self.label_theory_nearest = QtWidgets.QLabel(self.page_3)
        self.label_theory_nearest.setGeometry(QtCore.QRect(50, 130, 1090, 60)) 
        self.label_theory_nearest.setStyleSheet("font-size: 14px; color: #000; font-weight: bold;")
        self.label_theory_nearest.setText("1. Vizinhos Mais Próximos:")
        self.label_theory_nearest_description = QtWidgets.QLabel(self.page_3)
        self.label_theory_nearest_description.setGeometry(QtCore.QRect(50, 160, 1090, 80))
        self.label_theory_nearest_description.setStyleSheet("font-size: 12px; color: #000;")
        self.label_theory_nearest_description.setWordWrap(True)
        self.label_theory_nearest_description.setText(
            "Este método utiliza o valor do ponto mais próximo para representar os dados desconhecidos (SAMET, 1990)."
        )

        # Seção: IDW
        self.label_theory_idw = QtWidgets.QLabel(self.page_3)
        self.label_theory_idw.setGeometry(QtCore.QRect(50, 440, 1090, 60))
        self.label_theory_idw.setStyleSheet("font-size: 14px; color: #000; font-weight: bold;")
        self.label_theory_idw.setText("3. Inverso da Distância Ponderada (IDW):")
        self.label_theory_idw_description = QtWidgets.QLabel(self.page_3)
        self.label_theory_idw_description.setGeometry(QtCore.QRect(50, 470, 1090, 80))
        self.label_theory_idw_description.setStyleSheet("font-size: 12px; color: #000;")
        self.label_theory_idw_description.setWordWrap(True)
        self.label_theory_idw_description.setText(
            "ermite inferir peso aos pontos que se encontram mais próximos e diminuir o peso à medida que a distância aumenta em função do parâmetro de potência (RIGHI; BASSO,2016)."
        )


        #Seção equação IDW
        self.label_eq_idw = QtWidgets.QLabel(self.page_3)
        self.label_eq_idw.setGeometry(QtCore.QRect(50, 510, 1090, 60))
        self.label_eq_idw.setStyleSheet("font-size: 14px; color: #000; font-weight: bold;")
        self.label_eq_idw.setText("Equação IDW:")

        # Equação idw imagem
        self.label_eq_elipse = QtWidgets.QLabel(self.page_3)
        self.label_eq_elipse.setGeometry(QtCore.QRect(50, 560, 386, 65))
        self.label_eq_elipse.setPixmap(QPixmap("C:\dev\interpolador\View\idw_eq.png"))
        self.label_eq_elipse.setScaledContents(True)  # Ajusta a imagem ao tamanho do QLabel
        

        self.label_theory_idw = QtWidgets.QLabel(self.page_3)
        self.label_theory_idw.setGeometry(QtCore.QRect(50, 630, 1090, 100))
        self.label_theory_idw.setStyleSheet("font-size: 12px; color: #000;")
        self.label_theory_idw.setWordWrap(True)
        self.label_theory_idw.setText(
            """
            <p><b>Onde:</b></p>
            <ul>
                <li><i>Ẑ(x)</i> : Valor interpolado no ponto</li>
                <li><i>Z(x<sub>i</sub>)</i> : Valor conhecido no ponto <i>x<sub>i</sub></i></li>
                <li><i>d<sub>ij</sub></i> : Distância entre os pontos <i>i</i> e <i>j</i></li>
                <li><i>p</i> : Parâmetro de potência</li>
                <li><i>n</i> : Número de pontos conhecidos usados</li>
            </ul>
            """
        )

        #Seção: Média Móvel
        self.label_theory_moving_avg = QtWidgets.QLabel(self.page_3)
        self.label_theory_moving_avg.setGeometry(QtCore.QRect(50, 200, 1090, 60))
        self.label_theory_moving_avg.setStyleSheet("font-size: 14px; color: #000; font-weight: bold;")
        self.label_theory_moving_avg.setText("2. Média Móvel dos Pontos:")
        self.label_theory_moving_avg_description = QtWidgets.QLabel(self.page_3)
        self.label_theory_moving_avg_description.setGeometry(QtCore.QRect(50, 230, 1090, 80))
        self.label_theory_moving_avg_description.setStyleSheet("font-size: 12px; color: #000;")
        self.label_theory_moving_avg_description.setWordWrap(True)
        self.label_theory_moving_avg_description.setText(
            "Este método interpola os dados baseados na média dos valores dos pontos conhecidos dentro de"
            " uma elipse com raios a e b onde o ponto central da elipse corresponde à coordenada do ponto"
            " a ser interpolado (CAMPOS, 2018)."          
        )

        #Seção equação da elipse
        self.label_theory_elipse = QtWidgets.QLabel(self.page_3)
        self.label_theory_elipse.setGeometry(QtCore.QRect(50, 270, 1090, 60))
        self.label_theory_elipse.setStyleSheet("font-size: 14px; color: #000; font-weight: bold;")
        self.label_theory_elipse.setText("Equação da Elipse (OLIVEIRA, 2024):")
        # Equação da elipse imagem
        self.label_eq_elipse = QtWidgets.QLabel(self.page_3)
        self.label_eq_elipse.setGeometry(QtCore.QRect(50, 310, 297, 50))
        self.label_eq_elipse.setPixmap(QPixmap("C:\dev\interpolador\View\ellipse_eq.png"))
        self.label_eq_elipse.setScaledContents(True)  # Ajusta a imagem ao tamanho do QLabel

        self.label_theory_elipse = QtWidgets.QLabel(self.page_3)
        self.label_theory_elipse.setGeometry(QtCore.QRect(50, 360, 1090, 100))
        self.label_theory_elipse.setStyleSheet("font-size: 12px; color: #000;")
        self.label_theory_elipse.setWordWrap(True)
        self.label_theory_elipse.setText(
            """
            <p><b>Onde:</b></p>
            <ul>
                <li><i>(i, j)</i> : Coordenadas do centro da elipse</li>
                <li><i>a</i> : Semi-eixo maior</li>
                <li><i>b</i> : Semi-eixo menor</li>
                <li><i>(x, y)</i> : Coordenadas de um ponto qualquer</li>
            </ul>
            """
        )

        # Atribuindo métodos aos botões
        self.pushButton_menu_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_menu_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_menu.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_menu3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButtonInterpolar.clicked.connect(self.cria_grafico)
        self.pushButtonAbrirTB.clicked.connect(self.mostrar_tabela)
        self.checkbox.toggled.connect(self.atualiza_estado)
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


    def carregarshapefile(self):
        path = self.lineEditCaminho.text()
        gdf = gpd.read_file(path)
        self.mostrar_tabela(gdf)

    def mostrar_tabela(self):
        self.table_window = TableWindow(self.lineEditCaminho.text())
        self.table_window.exec_()

    def obtem_caminho_arquivo(self):
        caminho_arquivo, _ = QFileDialog.getOpenFileName(None,
        "Selecione um arquivo",
        "",  # Diretório inicial
        "(*.shp)")
        self.lineEditCaminho.setText(caminho_arquivo)
        if self.lineEditCaminho.text() != "":
            self.escreve_epsg()
        else:
            self.show_message("Nenhum Arquivo selecionado")

    def obtem_pontos(self):
        path = self.lineEditCaminho.text()
        return gpd.read_file(path)
    
    def obtem_header(self):
        path = self.lineEditCaminho.text()
        pontos = gpd.read_file(path)
        return pontos.columns

    def escreve_epsg(self):
        path = self.lineEditCaminho.text()
        pontos = gpd.read_file(path)
        epsg = str(pontos.crs.to_epsg())
        self.label_sistcoord.setText("EPSG: " + epsg)

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
    
    def save_file(self, file_path):
        self.file_path = file_path
        InterpolacaoController.transforma_TIFF(self.dfn,self.file_path)
    
    def define_algoritmo(self):

        #Determinando algoritmo escolhido na comboBox
        if self.comboBoxAlgoritmo.currentText() == "Vizinhos mais Próximos":
            algoritmo = "Vizinhos" 
        elif self.comboBoxAlgoritmo.currentText() == "Média dos Pontos":
            algoritmo = "Media" 
        elif self.comboBoxAlgoritmo.currentText() == "Inverso da Distância (IDW)":
            algoritmo = "IDW"
        return algoritmo
    
    def atualiza_estado(self, estado):
        if estado:  # Se o checkbox estiver marcado
            self.plota_pontos()
        else:  # Se o checkbox estiver desmarcado
            self.remove_pontos()

    def plota_pontos(self):
        pontos = self.obtem_pontos()
        # Extraindo as coordenadas X e Y dos pontos
        x_coords = pontos.geometry.x
        y_coords = pontos.geometry.y       
        # Plotando os pontos sobre o gráfico
        self.pontos_plotados = self.MplWidget.canvas.axes.scatter(x_coords, y_coords, color='blue', marker='o', s= 8,  label='Pontos amostrais')
        self.MplWidget.canvas.axes.set_title(self.comboBoxAlgoritmo.currentText())
        self.MplWidget.canvas.axes.set_xlabel("Latitude")
        self.MplWidget.canvas.axes.set_ylabel("Longitude")
        self.MplWidget.canvas.axes.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0., title="Legenda")
        self.MplWidget.canvas.draw()
            
    def remove_pontos(self):
        if self.pontos_plotados is not None:
            self.pontos_plotados.remove()  # Remove os pontos do gráfico
            self.pontos_plotados = None  # Limpa a referência
            self.MplWidget.canvas.axes.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
            self.MplWidget.canvas.draw()  # Atualiza o gráfico
        else:
            self.show_message("Nenhum ponto para remover.")
                
    def cria_grafico(self):
        if self.current_colorbar is not None:
            self.current_colorbar.remove()
            self.current_colorbar = None

        coluna_de_interpolacao = self.lineEditColunaDados.text()
        header = self.obtem_header()
        if coluna_de_interpolacao in header:
        
            algoritmo = self.define_algoritmo()
            #Instanciando objeto de interpolação
            interpolacao = InterpolacaoController(self.lineEditCaminho.text(), self.lineEditColunaDados.text(), algoritmo, self.doubleSpinBoxResolucao.value(),
                                        self.doubleSpinBoxRaioa.value(), self.doubleSpinBoxRaiob.value(),int(self.comboBoxPotencia.currentText()))
            #Interpolando com o método interpolar
            dados = interpolacao.interpolar()
            print("vou instanciar objeto ao self objeto")
            self.latitude_pixels = interpolacao.latitude_pixels
            self.longitude_pixels = interpolacao.longitude_pixels
            self.valores_z = dados
            self.dfn = interpolacao.gera_data_frame_de_dados()
            #Remodelando a lista em um array no formato do grid
            grid_de_valores_interpolados = InterpolacaoController.cria_grid(dados,interpolacao.xi)
            minx, miny, maxx, maxy = interpolacao.pontos.obtem_geolimites()

            #Plotando a imagem

            # resolucao = self.doubleSpinBoxResolucao.value()
            # minx = round(minx / resolucao) * resolucao
            # miny = round(miny / resolucao) * resolucao
            # maxx = round(maxx / resolucao) * resolucao
            # maxy = round(maxy / resolucao) * resolucao


            self.MplWidget.canvas.axes.clear()
            im = self.MplWidget.canvas.axes.imshow(grid_de_valores_interpolados, extent=(minx, maxx,
                                                                                        miny, maxy),
                                                                                            origin="lower", cmap=self.comboBoxPaletaCor.currentText())
            
            #Plotando a barra de cores
            self.current_colorbar = self.MplWidget.canvas.figure.colorbar(im, ax=self.MplWidget.canvas.axes, orientation='horizontal')
            self.current_colorbar.set_label('Valores Interpolados')

            
            self.MplWidget.canvas.axes.set_title(self.comboBoxAlgoritmo.currentText())
            self.MplWidget.canvas.axes.set_xlabel("Latitude")
            self.MplWidget.canvas.axes.set_ylabel("Longitude")
            self.MplWidget.canvas.draw()
        else:
            self.show_message("Coluna inexistente na tabela de atributos")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pyterpolador"))
        self.label.setText(_translate("MainWindow", "PyTerpolator"))
        self.pushButton_menu_2.setText(_translate("MainWindow", "Info"))
        self.pushButton_menu_1.setText(_translate("MainWindow", "Interpolar"))
        self.pushButton_menu3.setText(_translate("MainWindow", "Retornar ao Menu"))
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
        self.label_4.setText(_translate("MainWindow", "Algoritmo:"))
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
        self.pushButtonAbrirTB.setText(_translate("MainWindow", "Abrir Tabela de atributos"))
        self.checkbox.setText(_translate("MainWindow", "Plotar Pontos"))
        self.label_7.setText(_translate("MainWindow", "Potência (IDW)"))
        self.label_6.setText(_translate("MainWindow", "Raio Vertical"))
