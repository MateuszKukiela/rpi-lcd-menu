#!/usr/bin/python

"""
multi level menu with physical steering
"""

from rpilcdmenu import *
from rpilcdmenu.items import *
import RPi.GPIO as GPIO
import time
from pigpio_encoder.rotary import Rotary


def main():
    # configure standard button
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    prev_button = 0

    # create menu as in example3
    global menu
    menu = RpiLCDMenu(4, 17, [18, 22, 23, 24])

    function_item1 = FunctionItem("Item 1\nDupa", fooFunction, [1])
    function_item2 = FunctionItem("Item 2", fooFunction, [2])
    menu.append_item(function_item1).append_item(function_item2)

    submenu = RpiLCDSubMenu(menu)
    submenu_item = SubmenuItem("SubMenu (3)", submenu, menu)
    menu.append_item(submenu_item)

    submenu.append_item(FunctionItem("Item 31", fooFunction, [31])).append_item(
        FunctionItem("Item 32", fooFunction, [32]))
    submenu.append_item(FunctionItem("Back", exitSubMenu, [submenu]))

    menu.append_item(FunctionItem("Item 4", fooFunction, [4]))

    menu.start()

    def rotary_callback(counter):
        print("Counter value: ", counter)

    def sw_short():
        global menu
        menu = menu.processEnter()
        print("Switch pressed")

    def up_callback(counter):
        global menu
        menu = menu.processDown()
        print("Up rotation")

    def down_callback(counter):
        global menu
        menu = menu.processUp()
        print("Down rotation")

    my_rotary = Rotary(clk_gpio=5,
                       dt_gpio=6,
                       sw_gpio=13)
    my_rotary.setup_rotary(
        rotary_callback=rotary_callback,
        up_callback=up_callback,
        down_callback=down_callback,
    )
    my_rotary.setup_switch(sw_short_callback=sw_short)

    while True:
        time.sleep(0.001)


def fooFunction(item_index):
    """
    sample method with a parameter
    """
    print("item %d pressed" % (item_index))


def exitSubMenu(submenu):
    return submenu.exit()


if __name__ == "__main__":
    main()
