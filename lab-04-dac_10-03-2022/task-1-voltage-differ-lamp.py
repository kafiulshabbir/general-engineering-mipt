import RPi.GPIO as GPIO
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
    while True:
        input_str = input("Enter a value between 0 and 255 or 'q' to exit: ")

        if(input_str == 'q'):
            break

        if not input_str.isdigit():
            print("Not decimal, try again!")
            continue
        
        value = int(input_str)

        if value >= MAX_VAL:
            print("The entered value is too large, try again!")
            continue
        
        binary = dec2bin(value)
        bin2dac(binary)

        out_voltage = value / MAX_VAL * MAX_VOLTAGE
        print("Decimal entered = {:^3}, output voltage = {:.2f}".format(value, out_voltage))

except KeyboardInterrupt:
    print("\n ctrl+c stopped")
else:
    print("No exceptions.")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

