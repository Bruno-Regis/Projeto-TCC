
from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(900, 700)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(270, 150, 271, 81))
#         font = QtGui.QFont()
#         font.setFamily("ItalicT")
#         font.setPointSize(20)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.widget = QtWidgets.QWidget(self.centralwidget)
#         self.widget.setGeometry(QtCore.QRect(190, 270, 421, 30))
#         self.widget.setObjectName("widget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
#         self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.pushButton = QtWidgets.QPushButton(self.widget)
#         self.pushButton.setObjectName("pushButton")
#         self.horizontalLayout.addWidget(self.pushButton)
#         self.pushButton_2 = QtWidgets.QPushButton(self.widget)
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.horizontalLayout.addWidget(self.pushButton_2)
#         self.pushButton_3 = QtWidgets.QPushButton(self.widget)
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.horizontalLayout.addWidget(self.pushButton_3)
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#         self.page2 = QtWidgets.QWidget()
#         self.ui_page2 = Ui_Page2()
#         self.ui_page2.setupUi(self.page2)
#         self.stackedWidget.addWidget(self.page2)
#         self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "PyTerpolator"))
#         self.pushButton.setText(_translate("MainWindow", "Dúvidas"))
#         self.pushButton_2.setText(_translate("MainWindow", "Interpolar"))
#         self.pushButton_3.setText(_translate("MainWindow", "Sobre"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

import sys
from PyQt5 import QtWidgets, QtCore
from interpolargui import Ui_Page2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 150, 271, 81))
        font = QtGui.QFont()
        font.setFamily("ItalicT")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
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

        # Adicionando StackedWidget para navegação entre páginas
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 900, 700))
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.addWidget(self.centralwidget)

        # Adicionando Page2 ao StackedWidget
        self.page2 = QtWidgets.QWidget()
        self.ui_page2 = Ui_Page2()
        self.ui_page2.setupUi(self.page2)
        self.stackedWidget.addWidget(self.page2)

        # Conectando o botão 'Interpolar' à função que muda a página
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PyTerpolator"))
        self.pushButton.setText(_translate("MainWindow", "Dúvidas"))
        self.pushButton_2.setText(_translate("MainWindow", "Interpolar"))
        self.pushButton_3.setText(_translate("MainWindow", "Sobre"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
