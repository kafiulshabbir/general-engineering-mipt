import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#the GPIO pin numbers which are connected to the LEDs on our PCB
dac = [26, 19, 13, 6, 5, 11, 9, 10]
BITS = len(dac)
MAX_VAL = 2**BITS
MAX_VOLTAGE = 3.3
PIN_COMP = 4
PIN_TROYKA = 17

#Initialization, set up all the LED pins as output
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(PIN_TROYKA, GPIO.OUT)
GPIO.setup(PIN_COMP, GPIO.IN)

GPIO.output(dac, 0)
GPIO.output(PIN_TROYKA, 1)

#returns a sized-8 list of the digits of the binary
def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(BITS)]


#inputs a decimal number and pass the binary number to the DAC inputs
def bin2dac(binary):
   for i in range(BITS):
       GPIO.output(dac[i], binary[i])

#Outputs the given decimal value to the DAC
def VoltOut(decimal):
    bin2dac(dec2bin(decimal))
    time.sleep(0.001)

def adc():
    for i in range(MAX_VAL):
        VoltOut(i)
        #time.sleep(0.1)
        #print(GPIO.input(PIN_COMP))
        if GPIO.input(PIN_COMP) == 0:
           return i


#main program
try:
    while True:
        read = adc()
        print("Voltage input on COMP = {}".format(read))
        
except KeyboardInterrupt:
    print("\n ctrl+c stopped")
else:
    print("\n No exceptions.")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()


