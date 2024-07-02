from gpiozero import PWMLED, MCP3008 # import pwm for LED and MCP3008 classes from gpiozero library
from time import sleep

# Create an MCP3008 object called pot that refers to channel 0
pot = MCP3008(0)

# Create a PWMLED object called led that refers to GPIO 14
led = PWMLED(14)

try:
    while True:
        # Check if the pot value is close to zero
        if pot.value < 0.001:
            led.value = 0
        else:
            # otherwise, set the brightness to the pot value
            led.value = pot.value
        print(pot.value)
        
        sleep(0.1)
   
except KeyboardInterrupt:
    print("Keyboard Interrupt detected, Exiting Program")
