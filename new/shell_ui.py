# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shell_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("checkmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(1993, 12, 25))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 3, 1, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 3)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 5, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout_3.addWidget(self.listWidget_3, 1, 0, 1, 1)
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_4.setObjectName("listWidget_4")
        self.gridLayout_3.addWidget(self.listWidget_4, 1, 1, 1, 1)
        self.listWidget_5 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_5.setObjectName("listWidget_5")
        self.gridLayout_3.addWidget(self.listWidget_5, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 6, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menubar.addAction(self.menu.menuAction())
        self.label_3.setBuddy(self.lineEdit_3)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label.setBuddy(self.lineEdit)
        self.label_4.setBuddy(self.dateEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.dateEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Приём Врача"))
        self.label_3.setText(_translate("MainWindow", "Отчество"))
        self.label_2.setText(_translate("MainWindow", "Имя"))
        self.label.setText(_translate("MainWindow", "Фамилия"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.label_4.setText(_translate("MainWindow", "Дата рождения"))
        self.label_7.setText(_translate("MainWindow", "Выбор папки для сохранения"))
        self.pushButton_2.setText(_translate("MainWindow", "Начать приём"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.groupBox.setTitle(_translate("MainWindow", "Тип обследования"))
        self.label_8.setText(_translate("MainWindow", "Тип приёма"))
        self.label_9.setText(_translate("MainWindow", "Тип протокола"))
        self.label_10.setText(_translate("MainWindow", "Выбранные обследования"))
        self.pushButton.setText(_translate("MainWindow", "Закрыть программу"))
        self.pushButton_4.setText(_translate("MainWindow", "Записаться на приём"))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.action.setText(_translate("MainWindow", "Выбор папок"))
        self.action_3.setText(_translate("MainWindow", "Выход"))
        self.action_2.setText(_translate("MainWindow", "Выход"))

