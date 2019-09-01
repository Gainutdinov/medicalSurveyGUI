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