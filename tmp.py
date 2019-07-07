# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui

class DateEdit(QtWidgets.QDateEdit):
    def __init__(self, text, parent=None):
        QtWidgets.QDateEdit.__init__(self, text, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAlignment(QtCore.Qt.AlignCenter)

    def focusInEvent(self, e):
        self.grabKeyboard()
        QtWidgets.QDateEdit.focusInEvent(self, e)

    def focusOutEvent(self, e):
        self.releaseKeyboard()
        QtWidgets.QDateEdit.focusOutEvent(self, e)
    

    # def keyPressEvent(self, e):
    #     msg, modifiers = [], []
    #     if e.modifiers() & QtCore.Qt.ShiftModifier:
    #         modifiers.append("Shift")
    #     if e.modifiers() & QtCore.Qt.ControlModifier:
    #         modifiers.append("Ctrl")
    #     if e.modifiers() & QtCore.Qt.AltModifier:
    #         modifiers.append("Alt")
    #     if len(modifiers) == 0:
    #         modifiers.append("No")
    #     if e.matches(QtGui.QKeySequence.Copy):
    #         msg.append("Нажата комбинация <Ctrl>+<C>")
    #     if e.key() == QtCore.Qt.Key_B:
    #         msg.append("Нажата клавиша <B>")
    #     self.setText(
    #          "Код: {0}, символ: {1}\nmodifiers: {2}\n{3}".format(
    #          e.key(), e.text(), "+".join(modifiers), "\n".join(msg)))
    #     e.ignore()
    #     QtWidgets.QLabel.keyPressEvent(self, e)

    def keyReleaseEvent(self, e):
        if e.key() == 16777219:
            print('Backspace')
            print("Клавиша отпущена")
            print(self.sectionText(self.currentSection()))
            print('--------')
            print(self.cursor().pos())
            if not self.sectionText(self.currentSection()) and self.currentSection() != 0:
                self.setCurrentSectionIndex(self.currentSectionIndex() - 1)
                self.setSelectedSection(self.currentSection())
 
class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # self.resize(300, 150)
        # self.label = MyLabel("Нажмите любую клавишу")
        # self.label.setFrameStyle(QtWidgets.QFrame.Box |
        #                          QtWidgets.QFrame.Plain)
        # self.vbox = QtWidgets.QVBoxLayout()
        # self.vbox.addWidget(self.label)
        self.dat= DateEdit(QtCore.QDate(1993, 12, 25))
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.dat)
        self.setLayout(self.vbox)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())