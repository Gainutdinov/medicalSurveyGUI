# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys, datetime

def section_to_str(section):
    if section == QtWidgets.QDateTimeEdit.DaySection:
        return "День"
    elif section == QtWidgets.QDateTimeEdit.MonthSection:
        return "Месяц"
    elif section == QtWidgets.QDateTimeEdit.YearSection:
        return "Год"
    elif section == QtWidgets.QDateTimeEdit.HourSection:
        return "Часы"
    elif section == QtWidgets.QDateTimeEdit.MinuteSection:
        return "Минуты"
    elif section == QtWidgets.QDateTimeEdit.SecondSection:
        return "Секунды"
    return ""

def on_clicked():
    print("Всего секций -", dateTimeEdit.sectionCount())
    print("currentSectionIndex() -", dateTimeEdit.currentSectionIndex())
    print("currentSection() -", section_to_str(dateTimeEdit.currentSection()))
    print("sectionAt(1) -", section_to_str(dateTimeEdit.sectionAt(1)))
    print("День -", dateTimeEdit.sectionText(QtWidgets.QDateTimeEdit.DaySection))
    print(dateTimeEdit.sectionText(dateTimeEdit.currentSection()))
    print('-------------------')
    print(dateTimeEdit.text())

def on_date_changed():
    print(dateTimeEdit.text())

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Класс QDateTimeEdit")
window.resize(300, 70)
dateTimeEdit = QtWidgets.QDateTimeEdit(datetime.datetime.today())
dateTimeEdit.dateChanged["QDate"].connect(on_date_changed)
button = QtWidgets.QPushButton("Вывести значения")
button.clicked.connect(on_clicked)
box = QtWidgets.QVBoxLayout()
box.addWidget(dateTimeEdit)
box.addWidget(button)
window.setLayout(box)
window.show()
dateTimeEdit.setSelectedSection(QtWidgets.QDateTimeEdit.YearSection)
sys.exit(app.exec_())
