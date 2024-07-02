from gpiozero import Servo, MCP3008
from time import sleep

# Initialize the MCP3008 on channel 0
pot = MCP3008(channel=0)
# Initialize the Servo on GPIO pin 18 (make sure this is the correct pin)
servo = Servo(18)

# Function to map the potentiometer value to a servo value
def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

try:
    while True:
        # Read the potentiometer value
        pot_value = pot.value
        # Map the potentiometer value to an angle between -90 and 90 degrees
        angle = map_value(pot_value, 0, 1, -90, 90)
        # Convert the angle to a servo value between -1 and 1
        servo_value = map_value(angle, -90, 90, -1, 1)
        # Set the servo to the mapped value
        servo.value = servo_value
        print("Current angle:", angle)
        sleep(0.1)
except KeyboardInterrupt:
    print("Keyboard Interrupt detected, Exiting Program")
finally:
    # Ensure the servo is detached and freed on exit
    servo.detach()
    servo.close()
