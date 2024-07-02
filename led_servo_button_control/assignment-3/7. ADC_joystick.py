from gpiozero import MCP3008
from time import sleep

# Define Sensor channels
swt_channel = 0
vrx_channel = 1
vry_channel = 2

# Create an MCP3008 object for reading analog values
swt_pot = MCP3008(channel = swt_channel)
vrx_pot = MCP3008(channel = vrx_channel)
vry_pot = MCP3008(channel = vry_channel)

try:
     while True:
          # Read the Joystick position data
          vrx_pos = int(vrx_pot.value * 1023)
          vry_pos = int(vry_pot.value * 1023)
          swt_val = int(swt_pot.value)

          print(" -------------------------------------------- ")
          print(" X : {} Y : {} Switch : {}".format(vrx_pos, vry_pos, swt_val))

          sleep(0.5)

except KeyboardInterrupt:
     print("Keyboard interrupt detected. Exiting Program!")












