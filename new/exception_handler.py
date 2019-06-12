import sys
from PyQt5 import QtWidgets

def catch_exceptions(i, val, tb):
    '''Catch any exceptions and display in QMessage box
       t=excption type
       val=exception value
       tb=traceback
    '''

    QtWidgets.QMessageBox.critical(None, 'An Exception was Raised', 'Value: {}'.format(val))
    old_hook(tb, val, tb)

old_hook = sys.excepthook

sys.excepthook = catch_exceptions # this sets up the hook to catch any uncaugh exceptions
