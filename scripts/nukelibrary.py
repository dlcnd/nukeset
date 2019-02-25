#coding:utf8
from PySide2.QtWidgets import *
import os
import nuke

class NkLibrary(QWidget):
	def __init__(self):
		super(NkLibrary, self).__init__()
		#variable
		self.libpath = os.getenv("NUKE_PATH")+"/nk/"
		self.appname = "Nuke Library"
		self.version = "v0.1"

		#widget
		self.nklist = QListWidget()
		self.addNkList()
		self.ok = QPushButton("OK")
		self.cancle = QPushButton("Cancle")
		
		#layout
		layout = QVBoxLayout()
		layout.addWidget(self.nklist)
		layout.addWidget(self.ok)
		layout.addWidget(self.cancle)
		self.setWindowTitle(self.appname + " " + self.version)
		self.setLayout(layout)

		#event
		self.ok.clicked.connect(self.pushOK)
		self.cancle.clicked.connect(self.close)
		self.nklist.itemClicked.connect(self.itemClick)
		
	def pushOK(self):
		nuke.nodePaste(self.libpath + self.currentItem)
		self.close()

	def itemClick(self, item):
		self.currentItem = item.text()
		#nuke.tprint(self.currentItem)

	def addNkList(self):
		if not os.path.exists(self.libpath):
			nuke.message(self.libpath + "경로가 존재하지 않습니다.")
		for i in os.listdir(self.libpath):
			base, ext = os.path.splitext(i)
			if ext != ".nk":
					continue
			self.nklist.addItem(QListWidgetItem(i))

def main():
	global customApp
	try:
		customApp.close()
	except:
		pass
	
	customApp = NkLibrary()
	try:
		customApp.show()
	except:
		pass
