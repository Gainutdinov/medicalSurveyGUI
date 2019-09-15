# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets, QtGui
import sys

def on_clicked():
    sel = view.selectionModel()
    # print(sel.selectedIndexes().row()) # row of the selected item
    indexes = []
    viewData = []
    for index in sel.selectedIndexes()[:]:
        indexes.append(index.row())
    rows = set(indexes)
    # print('--->',indexes)
    for row in rows: # row of the selected item
        print(row)
        # print(model.index(row, 0))
        for column in range(model.columnCount()):
            viewData.append(model.data(model.index(row, column)))
        # print(row)
    
    print(viewData)
    # for i in sel.selectedRows(1):
    #     print(i.data())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QItemSelectionModel")
window.resize(400, 300)
view = QtWidgets.QTableView()

model = QtGui.QStandardItemModel(4, 2)
for row in range(0, 4):
    for column in range(0, 2):
        item = QtGui.QStandardItem("({0}, {1})".format(row, column))
        model.setItem(row, column, item)
model.setHorizontalHeaderLabels(["A", "B"])
model.setVerticalHeaderLabels(["01", "02", "03", "04"])
view.setModel(model)

selModel = QtCore.QItemSelectionModel(model)
view.setSelectionModel(selModel)

button = QtWidgets.QPushButton("Вывести выделеные элементы")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(view)
box.addWidget(button)
window.setLayout(box)
window.show()
sys.exit(app.exec_())