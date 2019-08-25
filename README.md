# medicalSurveyGUI
cd ./new

pyuic5 shell_ui.ui -o shell_ui.py

pyinstaller --onefile ./mainApp.py --noconsole --icon ./med.ico --add-data="checkmark.png;." --add-data="leftArrow.png;." --add-data="rightArrow.png;."





<!-- import os, sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


 icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("checkmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
  -->