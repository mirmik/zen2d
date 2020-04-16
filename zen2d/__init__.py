
import math


import zen2d.iobjects

from zen2d.showapi import show, disp

from zen2d.iobjects.line import line as iline, iline_between

from zen2d.unit import unit

from zen2d.trans import translate, rotate



def deg(d):
	return d/180.0*math.pi