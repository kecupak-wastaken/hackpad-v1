import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

# KEYS
keyboard.matrix = KeysScanner(
    pins=[
        board.GP26,  # SW1
        board.GP27,  # SW2
        board.GP28,  # SW3
        board.GP29,  # SW4
    ],
    value_when_pressed=False,
)

keyboard.keymap = [[
    KC.MEDIA_PLAY_PAUSE,
    KC.RGB_MOD,
    KC.MEDIA_PREV_TRACK,
    KC.MEDIA_NEXT_TRACK,
]]

# EC11
encoder = EncoderHandler()
encoder.pins = (
    (board.GP4, board.GP2),  # A, B
)
encoder.map = [
    (KC.VOLD, KC.VOLU),
]
keyboard.modules.append(encoder)

# SK6812 MINI
rgb = RGB(
    pixel_pin=board.GP6,
    num_pixels=5,
    val_limit=80,
    hue_default=160,
    sat_default=255,
    val_default=60,
)
keyboard.extensions.append(rgb)

if __name__ == '__main__':
    keyboard.go()


