import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB
from kmk.extensions.display import Display
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW 

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D7, board.D8, None, False),)
keyboard.modules.append(encoder_handler)

rgb = RGB(pixel_pin=board.D10, num_pixels=4, hue_default=150, sat_default=255, val_default=100)
keyboard.extensions.append(rgb)

try:
    display = Display(display=SSD1306(i2c=board.I2C(), width=128, height=32))
    keyboard.extensions.append(display)
except Exception as e:
    pass

keyboard.keymap = [[KC.PREV, KC.PLAY, KC.NEXT, KC.COPY, KC.PSTE, KC.MUTE]]
encoder_handler.map = [((KC.VOLD, KC.VOLU),)] 

if __name__ == '__main__':
    keyboard.go()