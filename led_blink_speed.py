import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def blink(pin, numTimes, speed):
    print 'blink function, pin=', pin, ' numtimes=', numTimes, ' speed=', speed
    for i in range(0, numTimes):
        print 'range: ', i
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(speed)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(speed)
    GPIO.cleanup()


if __name__ == '__main__':
    print 'enter main function'
    try:
        blink(7, 5, 2) 
    except KeyboardInterrupt:
        GPIO.cleanup()
        print 'except keyboardinterrupt'

print 'exit'
