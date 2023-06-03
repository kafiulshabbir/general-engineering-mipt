#External code
import RPi.GPIO as GPIO
import time

#nomenclature mode
GPIO.setmode(GPIO.BCM)

#the GPIO pin numbers which are connected to the LEDs on our PCB
list_led = [21, 20, 16, 12, 7, 8, 25, 24]

#Initialization, set up all the LED pins as output
GPIO.setup(list_led, GPIO.OUT)

#CONSTANTS
num_loop_light = 3
time_pause_sec = 0.2

#Makes a LED blink for time_pause_sec time
def Blink(port):
    GPIO.output(port, 1)
    time.sleep(time_pause_sec)
    GPIO.output(port, 0)

#Makes all 7 LEDs light up and one off once
def LightUp():
    for i in list_led:
        Blink(i)


#main program, which loops  indefinitely

for i in range(num_loop_light):
    LightUp()

GPIO.output(list_led, 0)
GPIO.cleanup()
