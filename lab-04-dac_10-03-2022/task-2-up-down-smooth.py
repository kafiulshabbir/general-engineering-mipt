import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#the GPIO pin numbers which are connected to the LEDs on our PCB
dac = [26, 19, 13, 6, 5, 11, 9, 10]
BITS = len(dac)
MAX_VAL = 2**BITS
MAX_VOLTAGE = 3.3

#Initialization, set up all the LED pins as output
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, 0)


#returns a sized-8 list of the digits of the binary
def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(BITS)]


#inputs a decimal number and pass the binary number to the DAC inputs
def bin2dac(binary):
   for i in range(BITS):
       GPIO.output(dac[i], binary[i])


#main program
try:
    for i in range(MAX_VAL):
        binary = dec2bin(i)
        bin2dac(binary)
        time.sleep(0.1)
    for i in range(MAX_VAL-1 , -1, -1):
        binary = dec2bin(i)
        bin2dac(binary)
        time.sleep(0.05)
        
except KeyboardInterrupt:
    print("\n ctrl+c stopped")
else:
    print("No exceptions.")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

