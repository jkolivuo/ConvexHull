from math import *
import sys
from PyQt4 import QtGui, QtCore



class Menu(QtGui.QMainWindow):

	def __init__(self):
		QtGui.QMainWindow.__init__(self)

		self.resize(300,300)
		self.center()
		self.setWindowTitle('Convex Hull')

		self.MainMenu()
		

		font = QtGui.QFont('Arial', 12)


		self.show()

	def MainMenu(self):

		self.lbl = QtGui.QLabel('Algorithm selection', self)
		self.lbl.move(90,20)
		self.lbl2 = QtGui.QLabel(' ', self)
		self.lbl2.move(95,110)

		combo = QtGui.QComboBox(self)
		combo.addItem("Select Algorithm")
		combo.addItem("Graham's Scan")
		combo.addItem("Jarvi's March")
		combo.move(90,70)
		
		combo.activated[str].connect(self.onActivated)		

		DrawConvex_btn = QtGui.QPushButton('Draw convex', self)
		Quit_btn = QtGui.QPushButton('Quit', self)
		#Select Algorithm drop down list

		DrawConvex_btn.move(90,150)
		Quit_btn.move(90,200)

		DrawConvex_btn.clicked.connect(self.start)
		Quit_btn.clicked.connect(QtCore.QCoreApplication.instance().quit)

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def onActivated(self, text):
		self.lbl2.setText(text)
		self.lbl2.adjustSize()

	def start(self):
		
		if str(self.lbl2.text()) == "Graham's Scan":
			import drawing_graham
		elif str(self.lbl2.text()) == "Jarvi's March":
			import drawing_jarvis
			

def main():

	app = QtGui.QApplication(sys.argv)
	ex = Menu()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()