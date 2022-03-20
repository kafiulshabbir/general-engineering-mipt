import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIN_BLINK_LED = 14
GPIO.setup(PIN_BLINK_LEP, GPIO.OUT)

state_of_led = True

while True:
	GPIO.output(PIN_BLINK_LED, state_of_led)
	time.sleep(0.5)
	state_of_led = not state_of_led
