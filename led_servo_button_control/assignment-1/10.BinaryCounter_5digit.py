import RPi.GPIO as GPIO # Import Raspberry Pi GPIO Library
from time import sleep

LED1 = 37
LED2 = 35
LED3 = 33
LED4 = 31
LED5 = 29
ON = 1
OFF = 0

GPIO.setwarnings(False) #IGNORE WARNING FOR NOW
GPIO.setmode(GPIO.BOARD) #USE PHYSICAL NUMBERING SYSTEM
GPIO.setup(LED1, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED3, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED4, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(LED5, GPIO.OUT, initial= GPIO.LOW)

try:
    # Count Decimal 0
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 0)
    sleep(0.5)
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 1)
    sleep(0.5)
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 0)
    sleep(0.5)
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 0)
    sleep(0.5)
    GPIO.output(LED1, 0)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 0)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 0)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 0)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 0)
    sleep(0.5)
    
    
    GPIO.output(LED1, 1)
    GPIO.output(LED2, 1)
    GPIO.output(LED3, 1)
    GPIO.output(LED4, 1)
    GPIO.output(LED5, 1)
    sleep(0.5)
    
except KeyboardInterrupt:
    GPIO.cleanup()
