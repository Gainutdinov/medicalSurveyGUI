from PyQt5 import QtCore, QtWidgets, QtGui

class ApntDurationLabel(QtWidgets.QLabel):
    def __init__(self, text='Длительность:', parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        # self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAlignment(QtCore.Qt.AlignCenter)
        # self.setMaximumWidth(250)

class DoctorNameLabel(QtWidgets.QLabel):
    def __init__(self, text='Доктор:', parent=None):
        QtWidgets.QLabel.__init__(self, text, parent)
        self.setAlignment(QtCore.Qt.AlignCenter)

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

class ApntGraphicView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super(ApntGraphicView, self).__init__(parent)
        self.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        scene = QtWidgets.QGraphicsScene()
        scene.setSceneRect(0.0, 0.0, 200.0, 400.0)
        scene.setBackgroundBrush(QtCore.Qt.white)

        line1 = scene.addLine(40.0, 0.0, 40.0, 860.0, pen=QtGui.QPen(QtCore.Qt.black, 1))
        for line in range(16):
            step = line*60
            scene.addLine(20.0, 0.0+step, 60.0, 0.0+step, pen=QtGui.QPen(QtCore.Qt.black, 2))
            scene.addLine(20.0, 0.0+step+30, 40.0, 0.0+step+30)
            hour_text = str(8 + line)+':00'
            txt = scene.addText(hour_text, QtGui.QFont("Verdana", 8))
            txt.setPos(QtCore.QPointF(0.0, 0.0+step))

        #line3 = scene.addLine(20.0, 0.0, 20.0, 60.0, pen=QtGui.QPen(QtCore.Qt.red, 3))
        #line3.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        #line3.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

        # line2 = scene.addLine(QtCore.QLineF(50.0, 100.0, 600.0, 100.0), pen=QtGui.QPen(QtCore.Qt.blue, 3))
        # line2.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        #line2.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

        rect = scene.addRect(QtCore.QRectF(0.0, 0.0, 400.0, 60.0), pen=QtGui.QPen(QtCore.Qt.blue, 3),
                            brush=QtGui.QBrush(QtCore.Qt.green))
        rect.setPos(QtCore.QPointF(50.0, 150.0))
        rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        rect.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

        line1.setSelected(True)

        #view = QtWidgets.QGraphicsView(scene)
        # scene = QtWidgets.QGraphicsScene(self)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.setMinimumSize(500, 400)
        self.setMinimumHeight(660)
        # self.setFixedSize(200, 400)
        self.setScene(scene)
        # item = OpenCVItem(cv2.imread("roi.jpg"))
        # scene.addItem(item)

class ApntVerticalSpacer(QtWidgets.QSpacerItem):
    def __init__(self, parent=None):
        QtWidgets.QSpacerItem.__init__(self, parent)
        QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding) 