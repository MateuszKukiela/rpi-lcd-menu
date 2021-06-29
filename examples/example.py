#!/usr/bin/python

"""
test if lcd display is connected to raspberry on default pins
"""

from rpilcdmenu import *

def main():
	menu = RpiLCDMenu(4,17,[18, 22, 23, 24])
	menu.displayTestScreen()

if __name__ == "__main__":
	main()
