# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Progs/router/patcher/iot-patcher.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 750)
        MainWindow.setStyleSheet("color:rgb(255, 176, 251);\n" "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabswitcher = QtWidgets.QTabWidget(self.centralwidget)
        self.tabswitcher.setGeometry(QtCore.QRect(-10, 0, 711, 700))
        self.tabswitcher.setMaximumSize(QtCore.QSize(711, 700))
        self.tabswitcher.setMovable(True)
        self.tabswitcher.setObjectName("tabswitcher")
        self.options = QtWidgets.QWidget()
        self.options.setObjectName("options")
        self.firmpathsel = QtWidgets.QPushButton(self.options)
        self.firmpathsel.setGeometry(QtCore.QRect(520, 10, 180, 30))
        self.firmpathsel.setAutoFillBackground(False)
        self.firmpathsel.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(112, 119, 255);")
        self.firmpathsel.setObjectName("firmpathsel")
        self.outpathsel = QtWidgets.QPushButton(self.options)
        self.outpathsel.setGeometry(QtCore.QRect(520, 50, 180, 30))
        self.outpathsel.setAutoFillBackground(False)
        self.outpathsel.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(112, 119, 255);")
        self.outpathsel.setObjectName("outpathsel")
        self.firmpath = QtWidgets.QLabel(self.options)
        self.firmpath.setGeometry(QtCore.QRect(10, 50, 500, 30))
        self.firmpath.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(112, 119, 255);")
        self.firmpath.setText("")
        self.firmpath.setObjectName("firmpath")
        self.outpath = QtWidgets.QLabel(self.options)
        self.outpath.setGeometry(QtCore.QRect(10, 10, 500, 30))
        self.outpath.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(112, 119, 255);")
        self.outpath.setText("")
        self.outpath.setObjectName("outpath")
        self.tabswitcher.addTab(self.options, "")
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.logfield = QtWidgets.QTextEdit(self.log)
        self.logfield.setGeometry(QtCore.QRect(10, 0, 690, 620))
        self.logfield.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.logfield.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.logfield.setObjectName("logfield")
        self.savelog = QtWidgets.QPushButton(self.log)
        self.savelog.setGeometry(QtCore.QRect(10, 625, 80, 30))
        self.savelog.setObjectName("savelog")
        self.copylog = QtWidgets.QPushButton(self.log)
        self.copylog.setGeometry(QtCore.QRect(100, 625, 80, 30))
        self.copylog.setObjectName("copylog")
        self.tabswitcher.addTab(self.log, "")
        self.vulnerabilities = QtWidgets.QWidget()
        self.vulnerabilities.setObjectName("vulnerabilities")
        self.tabswitcher.addTab(self.vulnerabilities, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabswitcher.setCurrentIndex(0)
        self.firmpathsel.clicked.connect(MainWindow.clicked) # type: ignore
        self.outpathsel.clicked.connect(MainWindow.clicked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IOT-patcher"))
        self.firmpathsel.setText(_translate("MainWindow", "Select path to firmware"))
        self.outpathsel.setText(_translate("MainWindow", "Select path to output folder"))
        self.tabswitcher.setTabText(self.tabswitcher.indexOf(self.options), _translate("MainWindow", "Options"))
        self.savelog.setText(_translate("MainWindow", "Save log"))
        self.copylog.setText(_translate("MainWindow", "Copy log"))
        self.tabswitcher.setTabText(self.tabswitcher.indexOf(self.log), _translate("MainWindow", "Log"))
        self.tabswitcher.setTabText(self.tabswitcher.indexOf(self.vulnerabilities), _translate("MainWindow", "Vulnerabilities"))
app = setupUi(sys.argv)
myWindow = Ui_MainWindow(None)
myWindow.show()
app.exec_()