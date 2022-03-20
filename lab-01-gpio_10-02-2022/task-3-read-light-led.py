import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIN_BLINK_LED = 14
PIN_READ_SWITCH = 15

GPIO.setup(PIN_BLINK_LED, GPIO.OUT)
GPIO.setup(PIN_READ_SWITCH, GPIO.IN)

while True:
	GPIO.output(PIN_BLINK_LED, GPIO.input(PIN_READ_SWITCH))
    #The next line is not verified, whether RPi can read acurattely at infinite frequency
    time.sleep(1)
    
