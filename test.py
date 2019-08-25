# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui
import sys

class MyRect(QtWidgets.QGraphicsRectItem):
    def __init__(self, r):
        QtWidgets.QGraphicsRectItem.__init__(self)
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3))
        self.setBrush(QtGui.QBrush(QtCore.Qt.darkGreen))
        self.setRect(r)

    def itemChange(self, signal, value):
        if signal == QtWidgets.QGraphicsItem.ItemEnabledChange:
            print("ItemEnabledChange", value)
        elif signal == QtWidgets.QGraphicsItem.ItemEnabledHasChanged:
            print("ItemEnabledHasChanged", value)
        elif signal == QtWidgets.QGraphicsItem.ItemSelectedChange:
            print("ItemSelectedChange", value)
        elif signal == QtWidgets.QGraphicsItem.ItemSelectedHasChanged:
            print("ItemSelectedHasChanged", value)
        elif signal == QtWidgets.QGraphicsItem.ItemPositionChange:
            print("ItemPositionChange", value)
        elif signal == QtWidgets.QGraphicsItem.ItemPositionHasChanged:
            print("ItemPositionHasChanged", value)
        elif signal == QtWidgets.QGraphicsItem.ItemScenePositionHasChanged:
            print("ItemScenePositionHasChanged", value)
        else:  
            print("itemChange", signal)
        return QtWidgets.QGraphicsRectItem.itemChange(self, signal, value)

def on_clicked():
    view.setFocus()
    rect.setEnabled(not rect.isEnabled())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Обработка изменения состояния")
window.resize(600, 400)

scene = QtWidgets.QGraphicsScene(0.0, 0.0, 500.0, 335.0)
scene.setBackgroundBrush(QtCore.Qt.white)

rect = MyRect(QtCore.QRectF(0.0, 0.0, 400.0, 200.0))
rect.setPos(QtCore.QPointF(50.0, 50.0))
rect.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
rect.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)
rect.setFlag(QtWidgets.QGraphicsItem.ItemSendsGeometryChanges)
rect.setFlag(QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)
scene.addItem(rect)

view = QtWidgets.QGraphicsView(scene)

button = QtWidgets.QPushButton("Переключить статус доступности")
button.clicked.connect(on_clicked)

box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)

window.show()
sys.exit(app.exec_())
