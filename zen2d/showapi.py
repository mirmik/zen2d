import zen2d

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from zen2d.view import view
from zen2d.scene import scene

import sys

default_scene = scene()

def disp(i):
	default_scene.add(i)

def show():
	app = QApplication(sys.argv[1:])

	v = view(default_scene)
	v.show()

	app.exec()
