from gpiozero import LED
from signal import pause


led= LED(14)

while True:
    led.blink()
    pause()
    