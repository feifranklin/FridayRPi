import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def blink(pin, numTimes, speed):
    GPIO.setup(pin, GPIO.OUT)
    print 'blink function, pin=', pin, ' numtimes=', numTimes, ' speed=', speed
    for i in range(0, numTimes):
        print 'range: ', i
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(speed)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(speed)
    GPIO.cleanup()

