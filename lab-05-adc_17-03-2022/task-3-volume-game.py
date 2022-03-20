import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#the GPIO pin numbers which are connected to the LEDs on our PCB
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

BITS = len(dac)
MAX_VAL = 2**BITS
MAX_VOLTAGE = 3.3
PIN_COMP = 4
PIN_TROYKA = 17


#Initialization, set up all the LED pins as output
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(PIN_TROYKA, GPIO.OUT)
GPIO.setup(PIN_COMP, GPIO.IN)

GPIO.output(dac, 0)
GPIO.output(leds, 0)
GPIO.output(PIN_TROYKA, 1)


#return a decimal from the given binary list
def bin2dec(list_bin):
    return int(''.join(str(c) for c in list_bin), 2)


#Outputs the given decimal value to the DAC
def VoltOut(list_binary):
    for i in range(BITS):
       GPIO.output(dac[i], list_binary[i])
    time.sleep(0.001)


#Binary search out the desired read on the potentiometer
def BinSrchLong():
    table = [0] * BITS

    for i in range(BITS):
        table[i] = 1
        VoltOut(table)
        table[i] = GPIO.input(PIN_COMP)

    return bin2dec(table)


def DisplayVolume(n):
    level = round(n/MAX_VAL*len(leds))
    for i in range(level):
        GPIO.output(leds[i], 1)
        time.sleep(0.001)
    GPIO.output(leds, 0)

#main program
try:
    while True:
        read = BinSrchLong()
        DisplayVolume(read)
        
except KeyboardInterrupt:
    print("\n ctrl+c stopped")
else:
    print("\n No exceptions.")
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()


