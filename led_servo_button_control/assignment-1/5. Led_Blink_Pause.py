from gpiozero import LED
from signal import pause


led= LED(14)

while True:
    led.blink(on_time = 2, off_time = 3, n = None, background = True)
    pause()
    