import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(0)

while True:
    duty = input('duty cycle:')

    if not duty.isdigit():
        print("failed, again!")
        continue

    value = int(duty)
    if value > 100:
        print("Too big")
        continue

    p.ChangeDutyCycle(value)

p.stop()
GPIO.cleanup()
