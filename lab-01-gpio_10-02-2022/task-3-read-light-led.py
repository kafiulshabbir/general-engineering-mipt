import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIN_BLINK_LED = 14
PIN_READ_SWITCH = 15

GPIO.setup(PIN_BLINK_LED, GPIO.OUT)
GPIO.setup(PIN_READ_SWITCH, GPIO.IN)

while True:
    GPIO.output(PIN_BLINK_LED, GPIO.input(PIN_READ_SWITCH))
    time.sleep(1) #Theline is not verified, whether RPi can read acurattely at infinite frequency
    
    
#Connect the circuit as follows:
#Input pin must be connected to GND by a 1kH resistor
#Switch must be connected to the 3.3V without a resistor
#!!!! The drow of 3.3V must be drained to the resistor permanently connected to GND and input
