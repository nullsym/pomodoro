#!/usr/bin/env python

# https://wiki.python.org/moin/PyQt/Tutorials
# http://stackoverflow.com/questions/27212026/how-to-separate-the-ui-and-implementation-in-pyqt

import sys
from PyQt4 import QtCore, QtGui
from countdown_ui import Ui_main_window

# UI class to call the auto generated qt-designer file
class StartQT4(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        ################################
        # Connect signals to our slots #
        ################################
        QtCore.QObject.connect(self.ui.pushButton_1, QtCore.SIGNAL("clicked()"), self.print_test1)
        QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.print_test2)
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.print_test3)

    #############
    # Functions #
    #############
    def print_test1(self):
        print("Button 1 pressed")

    def print_test2(self):
        print("Button 2 pressed")

    def print_test3(self):
        print("Button 3 pressed")


########
# Main #
########
if __name__ == "__main__":
    # Create a PyQT4 application object
    app = QtGui.QApplication(sys.argv)

    # Start the GUI
    myapp = StartQT4()

    # Show the widget on the screen
    myapp.show()

    # Ensure a clean exit
    sys.exit(app.exec_())
