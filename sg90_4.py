import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

# construct a pwm object
p = GPIO.PWM(7, 50) # 50 HZ, each pulse is 20 ms
p.start(7.5)        # duty cycle 7.5

try:
    while True:
        targetPosition = (float)(input("Enter the target position, between 0~180:"))
        dc = targetPosition/18 + 2.5
        print "targetPosition=", targetPosition, " dc=", dc 
        p.ChangeDutyCycle(dc)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    print "user interrupt"

