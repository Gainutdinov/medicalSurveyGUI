from PyQt5 import QtCore, QtWidgets

class DateEdit(QtWidgets.QDateEdit):
    def __init__(self, parent=None):
        QtWidgets.QDateEdit.__init__(self, parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setAlignment(QtCore.Qt.AlignLeft)
        # self.setMaximumDateTime(QtCore.QTime(23, 59, 59))

        self.setCalendarPopup(True)
        self.setDate(QtCore.QDate(1993, 12, 25))
        self.setDisplayFormat("dd.MM.yyyy")
        self.setObjectName("dateEdit")

    # def focusInEvent(self, e):
    #     self.grabKeyboard()
    #     QtWidgets.QDateEdit.focusInEvent(self, e)

    def focusOutEvent(self, e):
        self.releaseKeyboard()
        QtWidgets.QDateEdit.focusOutEvent(self, e)

    def keyReleaseEvent(self, e):
        if e.key() == 16777219: # Backspace button clicked
            if not self.sectionText(self.currentSection()) and self.currentSection() != 0:
                self.setCurrentSectionIndex(self.currentSectionIndex() - 1)
                self.setSelectedSection(self.currentSection())
        