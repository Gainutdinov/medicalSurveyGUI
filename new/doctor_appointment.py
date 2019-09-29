from PyQt5 import QtCore, QtWidgets, QtGui
import sqlite3

class ApntDurationLabel(QtWidgets.QLabel):
    def __init__(self, text='Длительность:', parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        # self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAlignment(QtCore.Qt.AlignLeft)
        # self.setMaximumWidth(250)

class DoctorNameLabel(QtWidgets.QLabel):
    def __init__(self, text='Доктор:', parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignLeft)

class ApntDuratonSpinbox(QtWidgets.QSpinBox):
    def __init__(self, parent=None):
        QtWidgets.QSpinBox.__init__(self, parent)
        self.setRange(15, 90)
        self.setSingleStep(5)
        # self.setMaximumWidth(250)
        self.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.setAlignment(QtCore.Qt.AlignCenter)

class DoctorComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        QtWidgets.QComboBox.__init__(self, parent)
        policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.setMinimumSize(160,28)
        # self.setMaximumWidth(250)
        # label.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
        sqlite_file = 'timetable.db'
        conn = sqlite3.connect(sqlite_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 'DOCTORS' ORDER BY ID")
        allRows = cursor.fetchall()
        for row in allRows:
            self.addItem(row[1])

        conn.commit() # not needed when only selecting data
        conn.close()

        self.setSizePolicy(policy)

class ApntCalendar(QtWidgets.QDateEdit):
    def __init__(self, parent=None):
        QtWidgets.QDateEdit.__init__(self, parent)
        self.setDateTime(QtCore.QDateTime.currentDateTime())
        # self.setMaximumWidth(500)
        self.setCalendarPopup(True)

class ApntCheckButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        QtWidgets.QPushButton.__init__(self, parent)
        # self.setMaximumWidth(500)
        self.setText('Посмотреть расписание')
        self.setObjectName('pushButton_0')

class ConsChgDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, selectedDoctor=None, \
            doctors=[], clientFullName='Иванов Иван Иванович', duration=15, consulationType='Common medical examination', startTime='08:00', bookingId=None, startTimeEpoch=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setWindowTitle("Изменить запись")
        self.resize(200, 70)
        
        self.mainBox = QtWidgets.QVBoxLayout()
        
        self.labelDoctor = QtWidgets.QLabel('Имя доктора')
        self.cmbDoctor = QtWidgets.QComboBox()
        for doctor in doctors:
            self.cmbDoctor.addItem(doctor)# setText('Имя доктора')
        self.cmbDoctor.setCurrentText(selectedDoctor)
        self.labelClient = QtWidgets.QLabel('Имя клиента')
        self.lineEditClient = QtWidgets.QLineEdit(clientFullName)
        self.lineEditClient.setPlaceholderText('Иванов Иван Иванович')
        # self.lineEditClient('Иванов Иван Иванович')
        self.labelStartTime = QtWidgets.QLabel('Время начала')
        self.timeEditStartTime = QtWidgets.QTimeEdit() # QDateTimeEdit.date()
        self.timeEditStartTime.setTime(QtCore.QTime.fromString(startTime, "HH:mm"))
        self.labelDuration = QtWidgets.QLabel('Длительность')
        self.spinDuration = QtWidgets.QSpinBox()
        self.spinDuration.setValue(duration)
        self.spinDuration.setRange(15, 120)
        self.spinDuration.setSingleStep(5)
        self.spinDuration.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.labelconsType = QtWidgets.QLabel('Тип консультации')
        self.lineEditConsType = QtWidgets.QLineEdit(consulationType)
        self.startTimeEpoch = startTimeEpoch
        self.bookingId = bookingId


        self.mainBox.addWidget(self.labelDoctor)
        self.mainBox.addWidget(self.cmbDoctor)
        self.mainBox.addWidget(self.labelClient)
        self.mainBox.addWidget(self.lineEditClient)
        self.mainBox.addWidget(self.labelStartTime)
        self.mainBox.addWidget(self.timeEditStartTime)
        self.mainBox.addWidget(self.labelDuration)
        self.mainBox.addWidget(self.spinDuration)

        self.mainBox.addWidget(self.labelconsType)
        self.mainBox.addWidget(self.lineEditConsType)
        
        self.hbox = QtWidgets.QHBoxLayout()
        self.btnOK = QtWidgets.QPushButton("&OK")
        self.btnCancel = QtWidgets.QPushButton("&Cancel")
        self.btnCancel.setDefault(True)
        self.btnOK.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        self.hbox.addWidget(self.btnOK)
        self.hbox.addWidget(self.btnCancel)
        self.mainBox.addLayout(self.hbox)
        
        self.setLayout(self.mainBox)


# class ApntRect(QtWidgets.QGraphicsRectItem):
#     def __init__(self, shape):
#         QtWidgets.QGraphicsRectItem.__init__(self)
#         self.setPen(QtGui.QPen(QtCore.Qt.black, 1))
#         self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
#         self.setRect(shape)

#         self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
#         self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, True)

#         print(self.pos())
#         # set move restriction rect for the item
#         self.move_restrict_rect = QtCore.QRectF(80.0, 80.0, 300.0, 300.0)


#     def mouseMoveEvent(self, event):
#         # check of mouse moved within the restricted area for the item 
#         if self.move_restrict_rect.contains(event.scenePos()):
#             QtWidgets.QGraphicsRectItem.mouseMoveEvent(self, event)
#             print('scenePos - ',self.scenePos())
#             print('pos - ',self.pos())
            


class ApntVerticalSpacer(QtWidgets.QSpacerItem):
    def __init__(self, parent=None):
        QtWidgets.QSpacerItem.__init__(self, parent)
        QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding) 