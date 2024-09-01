from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.label1 = QtWidgets.QLabel(self.page1)
        self.label1.setGeometry(QtCore.QRect(270, 150, 271, 81))
        font = QtGui.QFont()
        font.setFamily("ItalicT")
        font.setPointSize(20)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label1.setText("PyTerpolator")
        self.stackedWidget.addWidget(self.page1)

        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.label2 = QtWidgets.QLabel(self.page2)
        self.label2.setGeometry(QtCore.QRect(270, 150, 271, 81))
        font.setPointSize(20)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label2.setText("Página de Dúvidas")
        self.stackedWidget.addWidget(self.page2)

        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.label3 = QtWidgets.QLabel(self.page3)
        self.label3.setGeometry(QtCore.QRect(270, 150, 271, 81))
        font.setPointSize(20)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label3.setText("Página de Interpolação")
        self.stackedWidget.addWidget(self.page3)

        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.label4 = QtWidgets.QLabel(self.page4)
        self.label4.setGeometry(QtCore.QRect(270, 150, 271, 81))
        font.setPointSize(20)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.label4.setText("Página Sobre")
        self.stackedWidget.addWidget(self.page4)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(190, 270, 421, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Conectar botões às funções
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Dúvidas"))
        self.pushButton_2.setText(_translate("MainWindow", "Interpolar"))
        self.pushButton_3.setText(_translate("MainWindow", "Sobre"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())