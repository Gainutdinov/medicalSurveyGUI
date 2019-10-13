#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtSql
from docx import Document, shared
from shell_ui import Ui_MainWindow
from CustomDateEdit import DateEdit as customDateEdit
from dialog import MyDialog
from exception_handler import catch_exceptions
from doctor_appointment import ApntDurationLabel, DoctorNameLabel, ApntDuratonSpinbox, DoctorComboBox, ApntCalendar, ApntCheckButton, ApntVerticalSpacer, ConsChgDialog
import db_create
import os
import shutil
import json
import sys
import csv



class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        #super().__init__()
        #QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.gridLayout.removeWidget(self.ui.dateEdit)
        self.ui.dateEdit.close()
        self.ui.dateEdit = customDateEdit(self.ui.centralwidget)
        self.ui.gridLayout.addWidget(self.ui.dateEdit, 3, 1, 1, 2)
        self.ui.gridLayout.update()
        

        #self.ui.gridLayout.addWidget(customDateEdit, 3, 1, 1, 2)

        self.ui.lineEdit_4.setText(os.getcwd())

        # self.DOCTORS=[] 
        # self.VESSELS=[] 
        # self.PROTOCOL_ULTRASOUND=[]
        # self.typeOfProtocols={
        #     'Приём Врача':'Доктора',
        #     'УЗИ Общее':'Протоколы УЗИ',
        #     'УЗИ Сосудов':'Сосуды',
        # }





        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.copyAndOpenTheTemplate)
        self.ui.lineEdit.textChanged.connect(self.enableButton)
        self.ui.lineEdit_2.textChanged.connect(self.enableButton)
        self.ui.lineEdit_3.textChanged.connect(self.enableButton)
        #self.ui.menu.addAction("Выход", self.close)
        #self.ui.menu.addAction("Выбор папок", self.menuChoice)
        self.ui.action.triggered.connect(self.menuChoice)
        self.ui.action_2.triggered.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.fillBirthDate)
        self.ui.pushButton_4.clicked.connect(self.add_appointment_widgets)#lambda : self.ui.pushButton_4.setEnabled(False))
        # self.ui.buttonGroup.buttonToggled.connect(self.enableButton)
        # self.ui.buttonGroup.buttonClicked.connect(self.fullfillComboBox)
        self.ui.toolButton.clicked.connect(self.selectFolder)
        # self.ui.pushButton_4.clicked.connect(self.rmvFromSrv)
        # self.ui.pushButton_5.clicked.connect(self.addToSrv)
        # self.ui.listWidget.doubleClicked.connect(self.addToSrv)
        self.ui.listWidget_3.clicked.connect(self.addToMedTypes)
        self.ui.listWidget_4.doubleClicked.connect(self.addToSrv_2)
        self.ui.action_4.triggered.connect(self.reportCurrentMonth)
        


        self.readSettingsFile()


                    #self.ui.comboBox.addItem(str(_))
                    #print(_)

    def copy_rename(self, old_file_name, new_file_name, src_dir_file, dst_dir):
        try:
            #src_dir=os.path.join(os.curdir,'Протоколы УЗИ')
            #dst_dir= dest_dir #os.path.join(os.curdir , new_folder_name)
            if (os.path.isdir(dst_dir)):
                print('folder already exist')
            else:
                os.mkdir(dst_dir)
            #print('dst_dir',dst_dir)
            #print('src_dir_file',src_dir_file)
            shutil.copy(src_dir_file,dst_dir)
            #print('src_file',src_dir_file)
            #print('---->>>',os.listdir(dst_dir))
            
            dst_file = os.path.join(dst_dir, old_file_name)
            new_dst_file_name = os.path.join(dst_dir, new_file_name)
            os.rename(dst_file, new_dst_file_name)

            # add with name and surname
            document = Document(new_dst_file_name)

            paragraphs = document.paragraphs
            paragraphs[1].style.font.size = shared.Pt(12)
            text = paragraphs[1].text
            # patient = dst_dir.split('_')[0]+' '+dst_dir.split('_')[1]+' '+dst_dir.split('_')[2]+'\n'\
            #     +dst_dir.split('_')[3]+'.'+dst_dir.split('_')[4]+'.'+dst_dir.split('_')[5]+'\n'
            patient = 'Ф.И.О.: '  + self.ui.lineEdit.text() + ' ' + self.ui.lineEdit_2.text() + ' ' + self.ui.lineEdit_3.text()+'\n'\
                + 'Дата рождения: ' + self.ui.dateEdit.date().toString('dd.MM.yyyy') + ' ' \
                + 'Дата исследования: ' + QtCore.QDate.currentDate().toString('dd.MM.yyyy') + '\n'
            paragraphs[1]._p.clear()
            paragraphs[1].add_run(patient + text)
            document.save(new_dst_file_name)
        except OSError:
            print('OSError')
    
    def enableButton(self):
        # if self.ui.lineEdit.text().isEmpty(): # print('Empty') 
        if (self.ui.lineEdit.text() != "" and self.ui.lineEdit_2.text() != "" and self.ui.lineEdit_3.text() != "" \
            and self.ui.listWidget_5.count() != 0):
            # and self.ui.buttonGroup.checkedButton() is not None):
            self.ui.pushButton_2.setEnabled(True)
        else:
            self.ui.pushButton_2.setEnabled(False)
        #print(self.ui.buttonGroup.checkedButton())
    
    def menuChoice(self):
        dialog = MyDialog(self)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            print("Нажата кнопка Save")
            # self.ui.lineEdit_4.setText(dialog.dialog_ui.lineEdit_4.text())
            self.readSettingsFile()
        else:
            print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>", result)
        #print('ssssss')

    # def closeProgram(self):
    #     self.close()
    
    def fullfillComboBox(self):
        # print(self.ui.buttonGroup.checkedButton().text())
        selectButton=self.ui.buttonGroup.checkedButton().text()
        if selectButton=='Приём Врача':
            # self.ui.comboBox.addItems(self.DOCTORS)
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.DOCTORS)
            print('DOCTORS')
        elif selectButton=='УЗИ Общее':
            # self.ui.comboBox.addItems(self.PROTOCOL_ULTRASOUND)
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.PROTOCOL_ULTRASOUND)
            print('PROTOCOL_ULTRASOUND')
        elif selectButton=='УЗИ Сосудов':
            # self.ui.comboBox.addItems(self.VESSELS)
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.VESSELS)
            print('VESSELS')

    def selectFolder(self):
        directory=QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if (directory):
            self.ui.lineEdit_4.setText(directory)
            with open("settings.json", "r") as jsonFile:
                data = json.load(jsonFile)
            data["Пациенты"] = directory
            with open("settings.json", "w") as jsonFile:
                json.dump(data, jsonFile)
            #print('No')
        #print(directory)
    
    def readSettingsFile(self):
        # self.DOCTORS.clear()
        # self.PROTOCOL_ULTRASOUND.clear()
        # self.VESSELS.clear()
        with open('settings.json', 'r') as jsonfile:
            self.jsonData = json.load(jsonfile)

            self.ui.lineEdit_4.setText(self.jsonData['Пациенты'])

            try:
                completer = QtWidgets.QCompleter( [client.split('_')[0] for client in os.listdir(self.jsonData['Пациенты'])], self.ui.lineEdit)
                self.ui.lineEdit.setCompleter(completer)
                completer = QtWidgets.QCompleter( [client.split('_')[1] for client in os.listdir(self.jsonData['Пациенты'])], self.ui.lineEdit_2)
                self.ui.lineEdit_2.setCompleter(completer)
                completer = QtWidgets.QCompleter( [client.split('_')[2] for client in os.listdir(self.jsonData['Пациенты'])], self.ui.lineEdit_3)
                self.ui.lineEdit_3.setCompleter(completer)
            except:
                print('Пациентов не было найдено')

            # for _ in os.listdir(self.jsonData['Доктора']):
            #     self.DOCTORS.append(_.split('.')[0])
            # for _ in os.listdir(self.jsonData['Протоколы УЗИ']):
            #     self.PROTOCOL_ULTRASOUND.append(_.split('.')[0])
            # for _ in os.listdir(self.jsonData['Сосуды']):
            #     self.VESSELS.append(_.split('.')[0])
            self.ui.lineEdit.setText(self.jsonData['Фамилия'])
            self.ui.lineEdit_2.setText(self.jsonData['Имя'])
            self.ui.lineEdit_3.setText(self.jsonData['Отчество'])
            # birthDateStr = jsonData['ДатаРождения'] #"20/12/2015";
            # QDate Date = QDate::fromString(date_string_on_db,"dd/MM/yyyy");
            self.ui.dateEdit.setDate(QtCore.QDate.fromString(self.jsonData['ДатаРождения'],"dd.MM.yyyy")) # (1993, 12, 25)  # .setText(jsonData['Отчетсво'])
            # for x in os.walk(self.jsonData['Обследования']):
            for folder in filter(os.path.isdir, os.listdir(self.jsonData['Обследования'])):
                self.ui.listWidget_3.addItem(QtWidgets.QListWidgetItem(folder))#self.ui.listWidget.currentItem().text())
                #self.ui.listWidget_3
    
    def fillBirthDate(self):
        try:
            for client in os.listdir(self.jsonData['Пациенты']):
                if client.split('_')[0] == self.ui.lineEdit.text() and \
                   client.split('_')[1] == self.ui.lineEdit_2.text() and \
                   client.split('_')[2] == self.ui.lineEdit_3.text():
                    # print(str(client.split('_')[3:]))
                    self.ui.dateEdit.setDate(QtCore.QDate.fromString('_'.join(client.split('_')[3:]), "dd_MM_yyyy"))
                    self.ui.pushButton_3.setEnabled(False)
        except:
            print('Не найдено года рождения')
        


    def copyAndOpenTheTemplate(self):
        #copy_rename(old_file_name, new_file_name, src_dir, dest_dir):

        now = QtCore.QDate.currentDate().toString('dd_MM_yyyy') # datetime.date(2012, 12, 14).strftime('%d_%m_%Y'))
        birthDate=self.ui.dateEdit.date().toString('dd_MM_yyyy')
        birthDateUnixTime = QtCore.QDateTime.fromString(birthDate,"dd_MM_yyyy").toSecsSinceEpoch()
        name=self.ui.lineEdit_2.text()
        surname=self.ui.lineEdit.text()
        middleName=self.ui.lineEdit_3.text()

        # dirWithProtocols=self.jsonData[self.typeOfProtocols[self.ui.buttonGroup.checkedButton().text()]]
        for item in [self.ui.listWidget_5.item(i) for i in range(  self.ui.listWidget_5.count())]:
            protocolName=item.text()
            # protocolType=self.typeOfProtocols[item.data(QtCore.Qt.UserRole)]
            protocolType = item.data(QtCore.Qt.UserRole)

            # Original dirWithProtocols
            # dirWithProtocols=self.jsonData[self.typeOfProtocols[item.data(QtCore.Qt.UserRole)]]
            # dirWithProtocols = os.path.join( self.jsonData['Обследования'], self.jsonData[self.typeOfProtocols[item.data(QtCore.Qt.UserRole)]])
            dirWithProtocols = os.path.join( self.jsonData['Обследования'], self.jsonData[item.data(QtCore.Qt.UserRole)])
            protocol = [filename for filename in os.listdir(dirWithProtocols) if filename.startswith(item.text())][0]
            protocolExt=protocol.split('.')[1] #self.ui.comboBox.currentText().split('.')[1]

            # protocol=item.text() + '.' + protocolExt
            newDirName=('{0}_{1}_{2}_{3}').format(surname,name,middleName,birthDate)
            newFileName=('{0}_{1}.{2}').format(protocolName,now,protocolExt)
            destDir=os.path.join(self.ui.lineEdit_4.text(),newDirName)
            srcDir=os.path.join(os.getcwd(),protocolType,protocol)# self.ui.comboBox.currentText())
            new_dst_file_name=os.path.join(destDir,newFileName)
            self.copy_rename(protocol, newFileName, srcDir, destDir)
    
            command='start winword "{}"'.format(new_dst_file_name.replace('/', '\\'))
            os.system(command)


        self.jsonData['Фамилия'] = surname 
        self.jsonData['Имя'] = name
        self.jsonData['Отчество'] = middleName
        self.jsonData['ДатаРождения'] =  self.ui.dateEdit.date().toString('dd.MM.yyyy')
        # settings = json.dumps(settings).decode('unicode-escape').encode('utf8')
        with open('settings.json', 'w') as json_file:  
            json.dump(self.jsonData, json_file, ensure_ascii=False)
        print('OKAY!')
        
        conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        conn.setDatabaseName('timetable.db')
        conn.open()
        conn.transaction()
        query = QtSql.QSqlQuery()
        query.prepare("INSERT OR IGNORE INTO CLIENTS (client_full_name, client_birth_date) VALUES (?,?)")
        query.addBindValue(('{0} {1} {2}').format(surname,name,middleName))
        query.addBindValue(birthDateUnixTime)

        query.exec_()
        conn.commit()

        if self.ui.pushButton_4.isChecked():
            print('checked.')

            model = self.ui.gridLayout_4.itemAt(9).widget().model()
            sel = self.ui.gridLayout_4.itemAt(9).widget().selectionModel()

            print(model)

            indexes = []
            selectedEntry = []
            # find number of selected rows
            for index in sel.selectedIndexes()[:]:
                indexes.append(index.row())
            rows = set(indexes)

            for row in rows:
                rowValues = []
                for column in range(model.columnCount()):
                    rowValues.append(model.data(model.index(row, column)))
                selectedEntry.append(rowValues)

            
            val = selectedEntry[0][9] # booknig_id to delete
            query.prepare(" UPDATE SCHEDULE SET actual_consultancy_start_time = ? WHERE booking_id = ? ; ")
            now = QtCore.QDateTime.currentDateTime().toSecsSinceEpoch()
            query.bindValue(0, now)
            query.bindValue(1, val)
            query.exec_()
            ler = query.lastError ()
            if ler.isValid():
                conn.close()
                print(ler.text())
            conn.commit()
        conn.close()
        self.close()
    
    def addToSrv(self):
        if not (self.ui.listWidget.selectedIndexes() == []):
            item=QtWidgets.QListWidgetItem(self.ui.listWidget.currentItem().text())
            item.setData(QtCore.Qt.UserRole, self.ui.buttonGroup.checkedButton().text())
            #   data = currentItem->data(Qt::UserRole)
            selectedValues = [self.ui.listWidget_2.item(i).text() for i in range(self.ui.listWidget_2.count())]
            if item.text() not in selectedValues:
                self.ui.listWidget_2.addItem(item)#self.ui.listWidget.currentItem().text())
            # self.enableButton()

    def addToSrv_2(self):
        if not (self.ui.listWidget_4.selectedIndexes() == []):
            selectedValues = [self.ui.listWidget_5.item(i).text() for i in range(self.ui.listWidget_5.count())]
            item = QtWidgets.QListWidgetItem(self.ui.listWidget_4.currentItem().text())
            item.setData(QtCore.Qt.UserRole, self.ui.listWidget_3.currentItem().text())
            if item.text() not in selectedValues:
                self.ui.listWidget_5.addItem(item) # self.ui.listWidget.currentItem().text())
            self.enableButton()


    def addToMedTypes(self):
        # for _ in self.ui.listWidget_3.selectedItems():
        consType = self.ui.listWidget_3.selectedItems()[0].text()
        consTypeDir = os.path.join(self.jsonData['Обследования'], consType)
        self.ui.listWidget_4.clear()
        for file in os.listdir(consTypeDir):
            if file.endswith(".docx"):
                self.ui.listWidget_4.addItem(file.split('.')[0]) # .addItems(self.DOCTORS)
                # print(files) 


    def rmvFromSrv(self):
        listItems=self.ui.listWidget_2.selectedItems()
        if not listItems: return        
        for item in listItems:
            print(item.text())
            print(item.data(QtCore.Qt.UserRole))
            #self.ui.listWidget_2.takeItem(self.ui.listWidget_2.row(item))
        print('RemovevFromSRV')
    
    def add_appointment_widgets(self):
        self.ui.pushButton_4.setEnabled(False)
        grid_layout = self.ui.gridLayout_4
        # spinbox = QtWidgets.QAbstractSpinBox()
        grid_layout.addWidget(ApntDurationLabel(),0,0,1,1)
        grid_layout.addWidget(ApntDuratonSpinbox(),0,1,1,2)
        grid_layout.addWidget(DoctorNameLabel(),1,0,1,1)
        grid_layout.addWidget(DoctorComboBox(),1,1,1,2)
        grid_layout.addWidget(ApntCalendar(),2,0, 1, 3)
        button = ApntCheckButton()
        grid_layout.addWidget(button,3,0, 1, 3)

        grid_layout.addWidget(QtWidgets.QLabel('Booking time: '),4,0, 1, 1)
        timeedit = QtWidgets.QTimeEdit()
        timeedit.setDisplayFormat('HH:mm')
        time = QtCore.QTime().currentTime()
        timeedit.setTime(time)
        grid_layout.addWidget(timeedit,4,1, 1, 1)
        btnSch = QtWidgets.QPushButton()
        btnSch.setText('Book')
        grid_layout.addWidget(btnSch,4,2, 1, 1)
        # grid_layout.addWidget(QtWidgets.QPushButton(),5,2, 1, 1)

        grid_layout.addWidget(QtWidgets.QTableView(),5,0, 1, 3)
        btnDeact = QtWidgets.QPushButton()
        btnDeact.setText('Deactivate')
        grid_layout.addWidget(btnDeact,6,0, 1, 3)
        btnChg = QtWidgets.QPushButton()
        btnChg.setText('Change')
        grid_layout.addWidget(btnChg,7,0, 1, 3)
        chooseEntry = QtWidgets.QPushButton()
        chooseEntry.setText('Выбрать запись')
        grid_layout.addWidget(chooseEntry,8,0, 1, 3)
        # print(self.ui.gridLayout_4.itemAt(3).widget())


        self.ui.gridLayout_4.itemAt(5).widget().clicked.connect(self.sqlTbleviewModel)
        self.ui.gridLayout_4.itemAt(8).widget().clicked.connect(self.bookConsult)
        self.ui.gridLayout_4.itemAt(10).widget().clicked.connect(self.deactConsult)
        self.ui.gridLayout_4.itemAt(11).widget().clicked.connect(self.changeConsult)
        self.ui.gridLayout_4.itemAt(12).widget().clicked.connect(self.chooseEntry)

        # self.ui.gridLayout_4.pushButton_0.clicked.connect(self.sqlTbleviewModel)
        #print(self.ui.gridLayout_4.children())
        # tableview = grid_layout.tableView
        # self.model = QtSql.QSqlTableModel()
        # tableview.setModel(self.model)
        
        # self.model.setTable('PERSON')
        # self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
        # self.model.select()
        # self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        # self.model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        # self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")

       #spacerItem = QtWidgets.QSpacerItem(110, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        #grid_layout.addItem(spacerItem, 5,0)

        # vbox.addWidget(self.txtOutput)
        # layout.addLayout(grid_layout)

    def sqlTbleviewModel(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('timetable.db')

        if not db.open():
            print("Cannot establish a database connection ")
            sys.exit(1)
        tableview = self.ui.gridLayout_4.itemAt(9).widget() #.QTableView
        self.model = QtSql.QSqlQueryModel()
        # self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Name")
        # self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Price")
        tableview.setModel(self.model)

        q = QtSql.QSqlQuery()
        # q.prepare("SELECT * FROM CLIENTS")
        q.prepare(
           " SELECT CLIENTS.client_full_name AS client_name, "
           " DOCTORS.doctor_full_name AS doctor_name, "
           " strftime('%H:%M', DATETIME(consultancy_start_time, 'unixepoch','localtime')) AS 'start', "
           " strftime('%H:%M', DATETIME(consultancy_end_time, 'unixepoch','localtime')) AS 'finish', "
           " strftime('%m/%Y', DATETIME(consultancy_start_time, 'unixepoch','localtime')) AS 'date', "
           " consultancy_start_time AS unix_epoch_time_start, "
           " consultancy_end_time AS unix_epoch_time_finish, "
           " type_of_consultation AS consultancy_type, "
           " consultancy_duration  AS duration, "
           " booking_id "
           " FROM SCHEDULE "
           " INNER JOIN CLIENTS ON SCHEDULE.client_id=CLIENTS.id INNER JOIN DOCTORS ON SCHEDULE.doctor_id=DOCTORS.id "
           " WHERE SCHEDULE.consultancy_start_time >= ? AND SCHEDULE.consultancy_start_time <= ? "
           " ORDER BY SCHEDULE.consultancy_start_time;"
           " "
           )
        # q.addBindValue('1567242000')
        # q.addBindValue('1567328300')
        schCld = self.ui.gridLayout_4.itemAt(4).widget().date().toString('dd_MM_yyyy')
        print('UnixTime',QtCore.QDateTime.fromString(schCld,"dd_MM_yyyy").toSecsSinceEpoch())
        schCldUnix = QtCore.QDateTime.fromString(schCld,"dd_MM_yyyy").toSecsSinceEpoch()
        print(schCld)
        q.bindValue(0, schCldUnix)
        q.bindValue(1, str(int(schCldUnix)+86400))
        # UnixTime = QtCore.QDateTime.fromString(birthDate,"dd_MM_yyyy").toSecsSinceEpoch(
        # self.ui.dateEdit.date().toString('dd_MM_yyyy')
        
        q.exec_()
        if q.lastError().isValid():
            print('--Error with SQL query--')
            print(q.lastError().text())
        
        while q.next():
            cid = q.value (0)
            name =  q.value (1)
            price = q.value (2)
            print (cid,name,price)
        print('---------')
        db.close()
        self.model.setQuery(q)
        # print(q.value(0))

        # db.close()



        # self . model . setQuery ( query )
        # self . model . removeColumn (0)
        # self . model . setHeaderData (0 , Qt . Horizontal , " Name " )
        # self . model . setHeaderData (1 , Qt . Horizontal , " Price " )


        # self.model.setTable('PATIENTS')
        # self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)   # All changes to the model will be applied immediately to the database
        # self.model.select()
        # self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        # self.model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        # self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")
    
    def bookConsult(self):

        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('timetable.db')
        if not db.open():
            print("Cannot establish a database connection ")
            sys.exit(1)
        birthDate=self.ui.dateEdit.date().toString('dd_MM_yyyy')
        birthDateUnixTime = QtCore.QDateTime.fromString(birthDate,"dd_MM_yyyy").toSecsSinceEpoch()
        name=self.ui.lineEdit_2.text()
        surname=self.ui.lineEdit.text()
        middleName=self.ui.lineEdit_3.text()
        doctorFullName = self.ui.gridLayout_4.itemAt(3).widget().currentText()
        type_of_consultation = ''
        protocols=[]

        bookDateTime = self.ui.gridLayout_4.itemAt(4).widget().date().toString('dd_MM_yyyy')+'_'+\
            self.ui.gridLayout_4.itemAt(7).widget().time().toString("hh_mm")
        consultancy_duration = self.ui.gridLayout_4.itemAt(1).widget().value()
        consultancy_start_time = QtCore.QDateTime.fromString(bookDateTime,"dd_MM_yyyy_hh_mm").toSecsSinceEpoch()
        consultancy_end_time = consultancy_start_time + consultancy_duration * 60

        if (self.ui.listWidget_5.count() != 0):
            for item in [self.ui.listWidget_5.item(i) for i in range(self.ui.listWidget_5.count())]:
                protocolName=item.text()
                protocols.append(protocolName)
            type_of_consultation = '; '.join(protocols)
        else:
            type_of_consultation = 'Common medical examination'
        print(type_of_consultation)
        print('start',consultancy_start_time)
        print('end',consultancy_end_time)
        q = QtSql.QSqlQuery()
        q.prepare("INSERT OR IGNORE INTO CLIENTS (client_full_name, client_birth_date) VALUES (?,?)")
        q.addBindValue(('{0} {1} {2}').format(surname,name,middleName))
        q.addBindValue(birthDateUnixTime)
        q.exec_()
        if q.lastError().isValid():
            print('--Error with SQL query--')
            print(q.lastError().text())
        
        q.prepare(
            "SELECT * FROM SCHEDULE WHERE consultancy_start_time >= ?  AND consultancy_end_time <= ?"
            )
        q.addBindValue(consultancy_start_time)
        q.addBindValue(consultancy_end_time)
        q.exec_()
        if q.lastError().isValid():
            print('--Error with SQL query--')
            print(q.lastError().text())
        
 
        # print(q.record().count())
        
        if q.first(): # try to find whether the time slot is free for booking
            print('These time slot is already booked')
            QtWidgets.QMessageBox.information(self, "Временной слот уже занят", 
                          "Данный временной промежуток уже занят, пожалуйста, выберите другое время.",
                          buttons=QtWidgets.QMessageBox.Close,
                          defaultButton=QtWidgets.QMessageBox.Close)
            db.close()
        else:
            q.prepare(
                "INSERT INTO SCHEDULE (client_id, doctor_id, consultancy_start_time, consultancy_end_time, type_of_consultation, consultancy_duration)"
                "VALUES((SELECT id FROM CLIENTS WHERE client_full_name = ?),"
                "(SELECT id FROM DOCTORS WHERE doctor_full_name = ?),"
                "?,?,?,?)"
                )
            q.addBindValue(('{0} {1} {2}').format(surname,name,middleName))
            q.addBindValue(doctorFullName)
            q.addBindValue(consultancy_start_time)
            q.addBindValue(consultancy_end_time)
            q.addBindValue(type_of_consultation)
            q.addBindValue(consultancy_duration)
            q.exec_()
            if q.lastError().isValid():
                print('--Error with SQL query--')
                print(q.lastError().text())
            
            print('Value added.')
            db.close()
            self.sqlTbleviewModel()
    
    def deactConsult(self):
        print('deactivate')

        model = self.ui.gridLayout_4.itemAt(9).widget().model()
        sel = self.ui.gridLayout_4.itemAt(9).widget().selectionModel()

        indexes = []
        viewData = []
        # find number of selected rows
        for index in sel.selectedIndexes()[:]:
            indexes.append(index.row())
        rows = set(indexes)

        for row in rows:
            rowValues = []
            for column in range(model.columnCount()):
                rowValues.append(model.data(model.index(row, column)))
            viewData.append(rowValues)


        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("timetable.db")
        if not db.open():
            print("Cannot establish a database connection.")
        q = QtSql.QSqlQuery()

        for selectRow in viewData:
            # print('----------',selectRow[9]) 
            val = selectRow[9] # booknig_id to delete
            q.prepare(" DELETE FROM SCHEDULE WHERE booking_id = ? ; ")
            q.bindValue(0, val)
            q.exec_()
            ler = q.lastError ()
            if ler.isValid():
                db.close()
                print(ler.text())

        db.close()
        self.sqlTbleviewModel()
    
    def changeConsult(self):

        def on_accepted():
            if (dialog.lineEditClient.text() and dialog.lineEditConsType.text() ):
                consultancyStartTime = QtCore.QDateTime.fromSecsSinceEpoch(dialog.startTimeEpoch).toString('dd_MM_yyyy')+ \
                    dialog.timeEditStartTime.time().toString("_HH_mm")
                consultancy_start_time = QtCore.QDateTime.fromString(consultancyStartTime,"dd_MM_yyyy_HH_mm").toSecsSinceEpoch()
                consultancy_end_time = QtCore.QDateTime.fromString(consultancyStartTime,"dd_MM_yyyy_HH_mm").toSecsSinceEpoch() + dialog.spinDuration.value()*60
                type_of_consultation = dialog.lineEditConsType.text()
                consultancy_duration = dialog.spinDuration.value()
                client_full_name = dialog.lineEditClient.text()
                doctor_full_name = dialog.cmbDoctor.currentText()
                booking_id = dialog.bookingId

                # client_full_name = dialog.lineEditClient.text().replace("", "_")
                
                print("on_accepted", dialog.bookingId) 
                dialog.lineEditConsType.text()
                dialog.spinDuration.value()

                db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
                db.setDatabaseName('timetable.db')
                db.open()
                db.transaction()
                query = QtSql.QSqlQuery()
                query.prepare("INSERT OR IGNORE INTO CLIENTS (client_full_name, client_birth_date) VALUES (?, 747273600)")
                query.addBindValue(('{0}').format(dialog.lineEditClient.text()))
                query.exec_()
                db.commit()


                query.prepare(
                "UPDATE SCHEDULE "
                "SET consultancy_start_time = ?, "
                "    consultancy_end_time = ?, "
                "    type_of_consultation = ?, "
                "    consultancy_duration = ?, "
                "    client_id=( "
                "        SELECT id FROM CLIENTS WHERE client_full_name = ? ), "
                "    doctor_id=( "
                "        SELECT id FROM DOCTORS WHERE doctor_full_name = ? ) " 
                "WHERE booking_id = ? "
                )
                print(consultancy_start_time, consultancy_end_time, type_of_consultation, consultancy_duration,client_full_name,doctor_full_name, booking_id)    
                query.bindValue(0, consultancy_start_time)
                query.bindValue(1, consultancy_end_time)
                query.bindValue(2, type_of_consultation)
                query.bindValue(3, consultancy_duration)
                query.bindValue(4, client_full_name)
                query.bindValue(5, doctor_full_name)
                query.bindValue(6, booking_id)
                query.exec_()
                ler = query.lastError ()
                if ler.isValid():
                    db.close()
                    print('ERROR', query.result)
                    print(ler.text())
                db.commit()
                db.close()
                self.sqlTbleviewModel()
                    #------------------------------------------------------------------------------------------------------------------------------------------------------------------

        def on_rejected():
            print("on_rejected")

        def on_finished(status):
            print("on_finished", status)


        print('change consultancy')

        doctors = [self.ui.gridLayout_4.itemAt(3).widget().itemText(i) for i in range(self.ui.gridLayout_4.itemAt(3).widget().count())]
        model = self.ui.gridLayout_4.itemAt(9).widget().model()
        sel = self.ui.gridLayout_4.itemAt(9).widget().selectionModel()

        if sel:
            indexes = []
            viewData = []
            # find number of selected rows
            for index in sel.selectedIndexes()[:]:
                indexes.append(index.row())
            rows = set(indexes)

            for row in rows:
                rowValues = []
                for column in range(model.columnCount()):
                    rowValues.append(model.data(model.index(row, column)))
                viewData.append(rowValues)

            if viewData: # set up patient's full name
                print('changeConsult doctor ', viewData)
                clientFullName = viewData[0][0]
                duration = viewData[0][8]
                consultationType = viewData[0][-4]
                startTime = viewData[0][2]
                selectedDoctor = viewData[0][1]
                bookingId = viewData[0][9]
                startTimeEpoch = viewData[0][5]
        

        dialog = ConsChgDialog(w, selectedDoctor, doctors, clientFullName, duration, consultationType, startTime, bookingId, startTimeEpoch)
        dialog.accepted.connect(on_accepted)
        dialog.rejected.connect(on_rejected)
        dialog.finished[int].connect(on_finished)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            # print(dialog.lineEditClient.text())
            print('OK button was clicked.')
        else:
            print("Нажата кнопка Cancel, кнопка Закрыть или клавиша <Esc>", result)
        
    def chooseEntry(self):

        model = self.ui.gridLayout_4.itemAt(9).widget().model()
        sel = self.ui.gridLayout_4.itemAt(9).widget().selectionModel()

        if sel:
            indexes = []
            viewData = []
            # find number of selected rows
            for index in sel.selectedIndexes()[:]:
                indexes.append(index.row())
            rows = set(indexes)

            for row in rows:
                rowValues = []
                for column in range(model.columnCount()):
                    rowValues.append(model.data(model.index(row, column)))
                viewData.append(rowValues)

            if viewData: # set up patient's full name
                self.ui.lineEdit.setText(viewData[0][0].split(' ')[0])
                self.ui.lineEdit_2.setText(viewData[0][0].split(' ')[1])
                self.ui.lineEdit_3.setText(viewData[0][0].split(' ')[2])


    def reportCurrentMonth(self):
        days = int(QtCore.QDate.currentDate().toString("dd"))
        report = [ ['doctor_name', 'consultancy_start_time', 'client_name', 'type_of_consultation', 'consultancy_duration'] ]
        startDate = QtCore.QDate.currentDate().addDays(1 - days) # .toString("dd.MM.yyyy")
        startDateUnixTime = QtCore.QDateTime.fromString(startDate.toString('dd_MM_yyyy'),"dd_MM_yyyy").toSecsSinceEpoch() # .toString("dd.MM.yyyy")
        finishDateUnixTime = QtCore.QDateTime.fromString(startDate.addMonths(1).toString('dd_MM_yyyy'),"dd_MM_yyyy").toSecsSinceEpoch() # .toString("dd.MM.yyyy")
        print('--->',startDateUnixTime)
        print('--->',finishDateUnixTime)

        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("timetable.db")
        if not db.open():
            print("Cannot establish a database connection.")
        q = QtSql.QSqlQuery()
        q.prepare(" SELECT DOCTORS.doctor_full_name AS doctor_name,"
                  " SCHEDULE.consultancy_start_time,"
                  " CLIENTS.client_full_name AS client_name ,"
                  " SCHEDULE.type_of_consultation,  "
                  " SCHEDULE.consultancy_duration AS consultancy_duration FROM SCHEDULE "
                  " INNER JOIN CLIENTS ON SCHEDULE.client_id=CLIENTS.id INNER JOIN DOCTORS ON SCHEDULE.doctor_id=DOCTORS.id "
                  " WHERE SCHEDULE.consultancy_start_time >= ? AND SCHEDULE.consultancy_start_time <= ? ; ") # EXECUTE
        q.bindValue(0, startDateUnixTime) # 1567278000
        q.bindValue(1, finishDateUnixTime) # 1567872900
        q.exec_()
        ler = q.lastError ()
        if ler.isValid():
            db.close()
            print(ler.text())

        while q.next():
            doctor_name = q.value(0)
            consultancy_start_time = QtCore.QDateTime.fromSecsSinceEpoch(q.value(1)).toString(QtCore.Qt.ISODate)
            client_name = q.value(2)
            type_of_consultation = q.value(3)
            consultancy_duration = q.value(4)
            report.append([doctor_name, consultancy_start_time, client_name, type_of_consultation, consultancy_duration])
            # print( doctor_name, consultancy_start_time, client_name, type_of_consultation, consultancy_duration)

        db.close()
        

        with open("report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(report)




 
if __name__ == "__main__":
    if QtCore.QDate.currentDate().toString("yyyy") != '2020':
        if not ('settings.json' in os.listdir()):
            settings = {  
                'Доктора': os.path.join(os.getcwd(),'Доктора'),
                'Протоколы УЗИ': os.path.join(os.getcwd(),'Протоколы УЗИ'),
                'Сосуды': os.path.join(os.getcwd(),'Сосуды'),
                'Пациенты': os.getcwd(),
                'Обследования': os.getcwd(),
                'Фамилия': "Иванов",
                'Имя': "Иван",
                'Отчество': "Иванович",
                'ДатаРождения': "25.12.1993"
            }
            # settings = json.dumps(settings).decode('unicode-escape').encode('utf8')
            with open('settings.json', 'w') as json_file:  
                json.dump(settings, json_file, ensure_ascii=False)
        app = QtWidgets.QApplication(sys.argv)
        #ico = QtWidgets.QWidget().style().standardIcon(QtWidgets.QStyle.SP_MediaVolume)
        #app.setWindowIcon(ico)
        w = MyWin()
        w.show()
sys.exit(app.exec())