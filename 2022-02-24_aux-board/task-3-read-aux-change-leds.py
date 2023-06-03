#External code
import RPi.GPIO as GPIO
import time

#nomenclature mode
GPIO.setmode(GPIO.BCM)

#the GPIO pin numbers which are connected to the LEDs on our PCB
list_port = [26, 19, 13, 6, 5, 11, 9, 10]
list_num_display = [0, 5, 32, 64, 127, 255]
size_binary = 8
time_pause_sec = 8


#Initialization, set up all the LED pins as output
GPIO.setup(list_port, GPIO.OUT)
GPIO.output(list_port, 0)


#returns a sized-8 list of the digits of the binary
def Binary(num):
    binary_x8 = []
    for i in range(size_binary):
        binary_x8.append(num % 2)
        num = (num // 2)
    binary_x8.reverse()
    return binary_x8

#Displays particular number on the DAC LEDs
def Display(num_display):
    binary_x8 = Binary(num_display)

    print(num_display)
    print(binary_x8)
    print("-------------------------")
    
    for i in range(size_binary):
        GPIO.output(list_port[i], binary_x8[i])

#main program
for num_display in list_num_display:
    Display(num_display)
    time.sleep(time_pause_sec)
    GPIO.output(list_port, 0)


GPIO.output(list_port, 0)
GPIO.cleanup()
