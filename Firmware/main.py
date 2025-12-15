import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()

# ===== KEYS =====
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
    KC.MEDIA_PLAY_PAUSE,   # SW1
    KC.RGB_MOD,            # SW2
    KC.MEDIA_PREV_TRACK,   # SW3
    KC.MEDIA_NEXT_TRACK,   # SW4
]]

# ===== ROTARY ENCODER (EC11) =====
encoder = EncoderHandler()
encoder.pins = (
    (board.GP4, board.GP2, board.GP1),  # A, B, Button
)
encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)
]
keyboard.modules.append(encoder)

# ===== RGB (5x SK6812 MINI) =====
rgb = RGB(
    pixel_pin=board.GP6,  # DIN
    num_pixels=5,
    val_limit=80,
    hue_default=160,      # blue
    sat_default=255,
    val_default=60,
)
keyboard.extensions.append(rgb)

# ===== START =====
if __name__ == '__main__':
    keyboard.go()
