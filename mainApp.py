#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtMultimedia
from dialogWindow import Ui_Dialog
import os
import shutil
import sys


class MyWin(QtWidgets.QDialogButtonBox, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        #super().__init__()
        #QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #print(glob.glob("./'Протоколы УЗИ'/*"))
        #print(os.listdir("Протоколы УЗИ"))
        def selectDirectory():
            dialog = QtWidgets.QFileDialog()
            folder_path = dialog.getExistingDirectory(None, "Select Folder")
            self.ui.lineEdit_4.setText(folder_path)
            return folder_path

        self.ui.pushButton.clicked.connect(selectDirectory)
        #self.fileDialog = QtGui.QFileDialog(self)
        #self.fileDialog.show()

        for _ in os.listdir("Протоколы УЗИ"):
            if os.path.isfile('./'+'Протоколы УЗИ'+'/'+_):
                self.ui.comboBox.addItem(str(_))
                #print(_)

    def copy_rename(self, old_file_name, new_file_name, new_folder_name, dest_dir):
        try:
            src_dir= os.path.join(os.curdir,'Протоколы УЗИ')
            dst_dir= dest_dir #os.path.join(os.curdir , new_folder_name)
            print('dst_dir',dst_dir)
            src_file = os.path.join(src_dir, old_file_name)
            print('src_file',src_file)
            shutil.copy(src_file,dst_dir)
            
            dst_file = os.path.join(dst_dir, old_file_name)
            new_dst_file_name = os.path.join(dst_dir, new_file_name)
            os.rename(dst_file, new_dst_file_name)
            command='libreoffice "{}"'.format(new_dst_file_name)
            print('+++',command)
            os.system(command)
        except OSError:
            print('OSError')


    
    def accept(self):
        now = QtCore.QDate.currentDate().toString('dd_MM_yyyy') #datetime.date(2012, 12, 14).strftime('%d_%m_%Y')

        name=self.ui.lineEdit.text()
        surname=self.ui.lineEdit_2.text()
        middleName=self.ui.lineEdit_3.text()

        fileName=str(self.ui.comboBox.currentText())
        if (self.ui.lineEdit_4.text() == ''):
            path = os.path.join(os.curdir,(name+'_'+surname+'_'+middleName+'_'+now))
        else:
            path = os.path.join(self.ui.lineEdit_4.text(),(name+'_'+surname+'_'+middleName+'_'+now))
        print('=====',path)
        newFolderName=name+'_'+surname+'_'+middleName+'_'+now
        #path = os.path.join(os.curdir , newFolderName)
        newFileName=str(fileName.split('.')[0]+'_'+str(now)+'.'+fileName.split('.')[1])
        print(newFileName)
        


        #print(self.copy_rename)
        #print(path)
        try:  
            os.mkdir(path)
            print('----------------',newFolderName)
            self.copy_rename(fileName, newFileName, newFolderName,path)
            self.close()
        except OSError:  
            print ("Creation of the directory %s failed" % path)
        else:  
            print ("Successfully created the directory %s " % path)
        #print('sss')

    
    def reject(self):
        print('reject')
        self.close()
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #ico = QtWidgets.QWidget().style().standardIcon(QtWidgets.QStyle.SP_MediaVolume)
    #app.setWindowIcon(ico)
    w = MyWin()
    w.show()
sys.exit(app.exec())