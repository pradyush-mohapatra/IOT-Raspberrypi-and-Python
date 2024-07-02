from gpiozero import PWMLED, MCP3008
from time import sleep
import math

# Sensors channel
mcp3008_switch_channel = 0
mcp3008_x_voltage_channel = 1
mcp3008_y_voltage_channel = 2

# Define RGB LED Pins
red_led_pin = 16
green_led_pin = 6
blue_led_pin = 26

# Define the center position when joystick is at rest
center_x_pos = 530
center_y_pos = 504

# Create MCP3008 object for analog sensor reading
mcp3008 = MCP3008()

# Create PWMLED objects for RED LEDs
red_led = PWMLED(red_led_pin)
green_led = PWMLED(green_led_pin)
blue_led = PWMLED(blue_led_pin)

try:
     while True:
          # Read switch state
          switch_state = int(mcp3008.value)

          # Read X and Y position joystick
          x_pos = int((mcp3008.value) * 1023)
          y_pos = int((mcp3008.value) * 1023)

          # Calculate the distance from the centre for joystick position
          distance = math.sqrt((x_pos - center_x_pos) ** 2 + (y_pos - center_y_pos) ** 2)

          # Normalized distance to range (0, 1)
          normalized_distance = distance / math.sqrt((1023 - center_x_pos) ** 2 + (1023 - center_y_pos) ** 2)

          # Set RGB LED colors based on joystick
          red_led.value = normalized_distance
          green_led.value = 1 - normalized_distance
          blue_led.value = switch_state

except KeyboardInterrupt:
     print("Keyboard Interrupt detected. Exiting Program")

finally:
     # Turn off LEDs and clean up GPIO
     red_led.value = 0
     green_led.value = 0
     blue_led.value = 0

     
     











