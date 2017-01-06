import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

# construct a pwm object
p = GPIO.PWM(7, 50) # 50 HZ, each pulse is 20 ms
p.start(7.5)        # duty cycle 7.5

try:
    while True:
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(10)
        time.sleep(1)
        p.ChangeDutyCycle(5)
        time.sleep(1)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
    print "user interrupt"

