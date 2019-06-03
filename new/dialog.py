#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from dialog_shell_ui import Ui_Dialog
import sys
import json

class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        super(MyDialog, self).__init__(parent)
        #super().__init__()
        #QtWidgets.QWidget.__init__(self, parent)
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(self)

        self.dialog_ui.buttonBox.rejected.connect(self.close)
        self.dialog_ui.buttonBox.accepted.connect(self.saveConfig)
        self.dialog_ui.toolButton.clicked.connect(self.selectDirectory)
        self.dialog_ui.toolButton_2.clicked.connect(self.selectDirectory)
        self.dialog_ui.toolButton_3.clicked.connect(self.selectDirectory)
        self.dialog_ui.toolButton_4.clicked.connect(self.selectDirectory)
        self.dialog_ui.lineEdit.textChanged.connect(self.enableSaveConfig)
        self.dialog_ui.lineEdit_2.textChanged.connect(self.enableSaveConfig)
        self.dialog_ui.lineEdit_3.textChanged.connect(self.enableSaveConfig)
        self.dialog_ui.lineEdit_4.textChanged.connect(self.enableSaveConfig)

        # self.dialog_ui.buttonBox.Cancel.clicked.connect(self.close)
        # self.dialog_ui.buttonBox.Save.clicked.connect(self.saveConfig)

    def saveConfig(self):
        settings = {  
            'Доктора': self.dialog_ui.lineEdit.text(),
            'Протоколы УЗИ': self.dialog_ui.lineEdit_2.text(),
            'Сосуды': self.dialog_ui.lineEdit_3.text(),
            'Пациенты': self.dialog_ui.lineEdit_4.text()
        }
        # settings = json.dumps(settings).decode('unicode-escape').encode('utf8')
        with open('settings.json', 'w') as json_file:  
            json.dump(settings, json_file, ensure_ascii=False)

    def enableSaveConfig(self):
        if (self.dialog_ui.lineEdit.text() != '' and
            self.dialog_ui.lineEdit_2.text() != '' and
            self.dialog_ui.lineEdit_3.text() != '' and
            self.dialog_ui.lineEdit_4.text() != ''):
            self.dialog_ui.buttonBox.setEnabled(True)

    
    def selectDirectory(self):
        print(self.sender().objectName(),'toolButton')
        directory=QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if (directory):
            if (self.sender().objectName()=='toolButton'):
                self.dialog_ui.lineEdit.setText(directory)
            elif (self.sender().objectName()=='toolButton_2'):
                self.dialog_ui.lineEdit_2.setText(directory)
            elif (self.sender().objectName()=='toolButton_3'):
                self.dialog_ui.lineEdit_3.setText(directory)
            elif (self.sender().objectName()=='toolButton_4'):
                self.dialog_ui.lineEdit_4.setText(directory)

# app = QtWidgets.QApplication(sys.argv)
# window = QtWidgets.QWidget()
# window.setWindowTitle("Класс QDialog")
# window.resize(300, 70)

# button = QtWidgets.QPushButton("Отобразить диалоговое окно...")
# button.clicked.connect(on_clicked)

# box = QtWidgets.QVBoxLayout()
# box.addWidget(button)
# window.setLayout(box)

# window.show()
# sys.exit(app.exec_())



# dialog = MyDialog(window)
# dialog.accepted.connect(on_accepted)
# dialog.rejected.connect(on_rejected)
# dialog.finished[int].connect(on_finished)
# result = dialog.exec_()
# if result == QtWidgets.QDialog.Accepted:
#     print(dialog.lineEdit.text())
# else:
#     print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>", 
#             result)