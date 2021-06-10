# This is a PYQT Project

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from system import Ui_MainWindow as Main
from msgBox import Ui_MainWindow as msgbox

###################---------------for editing there's an error when you  are select and unselct an reselct again there's an error
var = 0

## Tested and for Install Instructions, see README
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    QMainWindow.__init__()


#this class to handle the system and the msgbox together
class Start(QMainWindow):
	"""docstring for StartClass"""
	def __init__(self,):
		QMainWindow.__init__(self)
		self.ui = Main()
		self.ui.setupUi(self)
		self.startSys = System()
		self.startSys.show()
		self.msBox = MsgBox()

class System(QMainWindow):
	"""docstring for SplashScreen"""
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Main()
		self.ui.setupUi(self)
		self.show()
		self.msBox = MsgBox()

class MsgBox(QMainWindow):
	"""docstring for SplashScreen"""
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = msgbox()
		self.ui.setupUi(self)
	# Reomve the title bar
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint )
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	# shadow effect
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(30)
		self.shadow.setXOffset(10)
		self.shadow.setYOffset(10)
		self.shadow.setColor(QColor(88,88,88,60))
	# show close
		self.ui.pushButton.clicked.connect(lambda:self.close())
