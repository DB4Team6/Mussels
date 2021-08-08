"""
    This module helps writting stuff to the small oled screen.
"""

import ssd1306
from machine import I2C, Pin

# Define I2C
_i2c = I2C(scl=Pin(22), sda=Pin(23), freq=100000)

_oled = ssd1306.SSD1306_I2C(128, 64, _i2c)
_oled.fill(0)

_current_text = []
_MAX_LINES = 7

def _refresh_screen():
    _oled.fill(0)
    cnt = 0
    for line in _current_text:
        cnt += 8
        _oled.text(line, 0, cnt)
    _oled.show()


def print_new_line(line):
    """
        Adds a new line at the end of the screen.
        IF there isn't enough space, the first line
        gets deleted.
    """
    global _MAX_LINES, _current_text

    if len(_current_text) >= _MAX_LINES:
        _current_text = _current_text[1:]
    
    _current_text.append(line)

    _refresh_screen()


def clear_screen():
    """
        Clears the screen.
    """
    global _current_text
    _current_text = []
    _refresh_screen()


def clear_screen_print_line(line):
    """
        Clears the screen, and writes the line.
    """
    global _current_text
    _current_text = [line]
    _refresh_screen()

