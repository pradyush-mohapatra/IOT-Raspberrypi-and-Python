from gpiozero import DigitalOutputDevice
from time import sleep


led= DigitalOutputDevice(14)

while True:
    led.on()
    sleep(3)
    led.off()
    sleep(1)
