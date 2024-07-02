from gpiozero import LEDBarGraph, MCP3008  #import LEDBarGraph and MCP3008 classes from gpiozero library
from signal import pause #Import the pause function from signal module

# Create an MCP3008 object called pot that refers to channel 0
pot = MCP3008(0)

# Create an LEDBarGraph object called graph with 5 LEDS connected to GPIO pins 5,6,13,19,26
graph = LEDBarGraph(5, 6, 13, 19, 26, pwm = True)

try:
    #Set the LEDBarGraph source to the pot input
    graph.source = pot
    
    #Wait for signals (program will run ntil terminated)
    pause()
    
except KeyboardInterrupt:
    print("Keyboard Interrupt detected, Exiting Program")
    