import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)

#the GPIO pin numbers which are connected to the LEDs on our PCB
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

#Constants
BITS = len(dac)
MAX_VAL = 2**BITS
MAX_VOLTAGE = 3.3
PIN_COMP = 4
PIN_TROYKA = 17
CUT_UP_RATIO = 0.95
CUT_DOWN_RATIO = 0.01
SLEEP_TIME_DAC = 0.001
SLEEP_TIME_LED = 0.001
SLEEP_MEASURE = 0.1

#Initialization, set up input and out puts
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(PIN_TROYKA, GPIO.OUT)
GPIO.setup(PIN_COMP, GPIO.IN)

GPIO.output(dac, 0)
GPIO.output(leds, 0)
GPIO.output(PIN_TROYKA, 0)

#return a decimal from the given binary list
def bin2dec(list_bin):
    return int(''.join(str(c) for c in list_bin), 2)


#Outputs the given decimal value to the DAC
def VoltOut(list_binary):
    for i in range(BITS):
       GPIO.output(dac[i], list_binary[i])
    time.sleep(SLEEP_TIME_DAC)

#Outputs Decimals upto 256
def Adc():
    table = [0] * BITS

    for i in range(BITS):
        table[i] = 1
        VoltOut(table)
        table[i] = GPIO.input(PIN_COMP)

    #return bin2dec(table)/MAX_VAL*MAX_VOLTAGE
    return bin2dec(table)


def DisplayVolume(volt_adc):
    GPIO.output(leds, 0)

    level = round(volt_adc/MAX_VAL*len(leds))
    for i in range(level):
        GPIO.output(leds[i], 1)
    
    time.sleep(SLEEP_TIME_LED)
    

#main program
try:
    list_time_x = []
    list_volt_y = []
    #measure the time
    start = time.time()

    number_measure = 0
    charge_capacitor = 1
    volt_on_capacitor = Adc()

    while charge_capacitor or volt_on_capacitor > CUT_DOWN_RATIO*MAX_VAL:
        DisplayVolume(volt_on_capacitor)
        
        if charge_capacitor == 1 and volt_on_capacitor > CUT_UP_RATIO*MAX_VAL:
            charge_capacitor = 0
        
        list_time_x.append(time.time() - start)
        list_volt_y.append(volt_on_capacitor)
        number_measure += 1

        time.sleep(SLEEP_MEASURE)

        GPIO.output(PIN_TROYKA, charge_capacitor)
        volt_on_capacitor = Adc()

        print("n = {}, charging = {}, time-elapsed = {:.1f}, volt = {}".format(number_measure, charge_capacitor, list_time_x[-1], volt_on_capacitor))
        #temporary addition
        #if time.time() - start > 4:
            #break

    with open("data.txt", "w") as outfile:
        for i in list_volt_y:
            outfile.write("{}\n".format(i))
    
    with open("time.txt", "w") as outfile:
        for i in list_time_x:
            outfile.write("{:.3f}\n".format(i))
    
    with open("settings.txt", "w") as outfile:
        outfile.write("{}\n".format(MAX_VOLTAGE/MAX_VAL))
        outfile.write("{:.3f}\n".format(list_time_x[-1]-list_time_x[0]))

    plt.plot(list_volt_y)
    plt.show()
        
except KeyboardInterrupt:
    print("\n keyboard interruption: ctrl+c stopped")
else:
    print("\n none exceptions")
finally:
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()



