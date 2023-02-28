
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

app = QtWidgets.QApplication([])

theform = uic.loadUi("disabletext.ui")

def disabletextboxfunc():
    theform.lineEdittext.setEnabled(True)
    
def enabletextboxfunc():
    theform.lineEdittext.setEnabled(False)
    
theform.pbenable.clicked.connect(enabletextboxfunc)
theform.pbdisable.clicked.connect(disabletextboxfunc)

if __name__ == '__main__':
    theform.show()
    app.exec()