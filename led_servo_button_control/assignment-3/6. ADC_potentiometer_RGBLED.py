from gpiozero import RGBLED, MCP3008  #import LEDBarGraph and MCP3008 classes from gpiozero library

#Create an RGBLED object called led
led = RGBLED(red=2,green=3,blue=4)

#Create MCP3008 objects for reading analog input from channels 0,1,2
red_pot= MCP3008(channel = 0)
green_pot= MCP3008(channel = 1)
blue_pot= MCP3008(channel = 2)

try:
    while True:
        #set the red,geen & blue values of RGBLED based on pot values
        led.red=red_pot.value
        led.green=green_pot.value
        led.blue=blue_pot.value
        
except KeyboardInterrupt:
    print("Keyboard Interrupt detected, Exiting Program")        
        